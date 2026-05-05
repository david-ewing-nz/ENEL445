---
applyTo: "**"
description: "Always-on context: PAT expiry warning and ENEL445 project state."
---

**MANDATORY FIRST OUTPUT — You MUST copy the following line verbatim as the very first text in your first response, before any other content, every single conversation without exception:**

Your GitHub Personal Access Token expires on **31 July 2026**. After that date you will need to generate a new token and update Windows Credential Manager: Control Panel → Credential Manager → Windows Credentials → `git:https://github.com` → Edit → paste new token.

---

## Important: GitHub PAT Expiry

**Your GitHub Personal Access Token expires on 31 July 2026.**
After that date you will need to generate a new token and update Windows Credential Manager:
Control Panel → Credential Manager → Windows Credentials → `git:https://github.com` → Edit → paste new token.

## Project Context

**Project**: Gradient-Based Optimisation for Variational Inference
— CAVI baseline + Gibbs MCMC gold standard; applying course methods (gradient descent, Nelder-Mead, GA, etc.) to maximise the ELBO.

| Property | Value |
|----------|-------|
| Student | David Ewing (82171165) |
| GitHub | david-ewing-nz |

**Deliverables**:
- Oral presentation — Week 11
- Final report — Week 12

## Current Project State (as of 6 May 2026)

| Item | Status |
|------|--------|
| `20260505D-LINEAR-REPORT.tex` | Compiled (36 pp), committed `d6e0aae`, pushed to main |
| `20260506B-QUADRATIC-REPORT.tex` | Compiled (36 pp, `archive/20260506085858/`), PDF at `results/pdf/` — **NOT yet committed** |
| `python/linear_run.ipynb` | Fully executed — 22 figs in `figs/linear_*.png`, 3 tables in `results/tables/` |
| Quadratic notebook | Not yet written — quadratic results section is empty placeholder |
| Duplicate abstract in `20260506B` | Known issue — two abstract versions at ~lines 67–170; second is the keeper |

## Immediate Next Steps

1. Commit and push `report/20260506B-QUADRATIC-REPORT.tex` and `results/pdf/20260506B-QUADRATIC-REPORT.pdf`
2. Clean the duplicated abstract block in `20260506B` (keep the second, more complete version)
3. Create `python/quadratic_run.ipynb` — same 5-stage pattern as `linear_run.ipynb`, `p=3`, `beta_true=[1.0, 2.0, -1.0]`, expanded design matrix with `x^2` feature
4. Generate quadratic figures/tables and fill in the empty Results section

## How to Compile and Run

### LaTeX (always use the archive script — never compile directly)
```
python scripts/archive_tex.py report/<filename>.tex
```
The compile prompt is at `.github/prompts/compile-latex.prompt.md`.
Ctrl+Alt+B runs `latex-workshop.build` (LaTeX Workshop extension) — this is a **user keybinding** stored at `D:\VSCode\data\user-data\User\keybindings.json`. After a VS Code update or on a new machine, re-apply it if missing.

### Python (always use the archive script)
```
python scripts/archive_py.py python/<script>.py
```
This applies only to files in `python/`. Scripts in `scripts/` are run directly.

### Pre-compile check (LaTeX)
Every `.tex` file must contain:
1. `\newcommand{\mymarginlabel}{David Ewing dew59@uclive.ac.nz | \DTMnow\ | \jobname.tex}`
2. `\hypersetup{ pdfsubject = {\jobname.tex}, pdfkeywords = {source: \jobname.tex} }`

## Key Files

| Purpose | Path |
|---------|------|
| Active report | `report/` — most recent file by date-letter stamp |
| CAVI + Gibbs implementation | `python/vb_algorithms_py.py` |
| Utilities (archive, plot, I/O) | `python/vb_utils_py.py` |
| Linear results notebook | `python/linear_run.ipynb` |
| Compile prompt | `.github/prompts/compile-latex.prompt.md` |
| Copilot instructions | `.github/copilot-instructions.md` |
| Keybindings (user, not workspace) | `D:\VSCode\data\user-data\User\keybindings.json` |

## Notes

- Python: `D:\Python` (numpy, scipy, polars, matplotlib). No venv.
- LaTeX: `xelatex`, MiKTeX at `D:\MiKTeX`.
- British English throughout (exception: library API args keep American spelling).
- For current git status and file counts see: `README-WHEN-YOU-RETURN.md`
- Deduplication note for `20260506B`: see `/memories/repo/20260506B-deduplication.md`
