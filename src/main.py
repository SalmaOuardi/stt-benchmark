"""
Main entry point for Speech-to-Text benchmark testing.
Provides CLI interface for running transcription tests and generating reports.
"""

import sys
import argparse
from typing import List, Dict, Any

from test_discovery import discover_test_cases, filter_test_cases
from runner import test_all_models
from reporting import print_results, generate_report


def list_test_cases() -> None:
    """Display available test cases and exit."""
    cases = discover_test_cases()
    print("Available test cases:")
    for audio_path, reference_path in cases:
        if reference_path:
            print(f"- {audio_path.name}  (reference: {reference_path.name})")
        else:
            print(f"- {audio_path.name}  (transcription only - no reference)")


def run_benchmark(audio_selections: List[str] = None, skip_report: bool = False) -> None:
    """
    Run the benchmark tests.

    Args:
        audio_selections: Optional list of specific audio files to test
        skip_report: If True, skip generating the markdown report
    """
    # Discover test cases
    cases = discover_test_cases()

    # Filter cases if selections provided
    if audio_selections:
        cases, unmatched = filter_test_cases(cases, audio_selections)

        if unmatched:
            print(f"⚠️  No matches found for selections: {', '.join(unmatched)}")

        if not cases:
            print("⚠️  No test cases remain after filtering. Exiting.")
            sys.exit(1)

    if not cases:
        print("⚠️  No test cases found")
        sys.exit(1)

    # Run tests
    all_results: List[List[Dict[str, Any]]] = []
    test_cases: List[Dict[str, Any]] = []

    for audio_path, reference_path in cases:
        # Check if we have a reference for evaluation or just transcription
        if reference_path:
            reference_text = reference_path.read_text(encoding="utf-8").strip()
        else:
            reference_text = None

        # Run tests for all models on this audio file
        results = test_all_models(audio_path, reference_text)
        all_results.append(results)

        # Store test case info for reporting
        test_cases.append({
            "audio_path": audio_path,
            "reference_path": reference_path,
            "reference_text": reference_text
        })

    # Display and save results
    if all_results:
        print_results(all_results)

        if not skip_report:
            generate_report(
                test_cases,
                all_results,
                output_path="reports/stt_report_normalized.md"
            )

    print(
        "\nℹ️  GPT Realtime testing is not automated because the realtime API "
        "requires a websocket session, which this script does not yet establish."
    )


def main() -> None:
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(
        description="Benchmark Azure speech transcription models against reference transcripts."
    )
    parser.add_argument(
        "-a",
        "--audio",
        nargs="+",
        help="Run only the specified audio files (accepts names, stems, or paths).",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available audio/reference pairs and exit.",
    )
    parser.add_argument(
        "--skip-report",
        action="store_true",
        help="Skip writing the detailed markdown report.",
    )

    args = parser.parse_args()

    # Handle --list command
    if args.list:
        list_test_cases()
        sys.exit(0)

    # Run benchmark
    run_benchmark(audio_selections=args.audio, skip_report=args.skip_report)


if __name__ == "__main__":
    main()
