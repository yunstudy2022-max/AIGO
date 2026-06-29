"""
Tests for AIGO utilities
Run with: python -m pytest tests/ -v
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from ai_tools import summarize_text, classify_issue, generate_changelog_entry, parse_pr_diff_stats


def test_summarize_basic():
    text = "This is sentence one. This is sentence two. This is sentence three. This is sentence four."
    result = summarize_text(text, max_sentences=2)
    assert result == "This is sentence one. This is sentence two."


def test_summarize_short_text():
    text = "Only one sentence here."
    result = summarize_text(text, max_sentences=3)
    assert result == "Only one sentence here."


def test_classify_bug():
    assert classify_issue("App crashes on startup", "Getting an error every time") == "bug"


def test_classify_feature():
    assert classify_issue("Add dark mode support", "Would be great to have dark mode") == "feature"


def test_classify_docs():
    assert classify_issue("Fix typo in README", "") == "docs"


def test_classify_question():
    assert classify_issue("How do I configure this?", "I want to know how to set it up") == "question"


def test_classify_other():
    assert classify_issue("Random title", "") == "other"


def test_changelog_entry():
    entry = generate_changelog_entry("Fix login bug", 42, "alice")
    assert "#42" in entry
    assert "Fix login bug" in entry
    assert "@alice" in entry


def test_diff_stats_empty():
    stats = parse_pr_diff_stats("")
    assert stats == {"files_changed": 0, "lines_added": 0, "lines_removed": 0}


def test_diff_stats_basic():
    diff = """diff --git a/foo.py b/foo.py
+added line
+another added
-removed line
"""
    stats = parse_pr_diff_stats(diff)
    assert stats["files_changed"] == 1
    assert stats["lines_added"] == 2
    assert stats["lines_removed"] == 1
