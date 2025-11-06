"""
Legacy entry point for backward compatibility.
This file now acts as a wrapper around the modularized codebase.

For the new modular structure, see:
- config.py: Configuration and environment setup
- test_discovery.py: Test case discovery and filtering
- transcription.py: API communication and transcription
- metrics.py: WER calculation and error analysis
- reporting.py: Console output and report generation
- runner.py: Test orchestration
- main.py: Main entry point with CLI

To run the benchmark, you can now use:
    python src/main.py
or continue using:
    python src/test_models.py
"""

# Import and run from the new modular structure
from main import main

if __name__ == "__main__":
    main()
