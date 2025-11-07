"""
Test case discovery and filtering module.
Handles pairing audio files with reference transcripts and filtering based on user selections.
Supports both evaluation mode (with references) and transcription-only mode (without references).
"""

from pathlib import Path
from typing import List, Tuple, Set, Optional

from config import DATA_ROOT


def discover_test_cases() -> List[Tuple[Path, Optional[Path]]]:
    """
    Pair each WAV file with its matching reference transcript, if available.

    Audio files without reference transcripts will be included for transcription-only mode.
    Searches both in DATA_ROOT and its subdirectories.

    Returns:
        List of tuples containing (audio_path, reference_path or None)

    Raises:
        FileNotFoundError: If the DATA_ROOT directory doesn't exist
    """
    if not DATA_ROOT.exists():
        raise FileNotFoundError(f"Audio data directory not found: {DATA_ROOT}")

    cases = []

    # Find all .wav files in DATA_ROOT and subdirectories
    for audio_path in sorted(DATA_ROOT.rglob("*.wav")):
        # Check if it matches the audio_XX pattern
        if audio_path.stem.startswith("audio_"):
            parts = audio_path.stem.split("_")
            if len(parts) < 2:
                print(f"⚠️  Skipping unexpected file name: {audio_path.name}")
                continue

            base_name = "_".join(parts[:2])
            reference_path = audio_path.with_name(f"{base_name}_reference.txt")

            if not reference_path.exists():
                print(f"ℹ️  No reference for {audio_path.name} - transcription only")
                cases.append((audio_path, None))
            else:
                cases.append((audio_path, reference_path))
        else:
            # Audio file without audio_XX prefix - transcription only
            print(f"ℹ️  Found {audio_path.relative_to(DATA_ROOT)} - transcription only")
            cases.append((audio_path, None))

    return cases


def _normalize_selection_value(value: str) -> Set[str]:
    """
    Normalize a selection value into multiple possible matching tokens.

    Args:
        value: User-provided selection string

    Returns:
        Set of normalized tokens that could match this value
    """
    tokens = set()
    raw = value.strip().lower()

    if not raw:
        return tokens

    tokens.add(raw)
    path = Path(value)
    tokens.add(path.name.lower())
    tokens.add(path.stem.lower())

    parts = path.stem.lower().split("_")
    if len(parts) >= 2:
        tokens.add("_".join(parts[:2]))

    return tokens


def _case_keys(audio_path: Path, reference_path: Optional[Path]) -> Set[str]:
    """
    Generate all possible matching keys for a test case.

    Args:
        audio_path: Path to audio file
        reference_path: Path to reference transcript (or None)

    Returns:
        Set of normalized keys that could identify this test case
    """
    keys = {
        audio_path.name.lower(),
        audio_path.stem.lower(),
        str(audio_path).lower(),
    }

    if reference_path:
        keys.update({
            reference_path.name.lower(),
            reference_path.stem.lower(),
            str(reference_path).lower(),
        })

        for stem in (audio_path.stem, reference_path.stem):
            parts = stem.lower().split("_")
            if len(parts) >= 2:
                keys.add("_".join(parts[:2]))
    else:
        parts = audio_path.stem.lower().split("_")
        if len(parts) >= 2:
            keys.add("_".join(parts[:2]))

    return keys


def filter_test_cases(
    cases: List[Tuple[Path, Optional[Path]]],
    selections: List[str]
) -> Tuple[List[Tuple[Path, Optional[Path]]], List[str]]:
    """
    Filter discovered cases based on user selections.

    Args:
        cases: List of (audio_path, reference_path or None) tuples
        selections: List of user-provided selection strings

    Returns:
        Tuple of (filtered_cases, unmatched_selections)
    """
    if not selections:
        return cases, []

    selection_keys = set()
    for value in selections:
        selection_keys.update(_normalize_selection_value(value))

    filtered = []
    matched_keys = set()

    for audio_path, reference_path in cases:
        keys = _case_keys(audio_path, reference_path)
        if keys & selection_keys:
            filtered.append((audio_path, reference_path))
            matched_keys.update(keys & selection_keys)

    unmatched = sorted(selection_keys - matched_keys)
    return filtered, unmatched
