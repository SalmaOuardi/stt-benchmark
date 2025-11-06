import os
import time
import base64
import json
import re
import unicodedata
from pathlib import Path
from difflib import SequenceMatcher
from openai import AzureOpenAI
from jiwer import wer
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Shared Azure OpenAI configuration
AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT", "https://draftspeechtotext.cognitiveservices.azure.com")
DATA_ROOT = Path(os.getenv("AUDIO_DATA_DIR", "data/processed")).expanduser()
NORMALIZATION_CONFIG_PATH = Path(
    os.getenv("NORMALIZATION_CONFIG", "config/normalization.json")
).expanduser()

if not AZURE_API_KEY:
    raise EnvironmentError(
        "AZURE_API_KEY is not set. Please add it to your environment or .env file."
    )

# Azure speech models and their target endpoints
MODELS = {
    "whisper": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/whisper/audio/translations?api-version=2024-06-01",
        "type": "whisper",
        "deployment": "whisper",
        "api_version": "2024-06-01",
    },
    "gpt-audio": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/gpt-audio/chat/completions?api-version=2025-01-01-preview",
        "deployment": "gpt-audio",
        "type": "chat",
        "api_version": "2025-01-01-preview",
    },
    "gpt-audio-mini": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/gpt-audio-mini/chat/completions?api-version=2025-01-01-preview",
        "deployment": "gpt-audio-mini",
        "type": "chat",
        "api_version": "2025-01-01-preview",
    },
    "gpt-4o-audio-preview": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/gpt-4o-audio-preview/chat/completions?api-version=2025-01-01-preview",
        "deployment": "gpt-4o-audio-preview",
        "type": "chat",
        "api_version": "2025-01-01-preview",
    }
}

ACTIVE_MODELS = [
    "gpt-audio",
    "gpt-audio-mini",
    "gpt-4o-audio-preview",
]

def load_normalization_rules():
    """Load normalization configuration from disk."""
    if NORMALIZATION_CONFIG_PATH.exists():
        try:
            with NORMALIZATION_CONFIG_PATH.open("r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    data.setdefault("replacements", [])
                    return data
        except Exception as exc:
            print(f"⚠️  Failed to load normalization config: {exc}")
    return {"replacements": []}

NORMALIZATION_RULES = load_normalization_rules()

def strip_accents(text):
    """Remove accent marks from text."""
    return "".join(
        ch for ch in unicodedata.normalize("NFD", text)
        if unicodedata.category(ch) != "Mn"
    )

def normalize_text(text):
    """Canonicalize transcription text using configured rules."""
    normalized = unicodedata.normalize("NFKC", text)
    normalized = normalized.replace("\u00a0", " ")
    for ch in ("’", "‘", "`", "´"):
        normalized = normalized.replace(ch, "'")
    for ch in ("“", "”", "„"):
        normalized = normalized.replace(ch, "\"")
    normalized = normalized.lower() if NORMALIZATION_RULES.get("lowercase", True) else normalized
    
    for rule in NORMALIZATION_RULES.get("replacements", []):
        pattern = rule.get("pattern")
        replacement = rule.get("replacement", "")
        if pattern:
            normalized = re.sub(pattern, replacement, normalized)
    
    if NORMALIZATION_RULES.get("strip_accents"):
        normalized = strip_accents(normalized)
    
    if NORMALIZATION_RULES.get("remove_punctuation", True):
        normalized = re.sub(r"(?<!\d)[.,!?;:]+", " ", normalized)
        normalized = re.sub(r"\.(?=\s|$)", " ", normalized)
    
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized

def discover_test_cases():
    """Pair each WAV file with its matching reference transcript."""
    if not DATA_ROOT.exists():
        raise FileNotFoundError(f"Audio data directory not found: {DATA_ROOT}")
    
    cases = []
    for audio_path in sorted(DATA_ROOT.glob("audio_*.wav")):
        parts = audio_path.stem.split("_")
        if len(parts) < 2:
            print(f"⚠️  Skipping unexpected file name: {audio_path.name}")
            continue
        base_name = "_".join(parts[:2])
        reference_path = audio_path.with_name(f"{base_name}_reference.txt")
        if not reference_path.exists():
            print(f"⚠️  Reference file missing for {audio_path.name}")
            continue
        cases.append((audio_path, reference_path))
    return cases

def test_whisper(audio_path):
    """Test Whisper (simple file upload)."""
    print("🎤 Testing Whisper...")
    
    with open(audio_path, "rb") as f:
        files = {"file": f}
        headers = {"api-key": AZURE_API_KEY}
        
        start = time.time()
        response = requests.post(MODELS["whisper"]["url"], headers=headers, files=files)
        latency = time.time() - start
    
    if response.ok:
        return {
            "model": "whisper",
            "transcript": response.json().get("text", ""),
            "latency": latency,
            "success": True
        }
    else:
        return {"model": "whisper", "error": response.text, "success": False}

def test_gpt_audio(audio_path, model_name):
    """Test GPT audio models"""
    print(f"🎤 Testing {model_name}...")
    
    client = AzureOpenAI(
        api_key=AZURE_API_KEY,
        api_version=MODELS[model_name]["api_version"],
        azure_endpoint=AZURE_ENDPOINT
    )
    
    # Encode audio to base64
    with open(audio_path, "rb") as f:
        audio_b64 = base64.b64encode(f.read()).decode()
    
    audio_suffix = audio_path.suffix.lower() if isinstance(audio_path, Path) else os.path.splitext(audio_path)[1].lower()
    audio_format = "wav" if audio_suffix == ".wav" else "mp3"
    
    try:
        start = time.time()
        response = client.chat.completions.create(
            model=MODELS[model_name]["deployment"],
            modalities=["text"],
            audio={"voice": "alloy", "format": audio_format},
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "input_audio",
                        "input_audio": {"data": audio_b64, "format": audio_format}
                    },
                    {
                        "type": "text",
                        "text": "Transcribe this French audio exactly. Return only the transcript."
                    }
                ]
            }]
        )
        latency = time.time() - start
        
        return {
            "model": model_name,
            "transcript": response.choices[0].message.content,
            "latency": latency,
            "success": True
        }
    except Exception as e:
        return {"model": model_name, "error": str(e), "success": False}

