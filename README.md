# Speech-to-Text Model Benchmark

A professional benchmarking framework for evaluating Azure OpenAI speech-to-text models. This toolkit provides comprehensive accuracy and latency measurements using controlled audio datasets, with detailed Word Error Rate (WER) analysis and automated reporting.

## Features

- **Automated Test Discovery** – Automatically pairs audio files with reference transcripts from your dataset directory
- **Multi-Model Support** – Benchmarks multiple Azure OpenAI models including:
  - Chat-based models: `gpt-audio`, `gpt-audio-mini`, `gpt-4o-audio-preview`
  - Transcription models: `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`
- **Comprehensive Metrics** – Calculates raw WER, latency, and detailed error analysis (substitutions, insertions, deletions)
- **Professional Reporting** – Generates executive summaries with model rankings, comparison tables, and detailed per-sample breakdowns
- **Detailed Error Analysis** – Shows exactly which words were substituted, inserted, or deleted for each model
- **Flexible CLI** – Target specific audio files, list available samples, or skip report generation with command-line options
- **Modular Architecture** – Clean, maintainable codebase with separate modules for configuration, testing, metrics, and reporting

## Project Structure

```
.
├── data/
│   ├── mine/processed/       # User-created test samples (not used)
│   └── off/processed/        # Official test audio samples
│       ├── audio_clean.wav
│       ├── audio_clean_reference.txt
│       ├── audio_noisy.wav
│       └── audio_noisy_reference.txt
├── reports/                  # Generated benchmark reports
│   ├── stt_report.md
│   └── stt_report_normalized.md
├── scripts/
│   └── convert_audio.sh      # Audio conversion utility
├── src/                      # Source code (modular architecture)
│   ├── __init__.py
│   ├── config.py             # Configuration and model definitions
│   ├── test_discovery.py     # Test case discovery and filtering
│   ├── transcription.py      # API communication for both chat and transcription models
│   ├── metrics.py            # WER calculation and error analysis
│   ├── llm_normalization.py  # LLM normalization (disabled)
│   ├── reporting.py          # Comprehensive benchmark report generation
│   ├── runner.py             # Test orchestration
│   └── main.py               # Main entry point with CLI
├── tests/                    # Test files
├── logs/                     # Application logs
├── .env                      # Environment variables (not in git)
├── .env.example              # Environment variables template
├── pyproject.toml            # Project dependencies and metadata
├── uv.lock                   # UV lock file
├── README.md                 # This file
├── ARCHITECTURE.md           # Architecture documentation
└── MODULE_DEPENDENCIES.md    # Module dependencies
```

## Quick Start

### Prerequisites

- Python 3.13+ (or Python 3.8+ with compatibility adjustments)
- Azure OpenAI resource with deployed speech models
- Audio samples with corresponding reference transcripts

### Installation

1. **Clone or download the project**

2. **Install dependencies:**
   ```bash
   pip install -e .
   ```

   Or using `uv`:
   ```bash
   uv pip install -r pyproject.toml
   ```

3. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```

   Edit `.env` with your Azure credentials:
   ```bash
   AZURE_API_KEY=your_azure_openai_api_key
   AZURE_ENDPOINT=https://your-resource.cognitiveservices.azure.com
   # Note: AUDIO_DATA_DIR is not needed - hardcoded to data/off/processed
   ```

4. **Prepare your dataset:**
   ```
   data/off/processed/
   ├── audio_clean.wav
   ├── audio_clean_reference.txt
   ├── audio_noisy.wav
   ├── audio_noisy_reference.txt
   └── ...
   ```

   Each `audio_*.wav` file must have a corresponding `audio_*_reference.txt` file with the ground truth transcript.

## Usage

### Basic Commands

**Run all benchmarks:**
```bash
python -m src.main
```

**List available test cases:**
```bash
python -m src.main --list
```

**Test specific audio files:**
```bash
python -m src.main --audio audio_clean audio_noisy
```

**Skip report generation:**
```bash
python -m src.main --skip-report
```

### CLI Options

| Option | Description |
|--------|-------------|
| `--list` | Display all discovered audio/reference pairs and exit |
| `-a, --audio FILES...` | Run benchmarks only on specified files (accepts names, stems, or paths) |
| `--skip-report` | Skip generating the detailed Markdown report |

### Example Output

**Console Summary:**
```
================================================================================
📊 BENCHMARK RESULTS - MODEL COMPARISON
================================================================================

