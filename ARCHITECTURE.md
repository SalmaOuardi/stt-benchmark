# Project Architecture

This document describes the modular architecture of the Speech-to-Text Benchmark Testing Suite.

## Overview

The codebase has been refactored from a single monolithic file ([test_models_old.py](src/test_models_old.py)) into a clean, modular architecture following Python best practices.

## Module Structure

```
src/
├── __init__.py              # Package initialization
├── config.py                # Configuration and environment setup
├── test_discovery.py        # Test case discovery and filtering
├── transcription.py         # API communication layer
├── metrics.py               # WER calculation and error analysis
├── reporting.py             # Results display and report generation
├── runner.py                # Test orchestration
├── main.py                  # Main entry point with CLI
├── test_models.py           # Legacy wrapper (backward compatible)
└── test_models_old.py       # Original monolithic file (backup)
```

## Module Descriptions

### 1. `config.py` - Configuration Management
**Purpose**: Centralized configuration and environment setup

**Key Components**:
- Environment variable loading (`.env` file support)
- Azure OpenAI API configuration
- Model definitions and endpoints
- Global constants (data paths, active models, prompts)

**Exports**:
- `AZURE_API_KEY`, `AZURE_ENDPOINT`, `DATA_ROOT`
- `MODELS` - Dictionary of model configurations
- `ACTIVE_MODELS` - List of models to test
- `TRANSCRIPTION_PROMPT` - Default prompt for transcription
- `RATE_LIMIT_DELAY` - Delay between API calls

### 2. `test_discovery.py` - Test Case Management
**Purpose**: Discover and filter audio/transcript pairs

**Key Functions**:
- `discover_test_cases()` - Finds all audio files with matching reference transcripts
- `filter_test_cases()` - Filters test cases based on user selections
- `_normalize_selection_value()` - Normalizes user input for matching
- `_case_keys()` - Generates matching keys for test cases

**Benefits**:
- Flexible file matching (by name, stem, or path)
- Clear error messages for missing files
- Easy to extend for different file patterns

### 3. `transcription.py` - API Communication
**Purpose**: Handle all API interactions with Azure OpenAI models

**Key Functions**:
- `test_whisper()` - Test Whisper model via REST API
- `test_gpt_audio()` - Test GPT audio models via SDK

**Design Principles**:
- Single responsibility: Only handles API communication
- Consistent return format across all models
- Proper error handling and reporting
- Automatic audio format detection

**Return Format**:
```python
{
    "model": str,           # Model name
    "transcript": str,      # Transcribed text (if successful)
    "latency": float,       # Request latency in seconds
    "success": bool,        # Success indicator
    "error": str           # Error message (if failed)
}
```

### 4. `metrics.py` - Quality Metrics
**Purpose**: Calculate WER and analyze transcription errors

**Key Functions**:
- `normalize_text()` - Text normalization for comparison
- `calculate_wer()` - Word Error Rate calculation
- `summarize_errors()` - Detailed error analysis (substitutions, insertions, deletions)
- `add_normalized_metrics()` - Add normalized WER metrics to results

**Benefits**:
- Uses industry-standard `jiwer` library
- Detailed token-level error tracking
- Both raw and normalized metric calculation

### 5. `reporting.py` - Output and Reports
**Purpose**: Display results and generate markdown reports

**Key Functions**:
- `print_results()` - Console output with aggregated statistics
- `generate_report()` - Detailed markdown report generation

**Features**:
- Clean, tabular console output
- Winner identification (lowest WER)
- Comprehensive markdown reports with:
  - Per-file, per-model results
  - Error details and analysis
  - Both raw and normalized metrics

### 6. `runner.py` - Test Orchestration
**Purpose**: Coordinate test execution across multiple models

**Key Functions**:
- `test_all_models()` - Run all active models on a single audio file

**Responsibilities**:
- Sequential model testing
- Metric calculation for successful tests
- Rate limiting between API calls
- Progress reporting

### 7. `main.py` - Entry Point
**Purpose**: CLI interface and program coordination

**Key Functions**:
- `main()` - Parse arguments and run benchmark
- `run_benchmark()` - Main benchmark orchestration
- `list_test_cases()` - List available test cases

**CLI Arguments**:
- `-a, --audio [FILES...]` - Test specific audio files
- `--list` - List available test cases
- `--skip-report` - Skip markdown report generation

## Benefits of the New Architecture

### 1. **Maintainability**
- Each module has a single, clear responsibility
- Easy to locate and fix bugs
- Self-documenting code structure

### 2. **Testability**
- Individual modules can be unit tested independently
- Minimal dependencies between modules
- Easy to mock API calls for testing

### 3. **Extensibility**
- New models: Add to `config.py` and `ACTIVE_MODELS`
- New metrics: Extend `metrics.py`
- New output formats: Extend `reporting.py`
- New test discovery patterns: Modify `test_discovery.py`

### 4. **Reusability**
- Modules can be imported and used in other projects
- Functions are well-documented and have clear interfaces
- Configuration is centralized and easy to modify

### 5. **Debugging**
- Smaller files are easier to navigate
- Clear separation of concerns helps isolate issues
- Better error messages with proper context

### 6. **Performance**
- No change in runtime performance
- Easier to optimize individual components
- Clear data flow makes bottlenecks easier to identify

## Backward Compatibility

The original `test_models.py` file is now a thin wrapper that imports and runs the new modular code. All existing scripts and workflows continue to work without modification:

```bash
# Both of these work identically:
python src/test_models.py --list
python src/main.py --list
```

## Migration Guide

If you have scripts that import from `test_models.py`, update them as follows:

**Old**:
```python
from test_models import discover_test_cases, calculate_wer
```

**New**:
```python
from test_discovery import discover_test_cases
from metrics import calculate_wer
```

## Future Enhancements

The new architecture makes these future improvements straightforward:

1. **Async API calls**: Modify `transcription.py` to use async/await
2. **Database storage**: Add a new `storage.py` module
3. **Web interface**: Import modules into a Flask/FastAPI app
4. **Additional models**: Add configurations to `config.py`
5. **Custom metrics**: Extend `metrics.py` with new calculation functions
6. **Parallel testing**: Modify `runner.py` to use multiprocessing
7. **Plugin system**: Load custom models/metrics from external files

## Best Practices Applied

1. **PEP 8**: Code follows Python style guidelines
2. **Type hints**: All functions have proper type annotations
3. **Docstrings**: Comprehensive documentation for all modules and functions
4. **DRY**: No code duplication across modules
5. **SOLID principles**: Especially Single Responsibility Principle
6. **Error handling**: Proper exceptions and user-friendly error messages
7. **Configuration**: Externalized via environment variables and constants

## Testing the Refactored Code

Run the test suite:
```bash
# Activate virtual environment
source .venv/bin/activate

# List available tests
python src/main.py --list

# Run all tests
python src/main.py

# Run specific test
python src/main.py -a audio_01_clean.wav

# Run without generating report
python src/main.py --skip-report
```

## Questions or Issues?

If you encounter any problems with the refactored code:
1. Check that all dependencies are installed
2. Verify environment variables are set correctly
3. Ensure the virtual environment is activated
4. Review module docstrings for usage examples
