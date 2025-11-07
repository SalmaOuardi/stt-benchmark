"""
Reporting module.
Handles console output and markdown report generation.
"""

from pathlib import Path
from typing import List, Dict, Any

from metrics import summarize_errors


def print_results(all_results: List[List[Dict[str, Any]]]) -> None:
    """
    Print aggregated benchmark results to console.

    Shows meaningful WER (after intelligent LLM normalization) as the primary metric
    for cases with references. For transcription-only cases, shows latency only.

    Args:
        all_results: List of result lists, one per test case
    """
    print(f"\n{'='*60}")
    print("📊 BENCHMARK RESULTS")
    print('='*60)

    # Aggregate stats
    stats = {}
    has_wer_data = False

    for results in all_results:
        for r in results:
            if not r["success"]:
                continue

            model = r["model"]
            if model not in stats:
                stats[model] = {"wers": [], "latencies": []}

            # Only add WER if available (not None)
            if r.get("wer") is not None:
                stats[model]["wers"].append(r["wer"])
                has_wer_data = True

            stats[model]["latencies"].append(r["latency"])

    # Print table
    if has_wer_data:
        print(f"\n{'Model':<30} {'WER':<12} {'Avg Latency':<15}")
        print('-'*60)

        for model, data in sorted(stats.items()):
            if data["wers"]:
                avg_wer = sum(data["wers"]) / len(data["wers"])
                wer_display = f"{avg_wer:>6.2f}%"
            else:
                wer_display = "  n/a"

            avg_lat = sum(data["latencies"]) / len(data["latencies"])
            print(f"{model:<30} {wer_display:<12} {avg_lat:>6.2f}s")

        # Find winner (only if we have WER data)
        models_with_wer = {m: d for m, d in stats.items() if d["wers"]}
        if models_with_wer:
            winner = min(models_with_wer.items(), key=lambda x: sum(x[1]["wers"])/len(x[1]["wers"]))
            print(f"\n🏆 WINNER: {winner[0]} (Lowest WER)")

        print("\nℹ️  WER calculated using LLM-based normalization (semantic errors only)")
    else:
        # Transcription-only mode
        print(f"\n{'Model':<30} {'Avg Latency':<15}")
        print('-'*60)

        for model, data in sorted(stats.items()):
            avg_lat = sum(data["latencies"]) / len(data["latencies"])
            print(f"{model:<30} {avg_lat:>6.2f}s")

        print("\nℹ️  Transcription-only mode (no reference texts provided)")


def generate_report(
    test_cases: List[Dict[str, Any]],
    all_results: List[List[Dict[str, Any]]],
    output_path: str = "reports/stt_report.md"
) -> None:
    """
    Create detailed markdown reports.

    Generates two separate reports:
    1. Evaluation report (for cases with references) - includes WER
    2. Transcription report (for cases without references) - just transcriptions

    Args:
        test_cases: List of test case dictionaries with audio/reference paths
        all_results: List of result lists, one per test case
        output_path: Path where the markdown report should be written
    """
    report_path = Path(output_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    # Separate cases into evaluation and transcription-only
    eval_cases = []
    eval_results = []
    transcription_cases = []
    transcription_results = []

    for case, results in zip(test_cases, all_results):
        if case["reference_text"] is not None:
            eval_cases.append(case)
            eval_results.append(results)
        else:
            transcription_cases.append(case)
            transcription_results.append(results)

    # Generate evaluation report if there are cases with references
    if eval_cases:
        _generate_evaluation_report(eval_cases, eval_results, output_path)

    # Generate transcription report if there are transcription-only cases
    if transcription_cases:
        transcription_path = str(report_path).replace(".md", "_transcriptions.md")
        _generate_transcription_report(transcription_cases, transcription_results, transcription_path)


def _generate_evaluation_report(
    test_cases: List[Dict[str, Any]],
    all_results: List[List[Dict[str, Any]]],
    output_path: str
) -> None:
    """Generate evaluation report with WER metrics."""
    report_path = Path(output_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# Speech-to-Text Evaluation Report")
    lines.append("")
    lines.append(f"Generated from {len(test_cases)} audio samples with reference transcripts.\n")

    for (case, results) in zip(test_cases, all_results):
        audio_path = case["audio_path"]
        reference_path = case["reference_path"]
        reference_text = case["reference_text"]

        lines.append(f"## {audio_path.name}")
        lines.append(f"- Audio file: `{audio_path}`")
        lines.append(f"- Reference transcript: `{reference_path}`")
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
            wer_value = result.get("wer")
            latency = result.get("latency")
            summary = result.get("errors", {})
            details = result.get("error_details", [])
            normalized_reference = result.get("normalized_reference")
            normalized_transcript = result.get("normalized_transcript")
            raw_wer = result.get("raw_wer")

            lines.append(f"- Status: ✅ Success")
            lines.append(f"- Latency: {latency:.2f}s")
            lines.append(f"- **Word Error Rate (Meaningful): {wer_value:.2f}%**")
            lines.append(f"- Transcript: {transcript_text}")

            # Show meaningful errors (after normalization)
            lines.append(
                f"- Meaningful Errors: substitutions={summary.get('substitutions', 0)}, "
                f"insertions={summary.get('insertions', 0)}, "
                f"deletions={summary.get('deletions', 0)}"
            )

            # Add meaningful error details
            if details:
                lines.append("#### Meaningful Error Details (Semantic differences only)")
                for issue in details:
                    lines.append(
                        f"- {issue['type'].capitalize()}: "
                        f"expected \"{issue['expected']}\" | "
                        f"actual \"{issue['actual']}\""
                    )
            else:
                lines.append("- Meaningful Errors: None 🎉")

            # Add raw WER for comparison (if available)
            if raw_wer is not None and raw_wer != wer_value:
                lines.append(f"- Raw WER (before normalization): {raw_wer:.2f}%")

            # Add normalized texts for debugging
            if normalized_reference and normalized_transcript:
                lines.append(f"- Normalized Reference: {normalized_reference}")
                lines.append(f"- Normalized Transcript: {normalized_transcript}")

            lines.append("")
        lines.append("---\n")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n📝 Evaluation report written to {report_path}")


def _generate_transcription_report(
    test_cases: List[Dict[str, Any]],
    all_results: List[List[Dict[str, Any]]],
    output_path: str
) -> None:
    """Generate transcription-only report without WER metrics."""
    report_path = Path(output_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# Speech-to-Text Transcription Report")
    lines.append("")
    lines.append(f"Generated from {len(test_cases)} audio samples without reference transcripts.\n")

    for (case, results) in zip(test_cases, all_results):
        audio_path = case["audio_path"]

        lines.append(f"## {audio_path.name}")
        lines.append(f"- Audio file: `{audio_path}`")
        lines.append("")

        for result in results:
            model_name = result["model"]
            lines.append(f"### Model: {model_name}")

            if not result["success"]:
                lines.append(f"- Status: ❌ Failed")
                lines.append(f"- Error: `{result['error']}`\n")
                continue

            transcript_text = result["transcript"]
            latency = result.get("latency")

            lines.append(f"- Status: ✅ Success")
            lines.append(f"- Latency: {latency:.2f}s")
            lines.append(f"- **Transcript:**")
            lines.append(f"```")
            lines.append(transcript_text)
            lines.append(f"```")
            lines.append("")

        lines.append("---\n")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n📝 Transcription report written to {report_path}")
