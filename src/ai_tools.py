"""
AIGO - AI-powered developer utilities
A lightweight toolkit for common AI-assisted development workflows.
"""

import re
import sys
import json
import argparse
from datetime import datetime


def summarize_text(text: str, max_sentences: int = 3) -> str:
    """
    Simple extractive summarization: picks the first N sentences.
    Useful for generating quick summaries of issue descriptions or PRs.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    selected = sentences[:max_sentences]
    return " ".join(selected)


def generate_changelog_entry(pr_title: str, pr_number: int, author: str) -> str:
    """
    Generate a formatted changelog entry from PR metadata.
    """
    date = datetime.now().strftime("%Y-%m-%d")
    return f"- [{date}] #{pr_number} {pr_title} (by @{author})"


def classify_issue(title: str, body: str) -> str:
    """
    Rule-based issue classifier. Labels issues as:
    bug / feature / docs / question / other
    """
    combined = (title + " " + body).lower()
    if any(w in combined for w in ["bug", "error", "crash", "fail", "broken", "exception"]):
        return "bug"
    if any(w in combined for w in ["feature", "add", "support", "implement", "enhance", "新增", "支援"]):
        return "feature"
    if any(w in combined for w in ["doc", "readme", "typo", "spelling", "document"]):
        return "docs"
    if any(w in combined for w in ["how", "what", "why", "when", "where", "question", "如何", "怎麼"]):
        return "question"
    return "other"


def parse_pr_diff_stats(diff_text: str) -> dict:
    """
    Parse a unified diff and return basic stats:
    files changed, lines added, lines removed.
    """
    files = set()
    added = removed = 0
    for line in diff_text.splitlines():
        if line.startswith("diff --git"):
            files.add(line)
        elif line.startswith("+") and not line.startswith("+++"):
            added += 1
        elif line.startswith("-") and not line.startswith("---"):
            removed += 1
    return {
        "files_changed": len(files),
        "lines_added": added,
        "lines_removed": removed,
    }


def cli():
    parser = argparse.ArgumentParser(
        description="AIGO - AI-powered developer utilities"
    )
    sub = parser.add_subparsers(dest="command")

    # summarize
    p_sum = sub.add_parser("summarize", help="Summarize a block of text")
    p_sum.add_argument("text", help="Text to summarize")
    p_sum.add_argument("--sentences", type=int, default=3)

    # classify
    p_cls = sub.add_parser("classify", help="Classify a GitHub issue")
    p_cls.add_argument("--title", required=True)
    p_cls.add_argument("--body", default="")

    # changelog
    p_log = sub.add_parser("changelog", help="Generate changelog entry")
    p_log.add_argument("--title", required=True)
    p_log.add_argument("--pr", type=int, required=True)
    p_log.add_argument("--author", required=True)

    args = parser.parse_args()

    if args.command == "summarize":
        print(summarize_text(args.text, args.sentences))
    elif args.command == "classify":
        label = classify_issue(args.title, args.body)
        print(json.dumps({"label": label}))
    elif args.command == "changelog":
        print(generate_changelog_entry(args.title, args.pr, args.author))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    cli()
