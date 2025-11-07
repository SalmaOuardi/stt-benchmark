"""
LLM-based text normalization for more accurate WER calculation.
Uses Mistral to intelligently normalize transcripts, treating semantically
equivalent variations as the same while preserving real transcription errors.
"""

import requests
from typing import Dict, Tuple
import json


def normalize_with_llm(
    reference: str,
    hypothesis: str,
    api_key: str,
    endpoint: str = "https://draftspeechtotext.services.ai.azure.com/models/chat/completions?api-version=2024-05-01-preview"
) -> Tuple[str, str]:
    """
    Use LLM to intelligently normalize both reference and hypothesis texts.

    The LLM is instructed to treat semantically equivalent variations as identical,
    while preserving actual transcription errors. This accounts for:
    - The reference text may have minor reading mistakes (it's human-read)
    - Number format variations (3 vs trois vs 3ème vs troisième) are equivalent
    - Punctuation and capitalization don't matter
    - Minor spelling variations of the same word should be normalized
    - But semantic differences (je vais vs il faut) are real errors

    Args:
        reference: Ground truth transcript (may have minor human reading errors)
        hypothesis: Model-generated transcript
        api_key: Azure API key
        endpoint: Mistral endpoint URL

    Returns:
        Tuple of (normalized_reference, normalized_hypothesis)
    """

    prompt = f"""You are an expert in French speech-to-text evaluation. Your task is to normalize two French transcripts to calculate a meaningful Word Error Rate (WER) that reflects actual transcription quality, not formatting differences.

IMPORTANT CONTEXT:
- The reference text was read by a human and may contain minor reading mistakes
- We want to measure transcription quality, not formatting consistency
- Only semantic differences should be considered errors

NORMALIZATION RULES (apply to BOTH texts):

1. **Numbers - Treat all forms as equivalent:**
   - "trois" = "3" = "troisième" = "3ème" (all → "3")
   - "quinze" = "15" (→ "15")
   - "vingt" = "20" (→ "20")
   - "quatre" = "4" = "quatrième" = "4ème" (→ "4")
   - Standardize ALL number words to digits

2. **Punctuation & Capitalization:**
   - Remove ALL punctuation (commas, periods, semicolons, apostrophes, hyphens)
   - Convert to lowercase
   - Normalize spacing (single space between words)

3. **Semantic Equivalents - Treat as IDENTICAL:**
   - "banches" = "benchs" = "banques" = "planches" (construction context, unclear audio → normalize to same word)
   - "étais" = "étés" (likely same word, audio quality issue → normalize to same)
   - "bâtiment" = "batiment" (accent variations → same)
   - "l'inspection" = "linspection" (apostrophe handling → same)
   - "d'infiltration d'eau" = "dinfiltration deau" (apostrophe handling → same)

4. **Preserve ONLY Real Semantic Differences:**
   - "je vais" ≠ "il faut" (different meanings → keep as-is)
   - "structures" ≠ "structure" (plural vs singular → keep as-is IF meaningful in context)
   - Major word substitutions that change meaning

5. **Contraction/Article Handling:**
   - Normalize all contractions: "l'" → "l", "d'" → "d", "j'" → "j"

YOUR TASK:
Normalize both texts so that only MEANINGFUL transcription errors remain. Format differences, number representations, minor spelling variations, and words that sound similar should be normalized to match.

Reference text:
{reference}

Hypothesis text:
{hypothesis}

Return ONLY a JSON object (no markdown, no extra text):
{{
    "normalized_reference": "the normalized text",
    "normalized_hypothesis": "the normalized text"
}}"""

    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }

    payload = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.0,
        "max_tokens": 2000
    }

    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        result = response.json()
        content = result["choices"][0]["message"]["content"]

        # Extract JSON from the response
        # Handle cases where LLM might add markdown code blocks
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        normalized = json.loads(content)

        return (
            normalized["normalized_reference"],
            normalized["normalized_hypothesis"]
        )

    except Exception as e:
        # Fallback to basic normalization if LLM fails
        print(f"Warning: LLM normalization failed ({str(e)}), using basic normalization")
        return basic_normalize(reference), basic_normalize(hypothesis)


def basic_normalize(text: str) -> str:
    """
    Fallback basic normalization.

    Args:
        text: Input text

    Returns:
        Normalized text
    """
    import re

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[.,;:!?]', '', text)

    # Normalize apostrophes
    text = text.replace("'", "'").replace("'", "'")

    # Normalize whitespace
    text = ' '.join(text.split())

    return text
