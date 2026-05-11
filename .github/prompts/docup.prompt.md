---
name: docup
description: "Doc update: compile latest case studies and combined report, publish to docs/, update landing page, git push."
---

# #docup — Document Update

Compile the latest version of each ENEL445 document, publish the PDFs to `docs/`, update the landing page (`docs/index.html`) with fresh abstracts, and push to GitHub.

Work from the project root `d:\github\ENEL445` throughout.

---

## Step 1 — Discover latest source files

Scan `report/` for the lexicographically latest `.tex` file matching each of these six suffixes (date-letter stamp means lexicographic order = chronological order):

| Slot | Pattern (files starting with a digit) |
|------|---------------------------------------|
| combined | `*-COMBINED-REPORT.tex` |
| linear | `*-LINEAR-CASE-STUDY.tex` excluding `*HIERARCHICAL*` |
| quadratic | `*-QUADRATIC-CASE-STUDY.tex` |
| logistic | `*-LOGISTIC-CASE-STUDY.tex` excluding `*HIERARCHICAL*` |
| hier-linear | `*-HIERARCHICAL-LINEAR-CASE-STUDY.tex` |
| hier-logistic | `*-HIERARCHICAL-LOGISTIC-CASE-STUDY.tex` |

Run this PowerShell to discover and confirm all six before proceeding:
```powershell
$slots = @{
  combined      = Get-ChildItem report\*-COMBINED-REPORT.tex | Sort-Object Name | Select-Object -Last 1
  linear        = Get-ChildItem report\*-LINEAR-CASE-STUDY.tex | Where-Object { $_.Name -notmatch 'HIERARCHICAL' } | Sort-Object Name | Select-Object -Last 1
  quadratic     = Get-ChildItem report\*-QUADRATIC-CASE-STUDY.tex | Sort-Object Name | Select-Object -Last 1
  logistic      = Get-ChildItem report\*-LOGISTIC-CASE-STUDY.tex | Where-Object { $_.Name -notmatch 'HIERARCHICAL' } | Sort-Object Name | Select-Object -Last 1
  hierlinear    = Get-ChildItem report\*-HIERARCHICAL-LINEAR-CASE-STUDY.tex | Sort-Object Name | Select-Object -Last 1
  hierlogistic  = Get-ChildItem report\*-HIERARCHICAL-LOGISTIC-CASE-STUDY.tex | Sort-Object Name | Select-Object -Last 1
}
$slots.GetEnumerator() | Sort-Object Key | Format-Table Key, @{L='File';E={$_.Value.Name}}
```

Report the discovered filenames. If any slot has no match, stop and report which slot is missing.

---

## Step 2 — Pre-compile checks

For each of the six `.tex` files, verify:
1. Contains `\newcommand{\mymarginlabel}{\textcopyright\ David Ewing dew59@uclive.ac.nz | \DTMnow\ | \jobname.tex}`
2. Contains a `\hypersetup` block with `pdfsubject = {\jobname.tex}` and `pdfkeywords = {source: \jobname.tex}`

If either is missing or malformed, correct it before compiling.

---

## Step 3 — Compile all six

Run sequentially (do not parallelise — xelatex uses shared aux files):
```
python scripts/archive_tex.py report/<combined>
python scripts/archive_tex.py report/<linear>
python scripts/archive_tex.py report/<quadratic>
python scripts/archive_tex.py report/<logistic>
python scripts/archive_tex.py report/<hier-linear>
python scripts/archive_tex.py report/<hier-logistic>
```

After each compilation confirm that a PDF was produced in `results/pdf/`. If any compilation fails, stop and report the error — do not proceed to later steps.

---

## Step 4 — Clean up old PDFs in docs/

For each of the six document types, check `docs/` for existing PDFs matching that type. If two or more versions are present (e.g. `20260510A-LINEAR-CASE-STUDY.pdf` and `20260509A-LINEAR-CASE-STUDY.pdf`), delete all but the most recent one — leaving the one currently linked in `index.html` in place during GitHub Pages propagation delay. Never delete the file that is currently referenced in `index.html`.

```powershell
# Example pattern — repeat for each type
$keep = Get-ChildItem docs\*-LINEAR-CASE-STUDY.pdf | Where-Object { $_.Name -notmatch 'HIERARCHICAL' } | Sort-Object Name | Select-Object -Last 1
Get-ChildItem docs\*-LINEAR-CASE-STUDY.pdf | Where-Object { $_.Name -notmatch 'HIERARCHICAL' -and $_.Name -ne $keep.Name } | Remove-Item
```

---

## Step 5 — Copy fresh PDFs to docs/

Copy the six freshly compiled PDFs from `results/pdf/` to `docs/`:
```powershell
$slots.GetEnumerator() | ForEach-Object {
  $stem = $_.Value.BaseName
  Copy-Item "results/pdf/$stem.pdf" "docs/$stem.pdf" -Force
}
```

Confirm all six files are present in `docs/`.

---

## Step 6 — Update docs/index.html

For each of the six entries in `docs/index.html`:

**6a. Update the `href`** to the new PDF filename (stem derived from the `.tex` basename).

**6b. Update the `<p>` description** using the abstract from the `.tex` file:
- Read the text between `\begin{abstract}` and `\end{abstract}`
- Strip LaTeX markup: remove `\setlength{...}{...}`, `\setlength\...`, remove `\emph{...}` (keep inner text), remove `$...$` math delimiters (keep content), remove `\mathcal`, `\bm`, `\mathrm`, `\mathbb` wrappers (keep argument), replace `---` with `—`, replace `\approx` with `≈`, replace `\times` with `×`
- The result should be readable plain prose as an HTML paragraph
- Replace the existing `<p>...</p>` description for that entry with the new text

Do this for all six entries. The Combined Report entry uses the combined report abstract.

---

## Step 7 — Git commit and push

```powershell
cd d:\github\ENEL445
$ts = Get-Date -Format "yyyy-MM-dd HH:mm"
git add -A
git commit -m "docup: publish latest case-studies/report as of $ts"
git push
```

Confirm the push succeeded and report the commit hash.