Model                     Avg WER    Latency      Errors     Status
--------------------------------------------------------------------------------
gpt-4o-mini-transcribe    5.84%        1.72s    9          ✅ 2
gpt-audio-mini            7.79%        3.85s    12         ✅ 2
gpt-4o-audio-preview      8.44%        1.83s    13         ✅ 2
gpt-4o-transcribe         9.09%        2.68s    14         ✅ 2
gpt-audio                 12.99%       2.45s    20         ✅ 2

================================================================================
🏆 BEST MODEL: gpt-4o-mini-transcribe
   Average WER: 5.84%
   Average Latency: 1.72s
   Total Errors: 9
================================================================================
```

**Markdown Report:**
A comprehensive benchmark report is generated at `reports/stt_report_normalized.md` containing:

**Executive Summary:**
- Model performance comparison table (ranked by WER)
- Best model announcement with key metrics
- Error type breakdown (substitutions, insertions, deletions)

**Detailed Results:**
- Per-audio sample analysis
- Side-by-side model comparison tables
- Full transcripts from each model
- Detailed error analysis showing exact mismatches

## Advanced Usage

### Adding New Models

Edit [src/config.py](src/config.py) to add model configurations:

```python
MODELS = {
    "your-new-model": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/your-model/...",
        "deployment": "your-model",
        "type": "chat",  # or "transcription" for audio transcription models
        "api_version": "2025-01-01-preview",
    }
}

ACTIVE_MODELS = [
    "gpt-audio",
    "gpt-audio-mini",
    "gpt-4o-transcribe",
    "gpt-4o-mini-transcribe",
    "your-new-model",  # Add here
]
```

**Model Types:**
- `"chat"` - For chat-based audio models (uses chat completions API)
- `"transcription"` - For dedicated transcription models (uses audio transcriptions API)

### Using as a Library

Import and use individual modules in your own scripts:

```python
from src.config import ACTIVE_MODELS
from src.test_discovery import discover_test_cases
from src.runner import test_all_models
from src.reporting import print_results, generate_report

# Discover test cases (returns list of (audio_path, reference_path) tuples)
cases = discover_test_cases()

# Prepare test cases with reference text
test_cases = []
all_results = []

for audio_path, ref_path in cases:
    if ref_path:
        reference = ref_path.read_text(encoding='utf-8').strip()
        test_cases.append({
            'audio_path': audio_path,
            'reference_path': ref_path,
            'reference_text': reference
        })
        results = test_all_models(audio_path, reference)
        all_results.append(results)

# Display results
print_results(all_results)

# Generate markdown report
generate_report(test_cases, all_results)
```

### Custom Metrics

Add new metric calculations in [src/metrics.py](src/metrics.py):

```python
def calculate_custom_metric(reference: str, hypothesis: str) -> float:
    """Your custom metric calculation."""
    # Implementation here
    return score
```

## Data Preparation

### Audio Format Requirements

- **Format:** WAV (16 kHz, mono recommended)
- **Naming:** `audio_*.wav` (e.g., `audio_clean.wav`, `audio_noisy.wav`)
- **Location:** `data/off/processed/`

### Reference Transcripts

- **Format:** Plain text (.txt) with UTF-8 encoding
- **Naming:** Must match audio file with `_reference` suffix (e.g., `audio_clean_reference.txt`)
- **Content:** Exact transcription of the audio file
- **Location:** Same directory as audio files (`data/off/processed/`)

### Current Test Dataset

The framework currently uses 2 audio samples:
- `audio_clean.wav` - Clean audio recording
- `audio_noisy.wav` - Noisy audio recording

Both with corresponding reference files for WER calculation.

## Architecture

The project uses a modular architecture for maintainability and extensibility:

- **config.py** – Centralized configuration with model definitions and API endpoints
- **test_discovery.py** – Automatically discovers and pairs audio files with references
- **transcription.py** – Handles API communication for both chat and transcription models
- **metrics.py** – Calculates raw WER and performs detailed error analysis
- **reporting.py** – Generates comprehensive benchmark reports with executive summaries
- **runner.py** – Orchestrates test execution across multiple models
- **main.py** – Entry point with CLI argument parsing

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `AZURE_API_KEY` | Yes | – | Your Azure OpenAI API key |
| `AZURE_ENDPOINT` | No | `https://draftspeechtotext.cognitiveservices.azure.com` | Azure OpenAI endpoint URL |

