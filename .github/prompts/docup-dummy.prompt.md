---
name: docup-dummy
description: "Regenerate and republish all DUMMY awaiting-review PDFs (title + abstract + black review box, no body content)."
---

# #docup-dummy — Regenerate DUMMY Review Copies

Recompile and republish all six DUMMY case study PDFs. Each DUMMY document contains only the title, abstract, and a full-width black "Awaiting review by Professor Le Yang" box — no body content.

Work from the project root `d:\github\ENEL445` throughout.

---

## Step 1 — Verify DUMMY source files exist

Confirm all six files are present in `report/`:

```powershell
Get-ChildItem d:\github\ENEL445\report\DUMMY-*.tex | Select-Object Name
```

Expected:
- `DUMMY-COMBINED-REPORT.tex`
- `DUMMY-LINEAR-CASE-STUDY.tex`
- `DUMMY-QUADRATIC-CASE-STUDY.tex`
- `DUMMY-LOGISTIC-CASE-STUDY.tex`
- `DUMMY-HIERARCHICAL-LINEAR-CASE-STUDY.tex`
- `DUMMY-HIERARCHICAL-LOGISTIC-CASE-STUDY.tex`

If any are missing, stop and report which ones are absent.

---

## Step 2 — (Optional) Sync abstracts from latest source

If the corresponding real case study has been updated since the DUMMY was last compiled, read the `\begin{abstract}...\end{abstract}` block from the latest real source and replace it in the DUMMY file before compiling.

Real source discovery (same as `#docup` Step 1):
- LINEAR: latest `report/*-LINEAR-CASE-STUDY.tex` excluding `HIERARCHICAL` and `DUMMY`
- QUADRATIC: latest `report/*-QUADRATIC-CASE-STUDY.tex` excluding `DUMMY`
- LOGISTIC: latest `report/*-LOGISTIC-CASE-STUDY.tex` excluding `HIERARCHICAL` and `DUMMY`
- HIER-LINEAR: latest `report/*-HIERARCHICAL-LINEAR-CASE-STUDY.tex` excluding `DUMMY`
- HIER-LOGISTIC: latest `report/*-HIERARCHICAL-LOGISTIC-CASE-STUDY.tex` excluding `DUMMY`
- COMBINED: latest `report/*-COMBINED-REPORT.tex` excluding `DUMMY`

Skip this step if the abstracts have not changed.

---

## Step 3 — Compile all six DUMMY files

Run sequentially from `d:\github\ENEL445`:

```
python scripts/archive_tex.py report/DUMMY-LINEAR-CASE-STUDY.tex
python scripts/archive_tex.py report/DUMMY-QUADRATIC-CASE-STUDY.tex
python scripts/archive_tex.py report/DUMMY-LOGISTIC-CASE-STUDY.tex
python scripts/archive_tex.py report/DUMMY-HIERARCHICAL-LINEAR-CASE-STUDY.tex
python scripts/archive_tex.py report/DUMMY-HIERARCHICAL-LOGISTIC-CASE-STUDY.tex
python scripts/archive_tex.py report/DUMMY-COMBINED-REPORT.tex
```

After each, verify the PDF was produced in `results/pdf/`. If any fails, stop and report the error.

---

## Step 4 — Copy fresh PDFs to docs/

```powershell
foreach ($stem in @('DUMMY-LINEAR-CASE-STUDY','DUMMY-QUADRATIC-CASE-STUDY',
  'DUMMY-LOGISTIC-CASE-STUDY','DUMMY-HIERARCHICAL-LINEAR-CASE-STUDY',
  'DUMMY-HIERARCHICAL-LOGISTIC-CASE-STUDY','DUMMY-COMBINED-REPORT')) {
  Copy-Item "results/pdf/$stem.pdf" "docs/$stem.pdf" -Force
  Write-Host "Copied $stem.pdf"
}
```

Confirm all six files are present in `docs/`.

---

## Step 5 — Git commit and push

Stage **only** DUMMY-related files — do **not** stage `docs/index.html` or any other file:

```powershell
cd d:\github\ENEL445
git add report/DUMMY-*.tex results/pdf/DUMMY-*.pdf docs/DUMMY-*.pdf
$ts = Get-Date -Format "yyyy-MM-dd HH:mm"
git commit -m "docup-dummy: refresh awaiting-review copies as of $ts"
git push
```

Confirm the push succeeded and report the commit hash.

---

## Step 6 — Verify

After 1–3 minutes for GitHub Pages propagation, confirm:
- `https://david-ewing-nz.github.io/ENEL445/DUMMY-LINEAR-CASE-STUDY.pdf` — 1-page PDF, black box visible
- `https://david-ewing-nz.github.io/ENEL445/DUMMY-COMBINED-REPORT.pdf` — 1-page PDF, black box visible
- The real PDFs (e.g. `20260511A-LINEAR-CASE-STUDY.pdf`) remain accessible and unchanged
