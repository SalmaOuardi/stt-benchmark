"""Unit tests for the WER metrics module.

These cover the pure, deterministic functions (no API access required).
"""

from __future__ import annotations

import pytest

from metrics import calculate_wer, normalize_text, summarize_errors


class TestNormalizeText:
    def test_lowercases(self) -> None:
        assert normalize_text("HeLLo World") == "hello world"


class TestCalculateWER:
    def test_identical_is_zero(self) -> None:
        assert calculate_wer("the cat sat", "the cat sat") == 0.0

    def test_single_substitution(self) -> None:
        # 1 wrong word out of 6 -> ~16.67%
        wer = calculate_wer("the cat sat on the mat", "the cat sat on the hat")
        assert wer == pytest.approx(100 / 6, abs=1e-3)

    def test_returns_percentage_scale(self) -> None:
        # Completely different single word -> 100%
        assert calculate_wer("cat", "dog") == 100.0


class TestSummarizeErrors:
    def test_counts_substitution(self) -> None:
        summary, details = summarize_errors("the cat sat on the mat", "the cat sat on the hat")
        assert summary == {"substitutions": 1, "insertions": 0, "deletions": 0}
        assert details[0]["type"] == "replace"
        assert details[0]["expected"] == "mat"
        assert details[0]["actual"] == "hat"

    def test_counts_deletion(self) -> None:
        summary, _ = summarize_errors("a b c d", "a c d")
        assert summary == {"substitutions": 0, "insertions": 0, "deletions": 1}

    def test_counts_insertion(self) -> None:
        summary, _ = summarize_errors("a b c", "a b x c")
        assert summary == {"substitutions": 0, "insertions": 1, "deletions": 0}

    def test_no_errors_on_match(self) -> None:
        summary, details = summarize_errors("same text here", "same text here")
        assert summary == {"substitutions": 0, "insertions": 0, "deletions": 0}
        assert details == []
