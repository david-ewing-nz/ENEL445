---
applyTo: "**"
description: "Always-on context: PAT expiry warning and ENEL445 project state."
---

## Important: GitHub PAT Expiry

> **Your GitHub Personal Access Token expires on 31 July 2026.**
> After that date you will need to generate a new token and update Windows Credential Manager:
> Control Panel → Credential Manager → Windows Credentials → `git:https://github.com` → Edit → paste new token.

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

## Key Files

| Purpose | Path |
|---------|------|
| Main LaTeX report | `report/` |
| CAVI + Gibbs implementation | `python/vb_algorithms_py.py` |
| Utilities (archive, plot, I/O) | `python/vb_utils_py.py` |
| Copilot instructions | `.github/copilot-instructions.md` |

## Notes

- Python: `D:\Python` (numpy, scipy, polars, matplotlib). No venv.
- LaTeX: `xelatex`, MiKTeX at `D:\MiKTeX`.
- For current git status and file counts see: `README-WHEN-YOU-RETURN.md`
