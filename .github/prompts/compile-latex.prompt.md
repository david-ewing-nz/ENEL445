---
name: compile-latex
description: "Compile a LaTeX file via the archive runner (xelatex + Biber + pandoc HTML). Pre-checks margin label and PDF metadata."
---

Compile `${input:texPath:Path relative to project root, e.g. report/20260505C REPORT.tex}`.

## Step 1 - Pre-compile checks
Read the `.tex` file and verify:
1. It contains `\newcommand{\mymarginlabel}{David Ewing dew59@uclive.ac.nz | \DTMnow\ | \jobname.tex}`
2. It contains a `\hypersetup` block with `pdfsubject = {\jobname.tex}` and `pdfkeywords = {source: \jobname.tex}`

If either is missing or malformed, add/correct it before proceeding.

## Step 2 - Compile
Run from the project root (`d:\github\ENEL445`):
```
python scripts/archive_tex.py "${input:texPath}"
```

## Step 3 - Report
Confirm:
- Archive folder created at `archive/<timestamp>/`
- PDF copied to `results/pdf/`
- HTML copied to `results/html/`
- Any compile errors from the log
