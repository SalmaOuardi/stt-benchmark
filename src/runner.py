"""
Test runner module.
Orchestrates the execution of transcription tests across multiple models.
"""

import time
from pathlib import Path
from typing import List, Dict, Any

from config import ACTIVE_MODELS, RATE_LIMIT_DELAY
from transcription import test_gpt_audio
from metrics import calculate_wer, summarize_errors, add_normalized_metrics


def test_all_models(audio_path: Path, reference_text: str) -> List[Dict[str, Any]]:
    """
    Test all active models on a single audio file and capture evaluation metrics.

    Args:
        audio_path: Path to audio file
        reference_text: Ground truth transcript

    Returns:
        List of result dictionaries, one per model tested
    """
    print(f"\n{'='*60}")
    print(f"Testing: {audio_path}")
    print(f"Reference: {reference_text[:100]}...")
    print('='*60)

    results = []

    for model in ACTIVE_MODELS:
        # Run transcription test
        result = test_gpt_audio(audio_path, model)

        # Add metrics if successful
        if result["success"]:
            # Calculate basic WER and errors
            result["wer"] = calculate_wer(reference_text, result["transcript"])
            result["errors"], result["error_details"] = summarize_errors(
                reference_text,
                result["transcript"]
            )

            # Add normalized metrics
            result = add_normalized_metrics(result, reference_text)

        results.append(result)

        # Rate limiting
        time.sleep(RATE_LIMIT_DELAY)

    return results
