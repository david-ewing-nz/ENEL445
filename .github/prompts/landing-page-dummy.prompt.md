---
name: landing-page-dummy
description: "Landing page: swap 5 of 6 PDF links to DUMMY-* versions (keep LINEAR case study live)."
---

# #landing-page-dummy — Switch landing page to DUMMY links

Update `docs/index.html` so that five of the six document links point to the `DUMMY-*.pdf` placeholders.
**The LINEAR case study link is left unchanged** — it continues to point to the current real PDF.

Work from the project root `d:\github\ENEL445` throughout.

---

## Step 1 — Read current state

Read `docs/index.html` and identify the current `href` values for all six `<a>` elements.
The six entries are:

| Entry | Keep / Replace |
|-------|---------------|
| Combined Report | Replace → `DUMMY-COMBINED-REPORT.pdf` |
| Case Study 1 — Linear Regression | **Keep** (real PDF, unchanged) |
| Case Study 2 — Quadratic Regression | Replace → `DUMMY-QUADRATIC-CASE-STUDY.pdf` |
| Case Study 3 — Logistic Regression | Replace → `DUMMY-LOGISTIC-CASE-STUDY.pdf` |
| Case Study 4 — Hierarchical Bayesian Linear Regression | Replace → `DUMMY-HIERARCHICAL-LINEAR-CASE-STUDY.pdf` |
| Case Study 5 — Hierarchical Bayesian Logistic Regression | Replace → `DUMMY-HIERARCHICAL-LOGISTIC-CASE-STUDY.pdf` |

---

## Step 2 — Apply the five href replacements

Use `multi_replace_string_in_file` (one call, five replacements) on `docs/index.html`.

For each of the five entries to replace, find the `<a href="…"` line and substitute the DUMMY filename.
The link text, description paragraph, and all other HTML must remain exactly as-is.

The target filename for each DUMMY link is the fixed string shown in Step 1 — do **not** include a date prefix.

Example replacement pattern (Combined Report):
```
old:  <a href="20260510A-COMBINED-REPORT.pdf" …>
new:  <a href="DUMMY-COMBINED-REPORT.pdf" …>
```

After the replacements, verify with a quick `grep` that exactly five `DUMMY-` hrefs appear and exactly one real-PDF href remains (the LINEAR case study).

```powershell
Select-String -Path docs\index.html -Pattern 'href="DUMMY-' | Measure-Object | Select-Object -ExpandProperty Count
Select-String -Path docs\index.html -Pattern 'href="[0-9]' | Measure-Object | Select-Object -ExpandProperty Count
# Expected: 5 and 1
```

---

## Step 3 — Commit and push

```powershell
git add docs/index.html
git commit -m "landing page: switch 5 links to DUMMY (LINEAR kept live)"
git push
```

Confirm the commit hash and that the push succeeded.

---

## Step 4 — Verify live URLs

Wait ~60 seconds, then confirm these five DUMMY URLs resolve (HTTP 200):

```
https://david-ewing-nz.github.io/ENEL445/DUMMY-COMBINED-REPORT.pdf
https://david-ewing-nz.github.io/ENEL445/DUMMY-QUADRATIC-CASE-STUDY.pdf
https://david-ewing-nz.github.io/ENEL445/DUMMY-LOGISTIC-CASE-STUDY.pdf
https://david-ewing-nz.github.io/ENEL445/DUMMY-HIERARCHICAL-LINEAR-CASE-STUDY.pdf
https://david-ewing-nz.github.io/ENEL445/DUMMY-HIERARCHICAL-LOGISTIC-CASE-STUDY.pdf
```

And that the LINEAR case study still resolves to its real PDF:
```
https://david-ewing-nz.github.io/ENEL445/20260511A-LINEAR-CASE-STUDY.pdf
```

---

## Notes

- To **restore** all six links to real PDFs, run `#docup` — its Step 6 rewrites `index.html` from the live `.tex` abstracts.
- `DUMMY-*.pdf` files must already be present in `docs/` (put there by `#docup-dummy`). If any are missing, run `#docup-dummy` first.
