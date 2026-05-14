---
mode: agent
description: Resume ENEL445 case study work from the last captured checkpoint. Reads SESSION_STATE.md then continues safely.
---

# Continue from Checkpoint — ENEL445 Case Studies

## Step 1 — Read the state file

Read `D:\github\ENEL445\SESSION_STATE.md` in full before doing anything else.

If `SESSION_STATE.md` does not exist, look for `AGENT_HANDOFF.md` in the workspace root as a fallback. If neither exists, tell the user and stop — do not proceed blind.

## Step 2 — Orient

From the state file, extract:
- The **pending tasks** in order (smallest first)
- The **preserved assumptions** (do not violate these)
- The **do-not-scan** list (respect it — do not load those directories)

## Step 3 — Confirm before acting

State back to the user in one short paragraph:
- What the next task is
- What files will be touched
- What the expected output is

Wait for user confirmation before starting work.

## Step 4 — Execute

Proceed with only the **next smallest safe step** from the state file. Do not batch multiple tasks. Mark each task done before moving to the next.

After completing a task:
- Verify the output (check file exists, check compile succeeded, etc.)
- Update the user
- Ask whether to continue to the next task or stop

## Scan discipline

- Do **not** recursively scan `archive/`, `_unzipped/`, or `results/pdf/`
- Do **not** use `semantic_search` speculatively — use `grep_search` with `includePattern` scoped to the specific file
- Do **not** read entire notebooks at once — `grep_search` first, then `read_file` on a narrow range
- Key source files (from last checkpoint):
  - `python/linear_run.ipynb` (CS1 reference)
  - `python/hierarchical_linear_run.ipynb` (CS4)
  - `python/hierarchical_logistic_run.ipynb` (CS5)
  - `report/20260514A-LINEAR-CASE-STUDY.tex`
  - `report/20260514A-HIERARCHICAL-LINEAR-CASE-STUDY.tex`
  - `report/20260514A-HIERARCHICAL-LOGISTIC-CASE-STUDY.tex`
  - `figs/` (verify outputs only)

## Compile rules (always)

- LaTeX: `python scripts/archive_tex.py report/<file>.tex` — never compile directly
- Python notebooks: `python scripts/archive_py.py python/<file>.py`
- Pre-compile check: every `.tex` must have `\mymarginlabel` and `\hypersetup` with `\jobname`
- Do **not** git commit or push unless the user explicitly asks