def calculate_wer(reference, hypothesis):
    """Calculate Word Error Rate"""
    return wer(reference, hypothesis) * 100

def summarize_errors(reference, hypothesis):
    """Return token-level error counts and details for hypothesis vs reference."""
    ref_tokens = reference.split()
    hyp_tokens = hypothesis.split()
    
    matcher = SequenceMatcher(None, ref_tokens, hyp_tokens)
    summary = {"substitutions": 0, "insertions": 0, "deletions": 0}
    details = []
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        ref_segment = " ".join(ref_tokens[i1:i2])
        hyp_segment = " ".join(hyp_tokens[j1:j2])
        
        if tag == "replace":
            summary["substitutions"] += max(i2 - i1, j2 - j1)
        elif tag == "delete":
            summary["deletions"] += (i2 - i1)
        elif tag == "insert":
            summary["insertions"] += (j2 - j1)
        
        details.append({
            "type": tag,
            "expected": ref_segment,
            "actual": hyp_segment
        })
    
    return summary, details

def test_all(audio_path, reference_text):
    """Test active models on one audio file and capture evaluation metrics."""
    print(f"\n{'='*60}")
    print(f"Testing: {audio_path}")
    print(f"Reference: {reference_text[:100]}...")
    print('='*60)
    
    results = []
    normalized_reference = normalize_text(reference_text)
    
    for model in ACTIVE_MODELS:
        r = test_gpt_audio(audio_path, model)
        if r["success"]:
            r["wer"] = calculate_wer(reference_text, r["transcript"])
            r["errors"], r["error_details"] = summarize_errors(reference_text, r["transcript"])
            r["normalized_reference"] = normalized_reference
            normalized_transcript = normalize_text(r["transcript"])
            r["normalized_transcript"] = normalized_transcript
            r["normalized_wer"] = calculate_wer(normalized_reference, normalized_transcript)
            (
                r["normalized_errors"],
                r["normalized_error_details"],
            ) = summarize_errors(normalized_reference, normalized_transcript)
        results.append(r)
        time.sleep(1)  # Avoid rate limits
    
    return results

def print_results(all_results):
    """Print comparison table"""
    print(f"\n{'='*60}")
    print("📊 BENCHMARK RESULTS")
    print('='*60)
    
    # Aggregate stats
    stats = {}
    for results in all_results:
        for r in results:
            if not r["success"]:
                continue
            model = r["model"]
            if model not in stats:
                stats[model] = {"wers": [], "normalized_wers": [], "latencies": []}
            stats[model]["wers"].append(r["wer"])
            if "normalized_wer" in r:
                stats[model]["normalized_wers"].append(r["normalized_wer"])
            stats[model]["latencies"].append(r["latency"])
    
    # Print table
    print(f"\n{'Model':<20} {'Avg WER':<12} {'Norm WER':<12} {'Avg Latency':<15}")
    print('-'*60)
    for model, data in sorted(stats.items()):
        avg_wer = sum(data["wers"]) / len(data["wers"])
        if data["normalized_wers"]:
            avg_norm = sum(data["normalized_wers"]) / len(data["normalized_wers"])
            norm_display = f"{avg_norm:>6.2f}%"
        else:
            norm_display = "  n/a"
        avg_lat = sum(data["latencies"]) / len(data["latencies"])
        print(f"{model:<20} {avg_wer:>6.2f}%     {norm_display:<12} {avg_lat:>6.2f}s")
    
    # Find winner
    winner = min(stats.items(), key=lambda x: sum(x[1]["wers"])/len(x[1]["wers"]))
    print(f"\n🏆 WINNER: {winner[0]} (Lowest WER)")

