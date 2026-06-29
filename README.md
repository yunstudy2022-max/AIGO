# AIGO — AI-Powered Developer Utilities

A lightweight, zero-dependency Python toolkit that brings AI-assisted workflows to everyday open-source maintenance tasks — issue triage, changelog generation, diff analysis, and text summarization.

---

## ✨ Features

| Utility | Description |
|---|---|
| `summarize_text` | Extractive summarization of issue bodies or PR descriptions |
| `classify_issue` | Auto-label GitHub issues as `bug / feature / docs / question / other` |
| `generate_changelog_entry` | Produce formatted changelog lines from PR metadata |
| `parse_pr_diff_stats` | Count files changed, lines added/removed from a unified diff |

---

## 🚀 Quick Start

```bash
git clone https://github.com/yunstudy2022-max/AIGO.git
cd AIGO
python examples/demo.py
```

No external dependencies required — pure Python 3.8+.

---

## 📦 CLI Usage

```bash
# Summarize text
python src/ai_tools.py summarize "Long text goes here..." --sentences 2

# Classify an issue
python src/ai_tools.py classify --title "App crashes on login" --body "NullPointerException in auth handler"

# Generate a changelog entry
python src/ai_tools.py changelog --title "Fix login bug" --pr 42 --author alice
```

---

## 🧪 Running Tests

```bash
python -m pytest tests/ -v
```

---

## 🛠️ Intended Workflow Integration

This project was built to explore how AI tooling (including OpenAI Codex) can assist open-source maintainers with:

- **Automated issue triage** — classify and route incoming issues without manual review
- **AI-assisted code review** — summarize PR diffs and surface key changes
- **Changelog automation** — reduce the friction of release notes
- **Community health** — faster response times for contributors

---

## 📁 Project Structure

```
AIGO/
├── src/
│   └── ai_tools.py       # Core utilities
├── tests/
│   └── test_ai_tools.py  # Unit tests
├── examples/
│   └── demo.py           # Usage examples
├── docs/
│   └── CONTRIBUTING.md   # How to contribute
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) first.

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Maintainer

[@yunstudy2022-max](https://github.com/yunstudy2022-max) — actively maintained since 2024.
