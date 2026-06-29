"""
Example: How to use AIGO utilities in your own workflow
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from ai_tools import summarize_text, classify_issue, generate_changelog_entry, parse_pr_diff_stats

# --- Summarize an issue body ---
issue_body = """
We discovered that the login endpoint returns a 500 error when the user submits
an empty password field. This happens consistently across all browsers. The error
appears in the logs as a NullPointerException. Users are unable to recover without
refreshing and re-entering their credentials. We need to add proper validation.
"""
print("=== Issue Summary ===")
print(summarize_text(issue_body, max_sentences=2))
print()

# --- Classify an issue ---
title = "App crashes when uploading large files"
body = "Getting a memory error when the file is over 100MB"
label = classify_issue(title, body)
print(f"=== Issue Classification ===")
print(f"Label: {label}")
print()

# --- Generate changelog entry ---
print("=== Changelog Entry ===")
entry = generate_changelog_entry("Fix null pointer in login handler", 87, "yunstudy2022-max")
print(entry)
print()

# --- Parse diff stats ---
sample_diff = """diff --git a/src/auth.py b/src/auth.py
index abc123..def456 100644
--- a/src/auth.py
+++ b/src/auth.py
+    if not password:
+        raise ValueError("Password cannot be empty")
-    return authenticate(user, password)
+    return authenticate(user, password.strip())
diff --git a/tests/test_auth.py b/tests/test_auth.py
+def test_empty_password():
+    with pytest.raises(ValueError):
+        login("user", "")
"""
stats = parse_pr_diff_stats(sample_diff)
print("=== PR Diff Stats ===")
print(f"Files changed : {stats['files_changed']}")
print(f"Lines added   : {stats['lines_added']}")
print(f"Lines removed : {stats['lines_removed']}")