### Model Configuration

Models are configured in [src/config.py](src/config.py). Each model requires:
- Deployment name
- API endpoint URL
- API version
- Model type (`"chat"` or `"transcription"`)

### Test Configuration

The framework is configured to:
- Use only `data/off/processed/` directory for audio samples
- Calculate raw WER (no normalization)
- Test 5 models: gpt-audio, gpt-audio-mini, gpt-4o-transcribe, gpt-4o-mini-transcribe, gpt-4o-audio-preview

## Metrics & Analysis

### Word Error Rate (WER)

The primary metric for transcription quality:
```
WER = (Substitutions + Insertions + Deletions) / Total Reference Words
```

Raw WER is calculated by comparing the model's transcript directly against the reference text (case-insensitive).

### Error Analysis

Detailed breakdown includes:
- **Substitutions** – Words incorrectly transcribed
- **Insertions** – Words added that weren't in the reference
- **Deletions** – Words omitted from the reference

### Latency

Measures API response time from request to completion (in seconds).

## Best Practices

1. **Audio Quality** – Use clear, noise-free recordings for accurate baseline measurements
2. **Reference Transcripts** – Ensure reference transcripts are accurate and match audio exactly
3. **Consistent Format** – Use 16 kHz mono WAV files for best results
4. **Batch Size** – Be mindful of Azure API rate limits when testing large datasets
5. **Version Control** – Keep historical reports for tracking model improvements over time

## Troubleshooting

### "AZURE_API_KEY is not set"
Ensure your `.env` file exists and contains valid Azure credentials.

### "Audio data directory not found"
The framework is configured to use `data/off/processed/`. Ensure this directory exists and contains your audio files.

### "Reference file missing"
Each `audio_*.wav` file must have a corresponding `audio_*_reference.txt` file with the same base name (e.g., `audio_clean.wav` → `audio_clean_reference.txt`).

### Import Errors
Activate your virtual environment:
```bash
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
```

## Benchmark Results

Based on testing with 2 audio samples (clean and noisy):

**🏆 Winner: gpt-4o-mini-transcribe**
- Average WER: 5.84%
- Average Latency: 1.72s
- Best for: Accuracy and speed

**Full Rankings:**
1. gpt-4o-mini-transcribe: 5.84% WER, 1.72s
2. gpt-audio-mini: 7.79% WER, 3.85s
3. gpt-4o-audio-preview: 8.44% WER, 1.83s
4. gpt-4o-transcribe: 9.09% WER, 2.68s
5. gpt-audio: 12.99% WER, 2.45s

## Limitations & Notes

- **GPT Realtime** – Not currently supported (requires websocket session)
- **Whisper Models** – Removed from testing (focus on OpenAI GPT models only)
- **Normalization** – Disabled to show true model performance
- **Audio Length** – Ensure audio files comply with Azure request size limits
- **Rate Limiting** – 1-second delay between API calls (configurable in [src/config.py](src/config.py))

## Contributing

The modular architecture makes contributions straightforward:
- Bug fixes: Target the specific module
- New features: Extend relevant modules
- New models: Update configuration
- New metrics: Extend metrics module

## Summary

This benchmark framework provides a clear, objective comparison of Azure OpenAI speech-to-text models. The comprehensive reports help you make informed decisions about which model best fits your use case based on accuracy, speed, and error characteristics.

**Key Takeaways:**
- **gpt-4o-mini-transcribe** offers the best balance of accuracy and speed
- All models handle clean audio better than noisy audio
- Transcription models are generally faster than chat-based models
- Detailed error analysis helps identify specific model weaknesses

---

**Ready to benchmark your models?** Run `python -m src.main` to get started! 🎤📊
