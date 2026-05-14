---
mode: agent
description: End-of-session capture. Run at the end of any working session to write SESSION_STATE.md in the workspace root. The output file is read by CONTINUE_FROM_CHECKPOINT.prompt.md at the start of the next session.
---

Capture the current project state and write it to `SESSION_STATE.md` in the workspace root (`D:\github\ENEL445\SESSION_STATE.md`). Overwrite any existing file.

## Instructions

Work through the steps below in order. Collect all facts before writing the file. Do NOT do broad recursive scans — use the targeted commands specified.

### Step 1 — Git state

Run:
```powershell
cd D:\github\ENEL445
git log --oneline -5
git status --short
```

Record: last 5 commits (hash + message), any uncommitted/untracked files.

### Step 2 — Recent PDFs

Run:
```powershell
Get-ChildItem D:\github\ENEL445\results\pdf\ | Sort-Object LastWriteTime -Descending | Select-Object -First 8 Name, LastWriteTime, Length
```

Record: the 8 most recently written PDFs with timestamps.

### Step 3 — Active report files

List the most recent `.tex` file in `report/` by date-letter stamp (e.g. `20260514A-*`). For each active report (CS1, CS4, CS5), record its filename and top-level section names. Use:
```
grep_search on report/<filename>.tex for pattern ^\\section
```

### Step 4 — Figures

Run:
```powershell
Get-ChildItem D:\github\ENEL445\figs\ | Sort-Object LastWriteTime -Descending | Select-Object -First 10 Name, LastWriteTime
```

Record: the 10 most recently written figures.

### Step 5 — Pending work

Search for any existing `SESSION_STATE.md` or `AGENT_HANDOFF.md` in the workspace root and extract the "Next smallest safe step" section if present. Also check your current todo list. Record all incomplete tasks.

### Step 6 — Known design decisions and preserved assumptions

Read `.github/instructions/return-context.instructions.md` for the project-level context already defined there. Do NOT re-copy it wholesale — only record decisions and assumptions that are **not already covered** by that file (i.e. session-specific state).

---

## Output format

Write `SESSION_STATE.md` with exactly this structure:

```markdown
# SESSION_STATE — ENEL445
Generated: <date and time>

## Git
Last commit: <hash> <message>
Uncommitted changes: <list or "none">

## Recent PDFs
<table: Name | LastWriteTime | Size>

## Active Reports
| Report | Filename | Sections |
|--------|----------|----------|
| CS1    | ...      | ...      |
| CS4    | ...      | ...      |
| CS5    | ...      | ...      |

## Recent Figures
<table: Name | LastWriteTime>

## Pending Tasks
<numbered list — smallest first>

## Session-Specific Design Decisions
<only decisions NOT in return-context.instructions.md>

## Preserved Assumptions
<only assumptions NOT in return-context.instructions.md>

## Do Not Scan
- archive/
- _unzipped/
- results/pdf/ (binary)
- cs4_compile.log, cs5_compile.log (temporary)
```

After writing the file, confirm: "SESSION_STATE.md written — <N> pending tasks recorded."
