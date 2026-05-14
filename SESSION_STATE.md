# SESSION_STATE — ENEL445
Generated: 2026-05-14

## Git
Last commit: `5ffaec6` (per session — README-WHEN-YOU-RETURN.md shows `ac94e75` from 2026-04-27 as last auto-recorded; session commits added since)  
Uncommitted changes: none (no source files were modified this session — only PDFs compiled)

## Recent PDFs
| Name | Date | Notes |
|------|------|-------|
| `20260514A-LINEAR-CASE-STUDY.pdf` | 2026-05-14 ~10:37 | 30 pages, CS1 |
| `20260514A-HIERARCHICAL-LINEAR-CASE-STUDY.pdf` | 2026-05-14 ~10:40 | 21 pages, CS4 |
| `20260514A-HIERARCHICAL-LOGISTIC-CASE-STUDY.pdf` | 2026-05-14 ~10:44 | 15 pages, CS5 |
| `20260514A-COMBINED-REPORT.pdf` | 2026-05-14 | combined |

## Active Reports
| Report | Filename | Sections (top-level) |
|--------|----------|----------------------|
| CS1 | `20260514A-LINEAR-CASE-STUDY.tex` | Introduction · Optimisation Problem Formulation · Posterior Variance Collapse · ELBO Evaluation · Optimisation Methods · Test Cases and Implementation Details · Assessment Framework · Results and Discussion · Conclusion · [Appendices] |
| CS4 | `20260514A-HIERARCHICAL-LINEAR-CASE-STUDY.tex` | Introduction · Model Formulation · Conjugate Gibbs Sampler · Posterior Variance Collapse · Optimisation Problem Formulation · Numerical Study · Results · Discussion · Conclusion |
| CS5 | `20260514A-HIERARCHICAL-LOGISTIC-CASE-STUDY.tex` | Introduction · Model Formulation · Pólya–Gamma Blocked Gibbs Sampler · Optimisation Problem Formulation · Numerical Study · Results · Discussion · Conclusion |

## Recent Figures
All figures in `figs/` — no timestamps available without terminal. Full set present as of 2026-05-14:

**CS1 (linear_*):** data_scatter, prior_likelihood_posterior, elbo_*, gibbs_*, vb_gibbs_*, comparison_*, gradient_stepsize, mean_errors, newton_condition, sd_ratios, timing_comparison

**CS4 (hierarchical_linear_*):** data_scatter, likelihood_posterior, elbo_*, gibbs_*, vb_gibbs_*, gradient_stepsize, mean_errors, newton_condition, random_effects, sd_ratios, timing_comparison

**CS5 (hierarchical_logistic_*):** data_scatter, elbo_*, gibbs_*, vb_gibbs_*, gradient_stepsize, mean_errors, newton_condition, random_effects, sd_ratios, timing_comparison

## Pending Tasks

1. **[Task A — CS4 figures]** Add prior band to `hierarchical_linear_data_scatter.png` to match CS1 pattern (prior + likelihood + data). The figure currently shows data and likelihood only.
2. **[Task A — CS5 figures]** Add `hierarchical_logistic_likelihood_posterior.png` — CS5 has no likelihood+posterior figure at all. Also verify whether `hierarchical_logistic_data_scatter.png` needs a prior band.
3. **[Task A — recompile]** After updating notebooks, recompile CS4 and CS5 LaTeX to include the new figures in Results sections.
4. **[Task B — section alignment]** Align section names/structure across CS1 (baseline), CS4, CS5. Key gaps:
   - CS5 is missing Posterior Variance Collapse section (CS4 has it, CS1 has it)
   - CS4 and CS5 are missing ELBO Evaluation, Optimisation Methods, Assessment Framework sections
   - CS1 combines Results+Discussion; CS4/CS5 split them — decide whether to split CS1 or merge CS4/CS5
   - CS1 calls it "Test Cases and Implementation Details"; CS4/CS5 call it "Numerical Study" — standardise
5. **[Cleanup]** Delete `AGENT_HANDOFF.md` from workspace root (superseded by this file). Also delete `cs4_compile.log` and `cs5_compile.log` from workspace root.

## Session-Specific Design Decisions

- **CS1 is the structural baseline.** Do not restructure CS1 to match CS4/CS5 — align CS4/CS5 to CS1.
- **CS4 β₀ ≈ 0.5 vs true 1.0 is NOT a bug.** This is hierarchical shrinkage / non-identifiability between fixed intercept and random effect mean. Do not correct it in code or narrative — it should be discussed in Results.
- **prior_sigma2 = 10.0** (`python/linear_run.ipynb` line 188) is accepted. Do not change it.
- **Figure naming convention:** `<prefix>_<description>.png` where prefix ∈ {`linear_`, `hierarchical_linear_`, `hierarchical_logistic_`}.
- **Two-figure entry pattern in Results (CS1 baseline):**
  - Figure 1: prior band + likelihood band + data scatter (title: "Prior and Likelihood")
  - Figure 2: likelihood band + posterior band (title: "Likelihood and Posterior")
  - CS4 and CS5 must have equivalent pairs.

## Preserved Assumptions

- Do **not** git commit or push without explicit user instruction.
- Python: system install at `D:\Python`. No venv. Do not create one.
- LaTeX: xelatex via MiKTeX at `D:\MiKTeX`. Compile via `python scripts/archive_tex.py report/<file>.tex`.
- Python notebooks: run via `python scripts/archive_py.py python/<file>.py`.
- Pre-compile check: every `.tex` must contain `\mymarginlabel` and `\hypersetup` with `\jobname` before compiling.
- All three reports use 5-method pipeline: CAVI, Gradient Ascent, Newton's Method, BFGS, Gibbs (gold standard).

## Do Not Scan
- `archive/` — timestamped compile snapshots, large, read-only
- `_unzipped/` — course material zip extracts, read-only
- `results/pdf/` — binary PDFs
- `cs4_compile.log`, `cs5_compile.log` — temporary, workspace root
- `AGENT_HANDOFF.md` — superseded by this file, pending deletion
