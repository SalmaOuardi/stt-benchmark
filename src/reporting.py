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

    Args:
        all_results: List of result lists, one per test case
    """
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
    if stats:
        winner = min(stats.items(), key=lambda x: sum(x[1]["wers"])/len(x[1]["wers"]))
        print(f"\n🏆 WINNER: {winner[0]} (Lowest WER)")


def generate_report(
    test_cases: List[Dict[str, Any]],
    all_results: List[List[Dict[str, Any]]],
    output_path: str = "reports/stt_report.md"
) -> None:
    """
    Create a detailed markdown report comparing transcripts to ground truth.

    Args:
        test_cases: List of test case dictionaries with audio/reference paths
        all_results: List of result lists, one per test case
        output_path: Path where the markdown report should be written
    """
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

            # Generate error summary if not present
            if summary is None or details is None:
                summary, details = summarize_errors(reference_text, transcript_text)

            lines.append(f"- Status: ✅ Success")
            lines.append(f"- Latency: {latency:.2f}s")
            lines.append(f"- Word Error Rate: {wer_value:.2f}%")
            lines.append(f"- Transcript: {transcript_text}")
            lines.append(
                f"- Errors: substitutions={summary['substitutions']}, "
                f"insertions={summary['insertions']}, "
                f"deletions={summary['deletions']}"
            )

            # Add error details
            if details:
                lines.append("#### Error Details")
                for issue in details:
                    lines.append(
                        f"- {issue['type'].capitalize()}: "
                        f"expected \"{issue['expected']}\" | "
                        f"actual \"{issue['actual']}\""
                    )
            else:
                lines.append("- Error Details: None 🎉")

            # Add normalized metrics if available
            if normalized_reference and normalized_transcript and normalized_wer is not None:
                lines.append(f"- Normalized Word Error Rate: {normalized_wer:.2f}%")
                lines.append(f"- Normalized Reference: {normalized_reference}")
                lines.append(f"- Normalized Transcript: {normalized_transcript}")

                norm_counts = normalized_summary or {"substitutions": 0, "insertions": 0, "deletions": 0}
                lines.append(
                    f"- Normalized Errors: substitutions="
                    f"{norm_counts.get('substitutions', 0)}, "
                    f"insertions={norm_counts.get('insertions', 0)}, "
                    f"deletions={norm_counts.get('deletions', 0)}"
                )

                if normalized_details:
                    lines.append("#### Normalized Error Details")
                    for issue in normalized_details:
                        lines.append(
                            f"- {issue['type'].capitalize()}: "
                            f"expected \"{issue['expected']}\" | "
                            f"actual \"{issue['actual']}\""
                        )
                else:
                    lines.append("- Normalized Error Details: None 🎉")

            lines.append("")
        lines.append("---\n")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n📝 Detailed report written to {report_path}")