def generate_report(test_cases, all_results, output_path="reports/stt_report.md"):
    """Create a detailed markdown report comparing transcripts to ground truth."""
    report_path = Path(output_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    lines = []
    lines.append("# Speech-to-Text Benchmark Report")
    lines.append("")
    lines.append(f"Generated from {len(test_cases)} audio samples.\n")
    
    for (case, results) in zip(test_cases, all_results):
        audio_path = case["audio_path"]
        reference_text = case["reference_text"]
        lines.append(f"## {audio_path.name}")
        lines.append(f"- Audio file: `{audio_path}`")
        lines.append(f"- Reference transcript: `{case['reference_path']}`")
        lines.append(f"- Reference text: {reference_text}")
        lines.append("")
        
        for result in results:
            model_name = result["model"]
            lines.append(f"### Model: {model_name}")
            if not result["success"]:
                lines.append(f"- Status: ❌ Failed")
                lines.append(f"- Error: `{result['error']}`\n")
                continue
            
            transcript_text = result["transcript"]
            wer_value = result.get("wer", float("nan"))
            latency = result.get("latency")
            summary = result.get("errors")
            details = result.get("error_details")
            normalized_reference = result.get("normalized_reference")
            normalized_transcript = result.get("normalized_transcript")
            normalized_wer = result.get("normalized_wer")
            normalized_summary = result.get("normalized_errors")
            normalized_details = result.get("normalized_error_details")
            
            if summary is None or details is None:
                summary, details = summarize_errors(reference_text, transcript_text)
            
            lines.append(f"- Status: ✅ Success")
            lines.append(f"- Latency: {latency:.2f}s")
            lines.append(f"- Word Error Rate: {wer_value:.2f}%")
            lines.append(f"- Transcript: {transcript_text}")
            lines.append(f"- Errors: substitutions={summary['substitutions']}, insertions={summary['insertions']}, deletions={summary['deletions']}")
            if details:
                lines.append("#### Error Details")
                for issue in details:
                    lines.append(f"- {issue['type'].capitalize()}: expected \"{issue['expected']}\" | actual \"{issue['actual']}\"")
            else:
                lines.append("- Error Details: None 🎉")
            
            if normalized_reference and normalized_transcript and normalized_wer is not None:
                lines.append(f"- Normalized Word Error Rate: {normalized_wer:.2f}%")
                lines.append(f"- Normalized Reference: {normalized_reference}")
                lines.append(f"- Normalized Transcript: {normalized_transcript}")
                norm_counts = normalized_summary or {"substitutions": 0, "insertions": 0, "deletions": 0}
                lines.append(
                    "- Normalized Errors: substitutions="
                    f"{norm_counts.get('substitutions', 0)}, "
                    f"insertions={norm_counts.get('insertions', 0)}, "
                    f"deletions={norm_counts.get('deletions', 0)}"
                )
                if normalized_details:
                    lines.append("#### Normalized Error Details")
                    for issue in normalized_details:
                        lines.append(
                            f"- {issue['type'].capitalize()}: expected \"{issue['expected']}\" | actual \"{issue['actual']}\""
                        )
                else:
                    lines.append("- Normalized Error Details: None 🎉")
            lines.append("")
        lines.append("---\n")
    
    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n📝 Detailed report written to {report_path}")

if __name__ == "__main__":
    all_results = []
    cases = discover_test_cases()
    test_cases = []
    
    if not cases:
        print(f"⚠️  No test cases found in {DATA_ROOT}")
    
    for audio_path, reference_path in cases:
        reference_text = reference_path.read_text(encoding="utf-8").strip()
        results = test_all(audio_path, reference_text)
        all_results.append(results)
        test_cases.append({
            "audio_path": audio_path,
            "reference_path": reference_path,
            "reference_text": reference_text
        })
    
    if all_results:
        print_results(all_results)
        generate_report(test_cases, all_results, output_path="reports/stt_report_normalized.md")
    
    print("\nℹ️  GPT Realtime testing is not automated because the realtime API requires a websocket session, which this script does not yet establish.")
