# AGENT HANDOFF — ENEL445 Case Study Reports

**Date:** 2026-05-14  
**Student:** David Ewing (82171165)  
**Course:** ENEL445 — Applied Engineering Optimisation

---

## 1. Project Goal

Three LaTeX case study reports (CS1, CS4, CS5) must be internally consistent in structure, figures, and narrative. CS1 is the agreed baseline. CS4 and CS5 should follow the same section order and have equivalent figures.

---

## 2. Original Problem (this session)

Recompile CS1, CS4, CS5 LaTeX after overlay figures were added to their notebooks in the previous session. Reports were not to be committed or pushed.

---

## 3. Current Checkpoint State

### Compiled PDFs — all confirmed in `results/pdf/`
| File | Pages | Archive |
|------|-------|---------|
| `20260514A-LINEAR-CASE-STUDY.pdf` | 30 | `20260514103749` |
| `20260514A-HIERARCHICAL-LINEAR-CASE-STUDY.pdf` | 21 | `20260514104053` |
| `20260514A-HIERARCHICAL-LOGISTIC-CASE-STUDY.pdf` | 15 | `20260514104440` |

### Git status
No commits or pushes made this session. Last commit: `5ffaec6`.

### Discussion reached but not yet acted on
Two tasks were agreed upon but **not yet implemented**:

**Task A — Add missing figures to CS4 and CS5 notebooks:**
- CS1 has two "entry" figures in Results & Discussion:
  1. `linear_data_scatter.png` — Prior + Likelihood (initial conditions)
  2. `linear_prior_likelihood_posterior.png` — Likelihood + Posterior (inference result)
- CS4 has `hierarchical_linear_data_scatter.png` but its prior band is absent. It has `hierarchical_linear_likelihood_posterior.png` but no prior+likelihood equivalent.
- CS5 has `hierarchical_logistic_data_scatter.png` but no likelihood+posterior figure at all.
- **Action needed:** Update CS4 and CS5 notebooks to generate equivalent two-figure sets.

**Task B — Align section structure between CS1 (baseline) and CS4/CS5:**

| # | CS1 (baseline) | CS4 | CS5 |
|---|---|---|---|
| 1 | Introduction | Introduction | Introduction |
| 2 | Optimisation Problem Formulation | Model Formulation | Model Formulation |
| 3 | Posterior Variance Collapse | Conjugate Gibbs Sampler | Pólya–Gamma Blocked Gibbs Sampler |
| 4 | ELBO Evaluation | Posterior Variance Collapse | Optimisation Problem Formulation |
| 5 | Optimisation Methods | Optimisation Problem Formulation | Numerical Study |
| 6 | Test Cases and Implementation Details | Numerical Study | Results |
| 7 | Assessment Framework | Results | Discussion |
| 8 | Results and Discussion | Discussion | Conclusion |
| 9 | Conclusion | Conclusion | — |

Sections present in CS1 but **missing** in CS4 and CS5:
- ELBO Evaluation
- Optimisation Methods
- Assessment Framework

CS4/CS5 split Results and Discussion (better practice); CS1 combines them.

---

## 4. Files Changed This Session

None. Only compiled PDFs were produced (not source files).

---

## 5. Important Design Decisions

- **CS1 is the structural baseline.** CS4 and CS5 should be brought into alignment with it, not the reverse.
- **British English throughout** all source files and comments (exception: library API args keep American spelling).
- **prior_sigma2 = 10.0** in CS1 (`python/linear_run.ipynb` line 188). This gives $\sigma_0 \approx 3.16$ — on the *small* side for a flat prior given $|\beta| \sim 2$, but accepted as-is.
- **CS4 beta0 offset is NOT a bug.** In `hierarchical_linear_vb_gibbs_beta0.png`, all methods estimate $\beta_0 \approx 0.5$ rather than the true value of 1.0. This is hierarchical shrinkage / non-identifiability between the fixed intercept and the random effect mean $u_j$. Do not "fix" this.
- **Compile command:** Always use `python scripts/archive_tex.py report/<file>.tex` — never compile directly.
- **Python run command:** Always use `python scripts/archive_py.py python/<file>.py` for files in `python/`.

---

## 6. Things Tried and Failed

- **Terminal polling via `get_terminal_output`** during async CS5 compile: all calls returned 32KB files (truncated xelatex preamble output) without visible completion marker. Workaround: read compile log file directly with `grep_search` for "Output written|PDF ->|Archive:".
- **Sync terminal commands after async CS5 compile:** All returned `>>` (PowerShell continuation prompt) because the terminal session was attached to the still-running async process. Commands silently did nothing. Workaround: use `file_search` or `grep_search` to verify file existence instead.

---

## 7. Current Blocker

None. The next steps (Task A and Task B above) are clearly defined. The user confirmed intent to add missing sections and figures but the conversation was paused to discuss the CS4 prior plot before implementation began.

---

## 8. Relevant Commands Already Run

```powershell
# CS1 compile
D:\Python\python.exe scripts/archive_tex.py report/20260514A-LINEAR-CASE-STUDY.tex

# CS4 compile (log tee'd)
D:\Python\python.exe scripts/archive_tex.py report/20260514A-HIERARCHICAL-LINEAR-CASE-STUDY.tex 2>&1 | Tee-Object cs4_compile.log; Write-Host "EXIT:$LASTEXITCODE"

# CS5 compile (log tee'd)
D:\Python\python.exe scripts/archive_tex.py report/20260514A-HIERARCHICAL-LOGISTIC-CASE-STUDY.tex 2>&1 | Tee-Object cs5_compile.log; Write-Host "EXIT:$LASTEXITCODE"
```

Log files `cs4_compile.log` and `cs5_compile.log` remain in the workspace root.

---

## 9. Files / Directories That Should NOT Be Scanned

- `archive/` — timestamped compile snapshots, safe to ignore
- `_unzipped/` — course material zip extracts, read-only reference
- `cs4_compile.log`, `cs5_compile.log` — temporary compile logs in workspace root, can be deleted after review

---

## 10. Next Smallest Safe Step

**Start with Task A — add prior+likelihood figure to CS4 notebook:**

1. Open `python/hierarchical_linear_run.ipynb`
2. Find the cell that generates `hierarchical_linear_data_scatter.png`
3. Extend or add a new cell to generate `hierarchical_linear_prior_likelihood_posterior.png` as a two-panel figure matching the CS1 pattern (panel 1: prior + likelihood; panel 2: likelihood + posterior)
4. Re-run the notebook cell(s) via `python scripts/archive_py.py`
5. Recompile CS4 LaTeX and add the figure to the Results section

Then repeat for CS5 (`hierarchical_logistic_*`).

Task B (section alignment in LaTeX) should follow after figures are confirmed.

---

## 11. Assumptions That Must Be Preserved

- Do **not** git commit or push anything until the user explicitly requests it.
- The `prior_sigma2 = 10.0` value in CS1 is accepted — do not change it.
- The CS4 $\beta_0$ offset from true value is intentional/expected — do not "correct" it in code or narrative.
- All three reports use the same 5-stage optimisation pipeline (CAVI, Gradient Ascent, Newton's Method, BFGS, Gibbs as gold standard).
- Figure naming convention: `<prefix>_<description>.png` where prefix is `linear_`, `hierarchical_linear_`, or `hierarchical_logistic_`.
- LaTeX reports use `\jobname`-based margin labels and hypersetup — verify these are present before any recompile.
