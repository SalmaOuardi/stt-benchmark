# Module Dependencies & Data Flow

This document visualizes how the modules interact with each other.

## Dependency Graph

```
┌─────────────────────────────────────────────────────────────┐
│                        main.py                              │
│                    (Entry Point & CLI)                       │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌──────────────┐   ┌───────────────┐   ┌───────────────┐
│test_discovery│   │    runner     │   │   reporting   │
└──────────────┘   └───────────────┘   └───────────────┘
        │                   │                   │
        │          ┌────────┼────────┐          │
        │          ▼                 ▼          │
        │   ┌──────────────┐  ┌────────────┐   │
        │   │transcription │  │  metrics   │◄──┘
        │   └──────────────┘  └────────────┘
        │          │
        └──────────┼──────────────┐
                   ▼              │
            ┌────────────┐        │
            │   config   │◄───────┘
            └────────────┘
```

## Import Relationships

### Layer 1: Foundation (No dependencies)
- **config.py**: Configuration constants, environment variables
  - Imports: `os`, `pathlib`, `dotenv`
  - Imported by: All other modules

### Layer 2: Core Utilities (Depend on config only)
- **test_discovery.py**: Test case discovery
  - Imports: `config`
  - Imported by: `main`

- **transcription.py**: API communication
  - Imports: `config`, `requests`, `openai`
  - Imported by: `runner`

- **metrics.py**: WER calculation and error analysis
  - Imports: `jiwer`, `difflib`
  - Imported by: `runner`, `reporting`

### Layer 3: Business Logic (Depend on Layer 1 & 2)
- **runner.py**: Test orchestration
  - Imports: `config`, `transcription`, `metrics`
  - Imported by: `main`

- **reporting.py**: Results display and report generation
  - Imports: `metrics`
  - Imported by: `main`

### Layer 4: Application (Depend on everything)
- **main.py**: Entry point and CLI
  - Imports: `test_discovery`, `runner`, `reporting`
  - Imported by: `test_models` (wrapper)

## Data Flow

### 1. Test Discovery Flow
```
User Input (CLI)
      │
      ▼
┌──────────────────┐
│ main.py          │
│ - Parse CLI args │
└──────────────────┘
      │
      ▼
┌──────────────────────┐
│ test_discovery.py    │
│ - Scan for WAV files │
│ - Match references   │
│ - Filter by user     │
└──────────────────────┘
      │
      ▼
List[(audio_path, reference_path)]
```

### 2. Test Execution Flow
```
Test Cases
      │
      ▼
┌──────────────────┐
│ main.py          │
│ - Loop over cases│
└──────────────────┘
      │
      ▼
┌──────────────────┐
│ runner.py        │
│ - test_all_models│
└──────────────────┘
      │
      ├─► ┌──────────────────┐
      │   │ transcription.py │
      │   │ - Call API       │
      │   └──────────────────┘
      │           │
      │           ▼
      │   {"model", "transcript", "latency", "success"}
      │
      └─► ┌──────────────────┐
          │ metrics.py       │
          │ - Calculate WER  │
          │ - Analyze errors │
          └──────────────────┘
                  │
                  ▼
      Enhanced Result Dict with WER & errors
```

### 3. Reporting Flow
```
All Results
      │
      ├─► ┌──────────────────┐
      │   │ reporting.py     │
      │   │ - print_results  │
      │   └──────────────────┘
      │           │
      │           ▼
      │   Console Output (tables, stats)
      │
      └─► ┌──────────────────┐
          │ reporting.py     │
          │ - generate_report│
          └──────────────────┘
                  │
                  ▼
          Markdown Report File
```

## Module Responsibilities (One-Line Summary)

| Module | Responsibility |
|--------|---------------|
| config.py | "I know where things are and what to test" |
| test_discovery.py | "I find test files and match them up" |
| transcription.py | "I talk to the APIs and get transcripts" |
| metrics.py | "I measure how good the transcripts are" |
| runner.py | "I coordinate testing all models on each file" |
| reporting.py | "I show results nicely to humans" |
| main.py | "I handle CLI and put everything together" |

## Circular Dependency Prevention

The architecture prevents circular dependencies through layering:

✅ **Good**: Lower layers import from upper layers
```python
main.py → runner.py → transcription.py → config.py
```

❌ **Bad**: Would create circular dependency
```python
config.py → transcription.py  # NEVER DO THIS
```

## Adding New Features

### To add a new model:
1. **config.py**: Add model to `MODELS` dict and `ACTIVE_MODELS` list
2. Done! (The rest automatically uses it)

### To add a new metric:
1. **metrics.py**: Add calculation function
2. **runner.py**: Call the new function
3. **reporting.py**: Display the new metric

### To add a new report format:
1. **reporting.py**: Add new generation function
2. **main.py**: Add CLI flag and call new function

### To add async/parallel processing:
1. **transcription.py**: Make functions async
2. **runner.py**: Use asyncio to run in parallel
3. Rest of the code stays the same!

## Testing Strategy

Each module can be tested independently:

```python
# Test config loading
from config import AZURE_API_KEY
assert AZURE_API_KEY is not None

# Test discovery
from test_discovery import discover_test_cases
cases = discover_test_cases()
assert len(cases) > 0

# Test metrics
from metrics import calculate_wer
wer_score = calculate_wer("hello world", "hello world")
assert wer_score == 0.0

# Test runner (with mocked API)
from runner import test_all_models
# Mock the API calls and test orchestration
```

## Performance Considerations

### Current Flow (Sequential)
```
Audio 1: Model A → Model B → Model C
Audio 2: Model A → Model B → Model C
Audio 3: Model A → Model B → Model C
```

### Potential Optimization (Parallel)
```
Audio 1: Model A ┐
Audio 2: Model A ├─► All run in parallel
Audio 3: Model A ┘
```

The modular structure makes this optimization straightforward by modifying only `runner.py`.

## Summary

The modular architecture provides:
- ✅ Clear separation of concerns
- ✅ No circular dependencies
- ✅ Easy to test each component
- ✅ Simple data flow
- ✅ Extensible design
- ✅ Independent module updates
