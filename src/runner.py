"""
Test runner module.
Orchestrates the execution of transcription tests across multiple models.
Supports both evaluation mode (with reference) and transcription-only mode.
"""

import time
from pathlib import Path
from typing import List, Dict, Any, Optional

from config import ACTIVE_MODELS, RATE_LIMIT_DELAY
from transcription import test_gpt_audio
from metrics import calculate_wer, summarize_errors, add_normalized_metrics


def test_all_models(audio_path: Path, reference_text: Optional[str]) -> List[Dict[str, Any]]:
    """
    Test all active models on a single audio file.

    If reference_text is provided, calculates WER and other evaluation metrics.
    If reference_text is None, only performs transcription.

    Args:
        audio_path: Path to audio file
        reference_text: Ground truth transcript (None for transcription-only mode)

    Returns:
        List of result dictionaries, one per model tested
    """
    print(f"\n{'='*60}")
    print(f"Testing: {audio_path}")
    if reference_text:
        print(f"Reference: {reference_text[:100]}...")
    else:
        print("Mode: Transcription only (no reference)")
    print('='*60)

    results = []

    for model in ACTIVE_MODELS:
        # Run transcription test
        result = test_gpt_audio(audio_path, model)

        # Add metrics if successful and we have a reference
        if result["success"] and reference_text:
            # Calculate basic WER and errors
            result["wer"] = calculate_wer(reference_text, result["transcript"])
            result["errors"], result["error_details"] = summarize_errors(
                reference_text,
                result["transcript"]
            )

            # Add normalized metrics
            result = add_normalized_metrics(result, reference_text)
        elif result["success"]:
            # Transcription-only mode - no metrics
            result["wer"] = None
            result["errors"] = None
            result["error_details"] = None

        results.append(result)

        # Rate limiting
        time.sleep(RATE_LIMIT_DELAY)

    return results
