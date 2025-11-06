# Speech-to-Text Model Benchmark

A professional benchmarking framework for evaluating Azure OpenAI speech-to-text models. This toolkit provides comprehensive accuracy and latency measurements using controlled audio datasets, with detailed Word Error Rate (WER) analysis and automated reporting.

## Features

- **Automated Test Discovery** – Automatically pairs audio files with reference transcripts from your dataset directory
- **Multi-Model Support** – Benchmarks multiple Azure OpenAI models (`gpt-audio`, `gpt-audio-mini`, `gpt-4o-audio-preview`) in a single run
- **Comprehensive Metrics** – Calculates WER (both raw and normalized), latency, and detailed error analysis (substitutions, insertions, deletions)
- **Professional Reporting** – Generates console summaries and detailed Markdown reports with per-file, per-model breakdowns
- **Flexible CLI** – Target specific audio files, list available samples, or skip report generation with command-line options
- **Modular Architecture** – Clean, maintainable codebase with separate modules for configuration, testing, metrics, and reporting
- **Audio Preparation Utility** – Helper script to convert and standardize audio recordings

## Project Structure

```
.
├── data/processed/           # Audio samples and reference transcripts
├── reports/                  # Generated benchmark reports
├── scripts/
│   └── convert_audio.sh      # Audio file conversion utility
├── src/                      # Source code (modular architecture)
│   ├── config.py             # Configuration and environment setup
│   ├── test_discovery.py     # Test case discovery and filtering
│   ├── transcription.py      # API communication layer
│   ├── metrics.py            # WER calculation and error analysis
│   ├── reporting.py          # Results display and report generation
│   ├── runner.py             # Test orchestration
│   ├── main.py               # Main entry point with CLI
│   └── test_models.py        # Legacy entry point (backward compatible)
├── .env.example              # Environment variables template
├── pyproject.toml            # Project dependencies and metadata
├── ARCHITECTURE.md           # Detailed architecture documentation
└── README.md                 # This file
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
   AUDIO_DATA_DIR=data/processed  # Optional: defaults to data/processed
   ```

4. **Prepare your dataset:**
   ```
   data/processed/
   ├── audio_01_clean.wav
   ├── audio_01_reference.txt
   ├── audio_02_technical.wav
   ├── audio_02_reference.txt
   └── ...
   ```

   Each `audio_*.wav` file must have a corresponding `*_reference.txt` file with the ground truth transcript.

## Usage

### Basic Commands

**Run all benchmarks:**
```bash
python src/main.py
```

**List available test cases:**
```bash
python src/main.py --list
```

**Test specific audio files:**
```bash
python src/main.py --audio audio_01_clean audio_05_safety
```

**Skip report generation:**
```bash
python src/main.py --skip-report
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
📊 BENCHMARK RESULTS
============================================================

Model                Avg WER      Norm WER     Avg Latency
------------------------------------------------------------
gpt-audio             12.45%        10.23%        2.34s
gpt-audio-mini        15.67%        13.12%        1.89s
gpt-4o-audio-preview   9.23%         7.45%        3.12s

🏆 WINNER: gpt-4o-audio-preview (Lowest WER)
```

**Markdown Report:**
A detailed report is generated at `reports/stt_report_normalized.md` containing:
- Per-file, per-model transcription results
- Word Error Rate (raw and normalized)
- Detailed error analysis (substitutions, insertions, deletions)
- Latency measurements
- Side-by-side comparison of reference vs. transcribed text

## Advanced Usage

### Adding New Models

Edit [src/config.py](src/config.py) to add model configurations:

```python
MODELS = {
    "your-new-model": {
        "url": f"{AZURE_ENDPOINT}/openai/deployments/your-model/...",
        "deployment": "your-model",
        "type": "chat",
        "api_version": "2025-01-01-preview",
    }
}

ACTIVE_MODELS = [
    "gpt-audio",
    "gpt-audio-mini",
    "your-new-model",  # Add here
]
```

### Using as a Library

Import and use individual modules in your own scripts:

```python
from src.config import ACTIVE_MODELS
from src.test_discovery import discover_test_cases
from src.runner import test_all_models
from src.reporting import print_results

# Discover test cases
cases = discover_test_cases()

# Run benchmarks
all_results = []
for audio_path, ref_path in cases:
    reference = ref_path.read_text().strip()
    results = test_all_models(audio_path, reference)
    all_results.append(results)

# Display results
print_results(all_results)
```

### Custom Metrics

Add new metric calculations in [src/metrics.py](src/metrics.py):

```python
def calculate_custom_metric(reference: str, hypothesis: str) -> float:
    """Your custom metric calculation."""
    # Implementation here
    return score
```

## Audio Preparation

Convert `.m4a` recordings to standardized WAV format:

```bash
bash scripts/convert_audio.sh
```

This script:
- Converts audio to 16 kHz mono WAV format
- Assigns consistent naming patterns
- Outputs to `test_audio/` for review
- Ready for moving to `data/processed/`

## Architecture

The project uses a modular architecture for maintainability and extensibility:

- **config.py** – Centralized configuration, environment variables, and model definitions
- **test_discovery.py** – Discovers and filters audio/transcript pairs
- **transcription.py** – Handles all API communication with Azure OpenAI
- **metrics.py** – Calculates WER and analyzes transcription errors
- **reporting.py** – Generates console output and detailed Markdown reports
- **runner.py** – Orchestrates test execution across multiple models
- **main.py** – Entry point with argument parsing and workflow coordination

For detailed architecture documentation, see [ARCHITECTURE.md](ARCHITECTURE.md).

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `AZURE_API_KEY` | Yes | – | Your Azure OpenAI API key |
| `AZURE_ENDPOINT` | No | `https://draftspeechtotext...` | Azure OpenAI endpoint URL |
| `AUDIO_DATA_DIR` | No | `data/processed` | Directory containing audio files and transcripts |

### Model Configuration

Models are configured in [src/config.py](src/config.py). Each model requires:
- Deployment name
- API endpoint URL
- API version
- Model type (whisper or chat)

## Metrics & Analysis

### Word Error Rate (WER)

The primary metric for transcription quality:
```
WER = (Substitutions + Insertions + Deletions) / Total Reference Words
```

Both raw and normalized (case-insensitive) WER are calculated.

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
Verify the `AUDIO_DATA_DIR` path exists and contains audio files.

### "Reference file missing"
Each `audio_*.wav` file must have a corresponding `*_reference.txt` file with the same base name.

### Import Errors
Activate your virtual environment:
```bash
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
```

## Limitations & Notes

- **GPT Realtime** – Not currently supported (requires websocket session)
- **Text Normalization** – Only lowercases text; punctuation, numbers, and accents are preserved
- **Audio Length** – Ensure audio files comply with Azure request size limits
- **Rate Limiting** – 1-second delay between API calls to avoid rate limits (configurable in [src/config.py](src/config.py))

## Contributing

The modular architecture makes contributions straightforward:
- Bug fixes: Target the specific module
- New features: Extend relevant modules
- New models: Update configuration
- New metrics: Extend metrics module

## Documentation

- **[ARCHITECTURE.md](ARCHITECTURE.md)** – Detailed module descriptions and design principles
- **[REFACTORING_SUMMARY.md](REFACTORING_SUMMARY.md)** – Architecture benefits and usage examples
- **[MODULE_DEPENDENCIES.md](MODULE_DEPENDENCIES.md)** – Dependency graph and data flow diagrams

## License

This project is provided as-is for benchmarking and evaluation purposes.

---

**Questions or feedback?** Please refer to the architecture documentation or open an issue.

Happy benchmarking! 🎤📊
