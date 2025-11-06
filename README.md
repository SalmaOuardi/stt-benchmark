# Speech-to-Text Model Benchmark

This project benchmarks several Azure OpenAI speech models on prepared audio
samples and reports transcription accuracy and latency. It is designed as a
lightweight harness for comparing model behavior on controlled datasets while
tracking key metrics such as word error rate (WER).

## Features
- **Automated dataset discovery** – `src/test_models.py` pairs every
  `audio_*.wav` file in `data/processed/` with its matching reference transcript.
- **Multiple Azure model support** – currently benchmarks `gpt-audio`,
  `gpt-audio-mini`, and `gpt-4o-audio-preview` using shared Azure OpenAI
  credentials.
- **Detailed reporting** – generates console summaries and a Markdown report with
  per-model transcripts, raw/normalized WER, and latency for each audio file.
- **Flexible execution** – CLI options allow targeting a subset of audio files,
  listing available samples, or skipping report generation.
- **Audio preparation helper** – `scripts/convert_audio.sh` converts `.m4a`
  recordings into mono 16 kHz WAV files and assigns consistent filenames.

## Project Structure
```
.
├── data/processed/           # Audio samples and ground-truth transcripts
├── reports/                  # Generated Markdown reports
├── scripts/convert_audio.sh  # Optional utility to convert recordings
├── src/test_models.py        # Main benchmarking harness
├── .env.example              # Template for Azure OpenAI credentials
├── pyproject.toml            # Python dependencies and metadata
└── README.md
```

## Prerequisites
- Python 3.13 (the project uses `pyproject.toml`; `uv`, `pip`, or any PEP 517
  compliant tool works for installing dependencies).
- Azure OpenAI resource with the required deployments (`whisper` optional,
  `gpt-audio`, `gpt-audio-mini`, `gpt-4o-audio-preview` available).
- Audio samples stored under `data/processed/` alongside reference transcripts.

## Setup
1. Install Python dependencies:
   ```bash
   pip install -e .
   ```
   Or with `uv`:
   ```bash
   uv pip install -r pyproject.toml
   ```
2. Copy environment variables template and provide your secrets:
   ```bash
   cp .env.example .env
   ```
   Update the `.env` file with your Azure endpoint and shared API key:
   ```
   AZURE_API_KEY=your_azure_openai_api_key
   AZURE_ENDPOINT=https://<your-resource>.cognitiveservices.azure.com
   ```
3. Verify the dataset layout:
   ```
   data/processed/
   ├── audio_01_clean.wav
   ├── audio_01_reference.txt
   ├── audio_02_technical.wav
   ├── audio_02_reference.txt
   └── ...
   ```

## Running Benchmarks
From the project root, execute:
```bash
python src/test_models.py
```

Useful CLI options:
- `--list` – print all discovered audio/reference pairs and exit.
- `--audio audio_05 audio_10` – limit the run to selected samples (accepts file
  stems, filenames, or full paths).
- `--skip-report` – skip generating the Markdown report.

Execution produces:
- Console summary with average WER (raw and case-insensitive) and latency per
  model.
- Detailed report at `reports/stt_report_normalized.md` containing per-model
  transcripts, error breakdowns, and latency measurements.

## Preparing Audio Samples
If your raw recordings are `.m4a`, the helper script can standardize them:
```bash
bash scripts/convert_audio.sh
```
The script writes 16 kHz mono WAV files into `test_audio/` with consistent naming
so they can be reviewed and, if desired, moved into `data/processed/`.

## Limitations & Notes
- GPT Realtime is not currently benchmarked because it requires a persistent
  websocket session; extending the harness to cover it would involve additional
  streaming logic.
- Normalized WER only lowercases strings. Formatting differences (punctuation,
  numerals vs. words, accent marks) remain visible in the raw WER and report.
- Ensure audio files are short enough to stay within Azure request limits and
  that your account has adequate quota for the benchmark volume.

## Generating New Reports
If you update the audio dataset or transcripts, simply rerun the benchmark to
regenerate the console summary and Markdown report. Previous reports (e.g.
`reports/stt_report.md`) can be kept for historical comparison.

---

Happy benchmarking! Use the harness to iterate rapidly on prompt tweaks, model
choices, or audio preprocessing strategies and capture the results in a
repeatable format.
