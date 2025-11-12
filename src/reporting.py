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
    print(f"\n{'='*80}")
    print("📊 BENCHMARK RESULTS - MODEL COMPARISON")
    print('='*80)

    # Aggregate stats
    stats = {}
    has_wer_data = False

    for results in all_results:
        for r in results:
            model = r["model"]
            if model not in stats:
                stats[model] = {
                    "wers": [],
                    "latencies": [],
                    "errors": {"substitutions": 0, "insertions": 0, "deletions": 0},
                    "success": 0,
                    "failed": 0
                }

            if not r["success"]:
                stats[model]["failed"] += 1
                continue

            stats[model]["success"] += 1

            # Only add WER if available (not None)
            if r.get("wer") is not None:
                stats[model]["wers"].append(r["wer"])
                has_wer_data = True

                errors = r.get("errors", {})
                stats[model]["errors"]["substitutions"] += errors.get("substitutions", 0)
                stats[model]["errors"]["insertions"] += errors.get("insertions", 0)
                stats[model]["errors"]["deletions"] += errors.get("deletions", 0)

            stats[model]["latencies"].append(r["latency"])

    # Print comprehensive table
    if has_wer_data:
        print(f"\n{'Model':<25} {'Avg WER':<10} {'Latency':<12} {'Errors':<10} {'Status':<10}")
        print('-'*80)

        # Sort by WER
        sorted_models = sorted(stats.items(), key=lambda x: sum(x[1]["wers"])/len(x[1]["wers"]) if x[1]["wers"] else float('inf'))

        for model, data in sorted_models:
            if data["wers"]:
                avg_wer = sum(data["wers"]) / len(data["wers"])
                wer_display = f"{avg_wer:.2f}%"
            else:
                wer_display = "n/a"

            avg_lat = sum(data["latencies"]) / len(data["latencies"]) if data["latencies"] else 0
            total_errors = sum(data["errors"].values())
            status = f"✅ {data['success']}" if data["failed"] == 0 else f"⚠️ {data['success']}/{data['success']+data['failed']}"

            print(f"{model:<25} {wer_display:<10} {avg_lat:>6.2f}s    {total_errors:<10} {status:<10}")

        # Find winner (only if we have WER data)
        models_with_wer = {m: d for m, d in stats.items() if d["wers"]}
        if models_with_wer:
            winner_model, winner_data = min(models_with_wer.items(), key=lambda x: sum(x[1]["wers"])/len(x[1]["wers"]))
            winner_wer = sum(winner_data["wers"]) / len(winner_data["wers"])
            print(f"\n{'='*80}")
            print(f"🏆 BEST MODEL: {winner_model}")
            print(f"   Average WER: {winner_wer:.2f}%")
            print(f"   Average Latency: {sum(winner_data['latencies'])/len(winner_data['latencies']):.2f}s")
            print(f"   Total Errors: {sum(winner_data['errors'].values())}")
            print('='*80)

        print("\nℹ️  WER calculated without normalization (raw comparison)")
    else:
        # Transcription-only mode
        print(f"\n{'Model':<30} {'Avg Latency':<15}")
        print('-'*60)

        for model, data in sorted(stats.items()):
            avg_lat = sum(data["latencies"]) / len(data["latencies"]) if data["latencies"] else 0
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
    """Generate comprehensive benchmark evaluation report with WER metrics."""
    report_path = Path(output_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# Speech-to-Text Model Benchmark Report")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(f"**Test Configuration:**")
    lines.append(f"- Number of audio samples: {len(test_cases)}")
    lines.append(f"- Evaluation metric: Word Error Rate (WER)")
    lines.append(f"- Normalization: Disabled (raw WER calculation)")
    lines.append("")

    # Calculate aggregate statistics
    model_stats = {}
    for results in all_results:
        for r in results:
            if not r["success"]:
                continue
            model = r["model"]
            if model not in model_stats:
                model_stats[model] = {
                    "wers": [],
                    "latencies": [],
                    "total_errors": {"substitutions": 0, "insertions": 0, "deletions": 0},
                    "success_count": 0
                }

            model_stats[model]["wers"].append(r.get("wer", 0))
            model_stats[model]["latencies"].append(r.get("latency", 0))
            model_stats[model]["success_count"] += 1

            errors = r.get("errors", {})
            model_stats[model]["total_errors"]["substitutions"] += errors.get("substitutions", 0)
            model_stats[model]["total_errors"]["insertions"] += errors.get("insertions", 0)
            model_stats[model]["total_errors"]["deletions"] += errors.get("deletions", 0)

    # Overall comparison table
    lines.append("### Model Performance Comparison")
    lines.append("")
    lines.append("| Model | Avg WER | Min WER | Max WER | Avg Latency | Total Errors | Status |")
    lines.append("|-------|---------|---------|---------|-------------|--------------|--------|")

    sorted_models = sorted(model_stats.items(), key=lambda x: sum(x[1]["wers"])/len(x[1]["wers"]) if x[1]["wers"] else float('inf'))

    for model, stats in sorted_models:
        if stats["wers"]:
            avg_wer = sum(stats["wers"]) / len(stats["wers"])
            min_wer = min(stats["wers"])
            max_wer = max(stats["wers"])
        else:
            avg_wer = min_wer = max_wer = 0

        avg_latency = sum(stats["latencies"]) / len(stats["latencies"])
        total_errors = sum(stats["total_errors"].values())
        status = "✅" if stats["success_count"] == len(test_cases) else "⚠️"

        lines.append(f"| {model} | {avg_wer:.2f}% | {min_wer:.2f}% | {max_wer:.2f}% | {avg_latency:.2f}s | {total_errors} | {status} |")

    lines.append("")

    # Winner announcement
    if sorted_models:
        winner_model, winner_stats = sorted_models[0]
        winner_avg_wer = sum(winner_stats["wers"]) / len(winner_stats["wers"])
        lines.append(f"### 🏆 Best Model: **{winner_model}**")
        lines.append(f"- Average WER: **{winner_avg_wer:.2f}%**")
        lines.append(f"- Average Latency: **{sum(winner_stats['latencies'])/len(winner_stats['latencies']):.2f}s**")
        lines.append(f"- Total Errors: **{sum(winner_stats['total_errors'].values())}**")
        lines.append("")

    # Detailed error breakdown
    lines.append("### Error Type Breakdown")
    lines.append("")
    lines.append("| Model | Substitutions | Insertions | Deletions | Total |")
    lines.append("|-------|---------------|------------|-----------|-------|")

    for model, stats in sorted_models:
        errors = stats["total_errors"]
        total = sum(errors.values())
        lines.append(f"| {model} | {errors['substitutions']} | {errors['insertions']} | {errors['deletions']} | {total} |")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Detailed Results by Audio Sample")
    lines.append("")

    for (case, results) in zip(test_cases, all_results):
        audio_path = case["audio_path"]
        reference_path = case["reference_path"]
        reference_text = case["reference_text"]

        lines.append(f"### Audio Sample: {audio_path.name}")
        lines.append("")
        lines.append(f"**Reference Text:**")
        lines.append(f"> {reference_text}")
        lines.append("")
        lines.append(f"**File Paths:**")
        lines.append(f"- Audio: `{audio_path}`")
        lines.append(f"- Reference: `{reference_path}`")
        lines.append("")

        # Performance table for this audio
        lines.append("**Model Performance:**")
        lines.append("")
        lines.append("| Model | WER | Latency | Sub | Ins | Del | Status |")
        lines.append("|-------|-----|---------|-----|-----|-----|--------|")

        for result in results:
            model_name = result["model"]

            if not result["success"]:
                lines.append(f"| {model_name} | - | - | - | - | - | ❌ Failed |")
            else:
                wer_value = result.get("wer", 0)
                latency = result.get("latency", 0)
                errors = result.get("errors", {})
                sub = errors.get("substitutions", 0)
                ins = errors.get("insertions", 0)
                dels = errors.get("deletions", 0)

                lines.append(f"| {model_name} | {wer_value:.2f}% | {latency:.2f}s | {sub} | {ins} | {dels} | ✅ |")

        lines.append("")

        # Detailed transcripts and error analysis
        lines.append("**Detailed Transcripts:**")
        lines.append("")

        for result in results:
            model_name = result["model"]
            lines.append(f"#### {model_name}")

            if not result["success"]:
                lines.append(f"❌ **Error:** `{result['error']}`")
                lines.append("")
                continue

            transcript_text = result["transcript"]
            details = result.get("error_details", [])

            lines.append(f"**Transcript:**")
            lines.append(f"```")
            lines.append(transcript_text)
            lines.append(f"```")
            lines.append("")

            # Error details
            if details:
                lines.append(f"**Error Analysis ({len(details)} errors):**")
                for issue in details:
                    lines.append(
                        f"- **{issue['type'].capitalize()}:** "
                        f"Expected `{issue['expected']}` → Got `{issue['actual']}`"
                    )
                lines.append("")
            else:
                lines.append("✅ **Perfect match - No errors!**")
                lines.append("")

        lines.append("---")
        lines.append("")

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
