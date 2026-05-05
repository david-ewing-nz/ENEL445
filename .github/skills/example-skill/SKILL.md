---
name: example-skill
description: "Reference example of a skill. Use when asked to audit Python scripts for style issues."
---

# Example Skill: Python Style Audit

## Steps

1. Use `file_search` to find all `*.py` files under `python/`.
2. For each file, use `grep_search` to check for:
   - American English spellings in comments (`optimize`, `color`, `normalize`)
   - `os.path` usage instead of `pathlib.Path`
3. Report findings as a table: `| File | Line | Issue |`
4. Offer to apply fixes.
