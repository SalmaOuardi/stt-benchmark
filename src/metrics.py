"""
Metrics calculation module.
Handles Word Error Rate (WER) calculation and error analysis.
"""

from difflib import SequenceMatcher
from typing import Dict, List, Tuple

from jiwer import wer


def normalize_text(text: str) -> str:
    """
    Normalize text for comparison.

    Args:
        text: Input text

    Returns:
        Lowercase version of the text
    """
    return text.lower()


def calculate_wer(reference: str, hypothesis: str) -> float:
    """
    Calculate Word Error Rate between reference and hypothesis.

    Args:
        reference: Ground truth transcript
        hypothesis: Model-generated transcript

    Returns:
        WER as a percentage (0-100)
    """
    return wer(reference, hypothesis) * 100


def summarize_errors(
    reference: str,
    hypothesis: str
) -> Tuple[Dict[str, int], List[Dict[str, str]]]:
    """
    Analyze and summarize token-level errors between reference and hypothesis.

    Args:
        reference: Ground truth transcript
        hypothesis: Model-generated transcript

    Returns:
        Tuple containing:
        - summary: Dictionary with counts of substitutions, insertions, deletions
        - details: List of dictionaries describing each error
    """
    ref_tokens = reference.split()
    hyp_tokens = hypothesis.split()

    matcher = SequenceMatcher(None, ref_tokens, hyp_tokens)
    summary = {"substitutions": 0, "insertions": 0, "deletions": 0}
    details = []

    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue

        ref_segment = " ".join(ref_tokens[i1:i2])
        hyp_segment = " ".join(hyp_tokens[j1:j2])

        if tag == "replace":
            summary["substitutions"] += max(i2 - i1, j2 - j1)
        elif tag == "delete":
            summary["deletions"] += (i2 - i1)
        elif tag == "insert":
            summary["insertions"] += (j2 - j1)

        details.append({
            "type": tag,
            "expected": ref_segment,
            "actual": hyp_segment
        })

    return summary, details


def add_normalized_metrics(result: Dict, reference_text: str) -> Dict:
    """
    Add normalized WER and error metrics to a result dictionary.

    Args:
        result: Result dictionary from transcription test
        reference_text: Original reference text

    Returns:
        Updated result dictionary with normalized metrics
    """
    if not result.get("success"):
        return result

    normalized_reference = normalize_text(reference_text)
    normalized_transcript = normalize_text(result["transcript"])

    result["normalized_reference"] = normalized_reference
    result["normalized_transcript"] = normalized_transcript
    result["normalized_wer"] = calculate_wer(normalized_reference, normalized_transcript)

    normalized_errors, normalized_error_details = summarize_errors(
        normalized_reference,
        normalized_transcript
    )

    result["normalized_errors"] = normalized_errors
    result["normalized_error_details"] = normalized_error_details

    return result
