# Introduction Redesign — Discussion Record

**Date:** 11 May 2026 (updated)
**Status:** Active — edits being applied to 20260511A rev of all five case studies.

---

## Changes Applied (11 May 2026) — CS3 (20260511A-LOGISTIC-CASE-STUDY.tex)

| # | Change | Rationale |
|---|--------|-----------|
| 1 | Added opener sentence: "Bayesian logistic regression is the simplest non-trivial model in which the posterior is \underline{genuinely non-conjugate}..." | Parallel to CS1's opener; positions CS3 as the non-conjugate contrast |
| 2 | Collapse footnote changed to match CS1: "for the full mechanistic explanation." | The longer JJ-specific version was over-specific and asymmetric with CS1 |
| 3 | \emph{} intentionally absent from "posterior variance collapse" in CS3 | User confirmed this is correct — do not add it |

## Load-Bearing Differences — CS3 vs CS1 (do NOT change)

| Item | CS1 | CS3 | Reason |
|------|-----|-----|--------|
| Collapse paragraph | "compounded by the mean-field factorisation assumption" | Absent | CS3 has one factor group; factorisation does not compound collapse |
| Slot 4 paragraph | 4 methods + entropy regularisation (shows $\mathcal{L}_{\text{reg}}$) | ELBO form + JJ bound + challenge sentence (shows base $\mathcal{L}$) | CS1 is a methodology roadmap — introduces the 4 methods for the first time; CS3 explains why logistic is hard — needs the expanded ELBO as a scaffold for the JJ bound argument |
| Smith paragraph | mentions least-squares/normal equations/τ_e | mentions linear predictor x_i^Tβ through sigmoid | Model-specific |
| θ definition | θ = (β, τ_e) | θ = β | Bernoulli has no noise precision |

---

## Python Code — CS1 vs CS3 Structural Differences (verified 11 May 2026)

| Difference | CS1 (`linear_run.ipynb` + `vb_algorithms_py.py`) | CS3 (`logistic_run.ipynb`) |
|---|---|---|
| Reference posterior | `run_gibbs_simple_linear()` — exact Normal–Gamma Gibbs, cheap | `sample_pg_*()` — Pólya–Gamma Gibbs, 200×50=10,000 Gamma draws/iteration |
| ELBO | Closed-form Gaussian–Gamma ELBO | Jaakkola–Jordan bound at optimal ξᵢ* |
| Parameters | θ=(μ_β, L, η_a, η_b) — includes τ_e factors | θ=(μ, L̃₁₁, ℓ₂₁, L̃₂₂) — β only, 5 parameters |
| CAVI | Closed-form coordinate updates for both β and τ_e | JJ-based coordinate update for β only |

Notebook structure mirrors report sections: `logistic_run.ipynb` Stage 4 = PG sampler = CS3 Section 2.

---

---

## Context

Each of the five case study reports currently opens with a generic Bayesian introduction
using θ notation and a wall of equations. This redesign makes each introduction
pedagogical — building the reader up step by step — and ensures all five case studies
use consistent, model-specific notation from the first equation.

---

## Decision 1: Two-equation opening — general then specific

Each introduction must present **two** equations in sequence:

**Step 1 — General Bayes:**
```
p(θ | y) = p(y | θ) p(θ) / ∫ p(y | θ) p(θ) dθ
```
Written once as the universal anchor. θ is named as a placeholder for "all unknown parameters".

**Step 2 — Model-specific substitution:**
Immediately after, state in plain English what θ is for *this* case study, then write
the specialised proportionality. Example for CS1:

> "In this case study, θ = (β, τ_e) — the regression coefficients and the observation
> noise precision — so the posterior of interest is:
> p(β, τ_e | y) ∝ p(y | β, τ_e) p(β) p(τ_e)"

---

## Decision 2: τ_e not bare τ (from CS1 onwards)

Use τ_e (subscript e = error, observation noise) throughout CS1 and CS2.
Rationale: CS4 introduces a second precision τ_u (subscript u = unit/random effect).
Establishing τ_e in CS1 makes the CS4 extension read as a natural addition,
not a notation change.

---

## Decision 3: Model-specific θ substitution per case study

| CS | Model | θ substitution | Notes |
|----|-------|---------------|-------|
| CS1 | Bayesian linear regression | θ = (β, τ_e) | Baseline — establishes the pattern |
| CS2 | Bayesian quadratic regression | θ = (β, τ_e) | Same structure; X includes x² column |
| CS3 | Bayesian logistic regression | θ = β | No τ_e — Bernoulli likelihood; Jaakkola–Jordan bound |
| CS4 | Hierarchical Bayesian linear | θ = (β, u, τ_e, τ_u) | Adds group offsets u and random-effect precision τ_u |
| CS5 | Hierarchical Bayesian logistic | θ = (β, u) | Combines CS3 (no τ) and CS4 (group effects) |

---

## Decision 4: Pedagogical 4-step scaffold per introduction

Every introduction follows this structure:

1. **The problem** — what model, what data (one sentence)
2. **The unknowns** — name each parameter in plain English before giving it a symbol
3. **The Bayesian answer** — general p(θ|y), then immediately specialise to p(β, τ_e | y) etc.
4. **The computational challenge** — the integral is intractable; VI converts it to optimisation

---

## Decision 5: Comparison table belongs in Combined Report only

The table in Decision 3 above is comparative and belongs **only** in the Combined Report
introduction. Individual case study introductions must not forward-reference other case studies.
Each document stands alone.

**Implication for draft text:** The CS1 draft below previously said "later case studies introduce
a second precision τ_u for random effects" — this violates Decision 5 and has been removed.
τ_e should be explained as "subscript e for observation error" with no mention of τ_u.

---

## Open Question (not yet a decision): Cholesky and variance collapse placement

Currently in CS1, Cholesky reparameterisation and posterior variance collapse appear in
the Introduction section. These could be considered **methods/results** topics more suited
to their own sections.
*Should these be moved out of the Introduction? This was observed but not explicitly agreed — pending discussion.*

## Decision 7: Notation tables carry the disambiguation burden

Each case study contains a key notation table. This is the correct and sufficient place
for the reader to resolve any symbol conflicts — including the lecture-notation differences
(Prof. R.S. Smith used θ for β, Φ for X, d for p).

**Consequences:**
- Introduction opening paragraphs need NO parenthetical notation explanations.
  Just write the correct symbols cleanly and let the table do its job.
- Prof. Smith footnotes are fixed attribution to course context. They appear wherever
  the document uses a symbol that Smith named differently. They stay verbatim and are
  NOT a notation decision made in this paper — do not remove or alter them.
- Which Smith footnotes appear will differ per case study depending on which symbols
  that document uses.
- The notation table entry for β should already read:
  "regression coefficient vector (denoted θ in lectures, Prof. R.S. Smith, ENEL445 2026)"

---

### CS1 — `20260510B-LINEAR-CASE-STUDY.tex`
- Opening equation uses **θ** (generic) — not yet specialised to (β, τ_e) ✗
- Body sections (Bayesian Regression Model subsection) already use τ_e correctly ✓
- Cholesky reparameterisation is in the Introduction — placement pending discussion ⚠
- Variance collapse discussion is in the Introduction — placement pending discussion ⚠
- **Prof. Smith footnotes — preserve as-is**: the current tex has footnotes stating
  "β denoted θ in lectures (Prof. R.S. Smith, ENEL445 2026)", "X denoted Φ in lectures",
  etc. These are fixed attribution to course context, not notation choices. They stay
  verbatim. The notation table in the document is the reader's resolution mechanism —
  the introduction text needs no additional explanation of these differences.
- Subsections "Numerical Study" and "Bayesian Linear Regression" within the Introduction
  block are valid content and stay unchanged. Only the opening paragraphs (before
  the first subsection) are being rewritten.

### CS2 — `20260510B-QUADRATIC-CASE-STUDY.tex`
- Same structure as CS1: opening uses θ generically ✗
- Body already uses τ_e throughout ✓
- Same Cholesky/variance collapse issue as CS1 ✗ (assumed — not yet fully read)

### CS3 — `20260510B-LOGISTIC-CASE-STUDY.tex`
- Opening section found at line 104 — content not yet read in this session
- No τ_e expected (Bernoulli likelihood) — needs verification

### CS4 — `20260510B-HIERARCHICAL-LINEAR-CASE-STUDY.tex`
- Content not yet read in this session

### CS5 — `20260510B-HIERARCHICAL-LOGISTIC-CASE-STUDY.tex`
- Content read 10 May 2026.
- Introduction does NOT use the generic θ opening — goes straight to model description
  in plain English, then model equations in the Model Formulation section.
- Real-world motivating sentence present ✓
- Model explained in prose before equations ✓
- Computational challenge is model-specific ✓
- No two-equation (general → specific) structure — model-specific only from line one.

---

## Open Questions — CS1 vs CS5 comparison (pending discussion)

The following points were observed by comparing the CS5 introduction against CS1.
These are questions, not decisions. No .tex changes should be made based on these
until each is explicitly approved by the user.

**Q1 — Motivating sentence:**
CS5 opens with a real-world application context sentence before any mathematics.
CS1 opens immediately with "Bayesian inference provides principled uncertainty
quantification..." which is generic.

**Resolution (agreed 10 May 2026):** A real-world application motivating sentence
does NOT apply to CS1. CS1 is a methodological testbed — the data is synthetic,
and the model is chosen because it is the simplest case where all components of
variational inference (ELBO, gradients, posterior approximation) can be derived
and verified in closed form. Pretending it is an application study would be misleading.

Instead, CS1's motivating sentence should be methodological:
> "Bayesian linear regression is the simplest non-trivial model in which all
> components of variational inference — the ELBO, its gradient, and the posterior
> approximation — can be derived and verified in closed form, making it the natural
> baseline for comparing optimisation methods."

Q1 may apply to CS3, CS4, and CS5, which have stronger natural application contexts.
To be reviewed when those case studies are addressed.

**Q2 — Model in plain English before equations:**
CS5 explains what the model does in prose before writing any LaTeX.
CS1 goes straight to the posterior integral.
*Should CS1 describe y = Xβ + ε in plain English (what β means, what τ_e means)
before presenting the equations?*

**Q3 — Specific vs generic computational challenge:**
CS5 names why *this particular model* is hard: "the logistic likelihood is not
conjugate to any natural prior."
CS1 says "the posterior integral cannot be evaluated analytically" — true of everything.
Note: for Bayesian linear regression with Gaussian-Gamma priors, CAVI updates ARE
available in closed form. The honest statement for CS1 may be that gradient-based
optimisers are applied as a testbed for harder cases.
*Should CS1's computational challenge statement be made more specific?*

**Q4 — Series position statement:**
CS5 says "this is Case Study 5, combining CS3 and CS4."
*Should CS1 note that it is the foundational case study and subsequent studies
build on this framework — without naming them specifically?*

---

## Draft introduction text (for review — not yet in LaTeX)

### CS1 — Bayesian Linear Regression

Bayesian linear regression is the simplest non-trivial model in which all components
of variational inference — the ELBO, its gradient, and the posterior approximation —
can be derived and verified in closed form, making it the natural baseline for
comparing optimisation methods.

Bayesian inference provides principled uncertainty quantification by treating unknown
quantities as probability distributions rather than point estimates. In general, given
data **y** and parameters **θ**, Bayes' theorem gives the posterior:

    p(θ | y) = p(y | θ) p(θ) / ∫ p(y | θ) p(θ) dθ

In this case study, the model is Bayesian linear regression:
**y** = **X**β + ε, where ε ~ N(0, τ_e⁻¹ I).
Two quantities are unknown: the regression coefficients **β** and the observation
noise precision τ_e. Substituting θ = (β, τ_e), the posterior of interest is:

    p(β, τ_e | y) ∝ p(y | β, τ_e) p(β) p(τ_e)

The substitution θ = (β, τ_e) is specific to this case study; other case studies
in this project define θ according to their own model parameters.

The denominator — the marginal likelihood — has no closed form, making exact posterior
inference intractable. Variational Inference (VI) resolves this by converting the
integration problem into an optimisation problem, making it directly amenable to the
gradient-based methods studied in this course.

---

### CS2 — Bayesian Quadratic Regression

*(Same opening as CS1, with this substitution sentence:)*

In this case study, the model is Bayesian quadratic regression. The design matrix
**X** ∈ ℝⁿˣ³ includes a column of ones, a column of x, and a column of x², so that
**y** = **X**β + ε models nonlinear relationships with a linear-in-parameters framework.
The unknowns are β ∈ ℝ³ and the observation noise precision τ_e. Substituting
θ = (β, τ_e), the posterior of interest is:

    p(β, τ_e | y) ∝ p(y | β, τ_e) p(β) p(τ_e)

*(Computational challenge paragraph identical to CS1.)*

---

### CS3 — Bayesian Logistic Regression

*(Same general Bayes opening, then:)*

In this case study, the model is Bayesian logistic regression. The response y_i ∈ {0,1}
follows a Bernoulli distribution: y_i | β ~ Bernoulli(σ(x_iᵀβ)), where σ(·) is the
logistic sigmoid. There is no observation noise term: the only unknowns are the
regression coefficients **β**. Substituting θ = β, the posterior of interest is:

    p(β | y) ∝ p(y | β) p(β)

The Bernoulli likelihood makes this posterior non-conjugate, so exact inference is
intractable. The Jaakkola–Jordan variational bound provides a tractable quadratic
lower bound on log p(y | β), enabling CAVI updates in closed form.

---

### CS4 — Hierarchical Bayesian Linear Regression

*(Same general Bayes opening, then:)*

In this case study, the model is hierarchical Bayesian linear regression with J groups.
Observations within each group j share a common group-level offset u_j, so that
y_ij = x_ijᵀβ + u_j + ε_ij. Four quantities are unknown: the fixed-effect coefficients
**β**, the group random effects **u** = (u_1,...,u_J)ᵀ, the observation noise
precision τ_e (error), and the random-effect precision τ_u (unit). Substituting
θ = (β, u, τ_e, τ_u), the posterior of interest is:

    p(β, u, τ_e, τ_u | y) ∝ p(y | β, u, τ_e) p(u | τ_u) p(β) p(τ_e) p(τ_u)

*(Computational challenge paragraph as before.)*

---

### CS5 — Hierarchical Bayesian Logistic Regression

*(Same general Bayes opening, then:)*

In this case study, the model is hierarchical Bayesian logistic regression with J groups.
Each observation y_ij ∈ {0,1} follows a Bernoulli distribution:
y_ij | β, u_j ~ Bernoulli(σ(x_ijᵀβ + u_j)), where σ(·) is the logistic sigmoid.
Two quantities are unknown: the fixed-effect coefficients **β** and the group random
effects **u** = (u_1,...,u_J)ᵀ. There is no noise precision term (Bernoulli likelihood).
Substituting θ = (β, u), the posterior of interest is:

    p(β, u | y) ∝ p(y | β, u) p(u | τ_u) p(β)

Note: τ_u appears as a fixed hyperparameter here, not inferred. The Jaakkola–Jordan
bound is extended to handle the random intercepts within the CAVI framework.

*(Computational challenge paragraph as before.)*

---

## Action items (awaiting approval before editing .tex files)

- [ ] CS1: Replace current Introduction section with draft above
- [ ] CS1: Move Cholesky and variance collapse paragraphs out of Introduction
- [ ] CS2: Replace current Introduction section with draft above
- [ ] CS3: Replace current Introduction section with draft above
- [ ] CS4: Replace current Introduction section with draft above
- [ ] CS5: Replace current Introduction section with draft above
- [ ] Combined report: Add comparison table (Decision 3) to its Introduction
- [ ] Recompile all 6 documents after edits
- [ ] Commit and push

---

## CS1 Development Log — 20260510B and 20260510C

The following decisions were made during editing sessions on 10 May 2026.
They apply to `report/20260510B-LINEAR-CASE-STUDY.tex` and `report/20260510C-LINEAR-CASE-STUDY.tex`.
The B series represents the edited-and-cleaned version of A; the C series is a further
human-voice revision of B. These decisions are NOT yet propagated to other case studies.

---

### Decision 8: Section heading "Observation in This Report" → "Diagnostic"

The original heading implied a future observation. Renamed to "Diagnostic" to reflect
that this subsection describes a diagnostic procedure applied in the report, not a
forthcoming observation.

---

### Decision 9: Approaches Considered — clarifying sentence added

Added the sentence: "Of these, only entropy regularisation (Approach 3) is implemented
in this report; the first two are discussed to motivate that choice."

Rationale: without this sentence, the reader cannot tell which approaches are theoretical
context and which are actually implemented.

---

### Decision 10: Section heading "Shared Entry and Exit Conditions" → "Shared Ascent Check and Exit Conditions"

The original heading implied these were entry conditions (initialisation). The section
actually covers the ascent condition check and exit criteria shared across line-search
methods. Corrected accordingly.

---

### Decision 11: θ → ξ throughout ELBO Evaluation and Gradient Verification

The unconstrained optimisation vector is ξ, not θ. The model parameters are
θ = (β, τ_e). Using θ in the gradient verification subsection was a notation clash.
All instances corrected: ∇_θ → ∇_ξ, ∂θ_i → ∂ξ_i, θ ± h e_i → ξ ± h e_i.

---

### Decision 12: Gradient Ascent subsection — update rule rewritten in ξ

The original update rule used a mix of φ (full variational vector) and ξ (unconstrained
vector). Simplified to use ξ throughout, with the redundant φ equation removed.

---

### Decision 13: BFGS — O(d²) → O(dim(ξ)²)

The per-iteration cost was written as O(d²) but d is used in the document for the
number of unconstrained parameters. To avoid ambiguity with p (predictors), changed
to O(dim(ξ)²).

---

### Decision 14: Test Case 2 (Quadratic) removed from CS1 file

The quadratic test case subsection was found in the CS1 file. It belongs only in the
CS2 file. Removed entirely from CS1.

---

### Decision 15: Code Structure rewritten to be CS1-specific

The original Code Structure section referenced a generic dict-loop pattern and two
test cases. Rewritten to reference `generate_linear_case()` only, with a single
`run_all_methods()` call.

---

### Decision 16: Nocedal & Wright added to references.bib

Citation (Nocedal & Wright) was used inline without a .bib entry. Added:
`@book{Nocedal2006, author={Nocedal, Jorge and Wright, Stephen J.}, title={Numerical
Optimization}, edition={2}, publisher={Springer}, year={2006}}`.
Inline citation updated to `\cite{Nocedal2006}`.

---

### Decision 17: Implementation Specifications subsection removed from main body

An 8-subsection block (Cholesky parameterisation, log-space, initialisation, Armijo
algorithm, Newton regularisation, convergence criteria, gradient verification, failure
modes) was in the main body. This is programming specification material, not report
content. Removed; the appendix already covers these topics.

---

### Decision 18: Evaluation Criteria section replaced with Assessment Framework

The original section was a bulleted planning list ("The following criteria will be used
to evaluate..."). Replaced with a single paragraph titled "Assessment Framework" stating
three criteria definitively: convergence to CAVI optimum, posterior accuracy against
Gibbs/true posterior, computational cost.

---

### Decision 19: Conclusion — quadratic reference removed

"Linear and quadratic Bayesian regression test cases" → "A linear Bayesian regression
test case". CS1 is not responsible for the quadratic case.

---

### Decision 20: Appendix A Observation — draft language fixed

"This will be demonstrated empirically as the first Python task" changed to past tense
with a cross-reference: "As shown in Section~\ref{sec:results}, the numerical
experiments confirm this analytically."

---

### Decision 21: KL equation extended to three-line aligned form

The Why Collapse Occurs subsection previously had a two-line KL expression using generic
dθ. Expanded to three lines:
1. Generic integral (notag)
2. CS1-specific double integral over β and τ_e with joint q(β,τ_e) (notag)
3. CS1-specific with mean-field factorisation q(β)q(τ_e) substituted (numbered)

---

### Decision 22: \newpage before Appendix A (VB Posterior Variance Collapse)

Added to ensure the appendix begins on a fresh page.

---

### Decision 23: Appendix A "Selected Approach" — future tense fixed

"Entropy regularisation (Approach 3) will be implemented and compared..." → "is
implemented and compared...". The implementation exists; future tense was draft residue.

---

### Decision 24: ∇_θ → ∇_ξ in vb_algorithms_py.py bullet in Python appendix

The analytical gradient bullet described ∇_θ L (no bold, wrong symbol). Corrected
to ∇_ξ L (bold ξ, consistent with established notation).

---

### Decision 25: Project Status and Course Alignment appendix removed

The final appendix was a project-management document: a dated checklist of completed
derivations, a timeline table (Week 7–12), and alignment notes. This is draft scaffolding
with no place in a submitted report. Removed entirely.

---

### Resolution of Q2 (Model in plain English before equations)

**Agreed (10 May 2026, C revision):** The Introduction already opens with the posterior
integral and immediately specialises θ = (β, τ_e). The prose after the equations
explains what τ_e means. No separate plain-English paragraph added — the current
structure (equation then explanation) is the correct order for a technical report.

---

### Resolution of Q3 (Specific vs generic computational challenge)

**Agreed (10 May 2026, C revision):** The challenge statement in the Introduction was
made CS1-specific. With Gaussian-Gamma conjugate priors, CAVI is analytically available
and gradient-based methods are applied as a testbed. The honest framing is: CAVI is
the natural solver here; the gradient methods are studied to understand their behaviour
before applying them to non-conjugate models.

---

### Resolution of Q4 (Series position statement)

**Not implemented.** A series-position sentence ("this is the foundational case study")
was considered but not added. CS1 stands alone; forward references to other case studies
violate Decision 5.

---

### C-revision decisions (humanising prose, 10 May 2026)

The following changes were made in the C revision to reduce AI-writing tells:

- **Duplicate abstract removed.** The B abstract contained two overlapping blocks
  (a rough draft and a revision). Replaced with a single clean version that opens with
  "but this convenience comes with a cost" and explains the choice of the linear model.

- **\vspace{} spacers removed from Introduction.** Five `\vspace{1em}` and
  `\vspace{2em}` tags between Introduction paragraphs were assembly artefacts.
  Removed; paragraph spacing is now handled by LaTeX normally.

- **"Posterior Variance Collapse" → "posterior variance collapse".** The capitalised
  form treated it as a proper noun. It is a descriptive term.

- **\ref{app:vb-collapse} → Appendix~\ref{app:vb-collapse}.** Cross-reference style
  corrected.

- **Optimisation Problem Formulation opener rewritten.** "Having established that VI
  converts posterior inference into optimisation, the problem must be stated precisely
  before any method can be applied. This section identifies the decision variables..."
  replaced with two direct sentences.

- **Computational Characteristics single-bullet subsection removed.** A subsection
  containing a single bullet point ("Parameters exhibit coupling...") was removed.
  The content is covered in the Discussion section.

- **Positive definite footnote trimmed.** A 5-line footnote defining "positive definite"
  with bold terms and underlines was replaced with an inline `\bm{\Sigma}_\beta \succ 0`.

- **Positive semidefinite footnote trimmed.** A paragraph-length footnote on
  semidefiniteness, invertibility, and degenerate directions was reduced to one sentence.

- **Test Cases section opener rewritten.** "This section defines the two numerical test
  cases and gives the implementation details..." replaced with two direct sentences.

- **Discussion failure modes — bullets instead of numbered prose.** "First... Second..."
  paragraph replaced with a `\begin{itemize}` list. "Newton's Method" normalised to
  "Newton's method" (title case was an AI tell).

---

---

## CS3 Development Log — 20260510B-LOGISTIC-CASE-STUDY.tex

The following decisions were made during editing on 10 May 2026.
They apply to `report/20260510B-LOGISTIC-CASE-STUDY.tex`.

---

### Decision CS3-1: Document is fully standalone (Decision 5 applied)

All cross-references to other case studies removed throughout:
- Abstract: "timing comparisons across the linear, quadratic, and logistic notebooks" → within-notebook framing only
- Introduction: "third numerical study in this project (following linear and quadratic...)" → removed; replaced with model-specific challenge statement
- PG Gibbs section: "more expensive than conjugate Gaussian Gibbs used in the linear and quadratic cases" → "more expensive per sample than the VI methods"
- Timing figure caption: "(vs. the linear and quadratic cases)" → removed
- Discussion "Comparison Across Test Cases" subsection: entire table removed; replaced with "Model Characteristics" prose covering CS3 properties only
- Conclusion: "in contrast to the linear and quadratic Gaussian cases" → removed; replaced with mechanistic explanation
- Code appendix: "linear_ and quadratic_ figures from the other test cases" → "figures from other notebooks in this project"

---

### Decision CS3-2: CAVI fixed point qualified as JJ-bound fixed point

"unique stationary point in this model (the CAVI fixed point)" → "unique stationary point at the CAVI fixed point under the Jaakkola–Jordan bound."
Rationale: CAVI is not an analytical fixed point of the true ELBO (likelihood is non-conjugate). It is the fixed point of the JJ-bound ELBO. The qualification is factually necessary.

---

### Decision CS3-3: Planning meta-sentence removed from Optimisation Components

"Each method is described in terms of the four components from the ENEL445 course: entry conditions, search direction, step-size rule, and exit conditions." removed before the description block.
Same as Decision 18 (CS1) — planning scaffolding, not report content.

---

### Decision CS3-4: Posterior Variance Collapse discussion reframed

Original opened with "Unlike the linear and quadratic Gaussian regression cases..." — cross-reference violation.
Rewritten to open with the result directly: "Posterior variance collapse is minimal in this model. All four VI methods achieve standard-deviation ratios σ_VI/σ_Gibbs between 0.90 and 1.10 for both parameters." Mechanistic explanation follows immediately.

---

### Decision CS3-5: "Comparison Across Test Cases" subsection replaced with "Model Characteristics"

The three-column table (Linear / Quadratic / Logistic) cannot exist in a standalone document.
Replaced with a prose paragraph describing CS3's own model characteristics: non-conjugate Bernoulli likelihood, JJ bound, PG Gibbs reference, PG computational cost, minimal variance collapse.

---

---

### Decision CS3-6: Prof. Smith lecture-notation footnotes added to Introduction

Three footnotes added to the closing paragraph of the CS3 Introduction, matching CS1:
- `\bm{X}` — "Denoted Φ and called the *regressor matrix* in lectures (Prof. R.S. Smith, ENEL445 2026)."
- `\bm{\beta}` — "Denoted θ in lectures."
- `p` — "Denoted d in lectures."

**MANDATORY FOR ALL REMAINING CASE STUDIES (CS4, CS5):**
These footnotes must be present in every case study introduction. They are not optional.
They were established in Decision 7 and must be the first thing checked when editing any new case study.
Failure to include them was the gap in the initial CS3 editing pass.

---

### Open question for CS3: Introduction structure (Decisions 1–4)

The CS3 Introduction now uses the two-equation general-then-specific scaffold (Decision 1):
- General Bayes formula with generic θ
- "In this case study, θ = β" substitution sentence
- Proportionality for p(β | y)
- Substitution note: "The substitution θ = β is specific to this case study..."

This matches the CS1 pattern. Decision 4 (pedagogical 4-step scaffold) is now applied to CS3.

---

## Status after C revision (10 May 2026)

| Item | Status |
|------|--------|
| 20260510B-LINEAR-CASE-STUDY.tex | Complete — compiled cleanly (28 pp) |
| 20260510C-LINEAR-CASE-STUDY.tex | Complete — compiled cleanly (28 pp) |
| Introduction redesign (Decisions 1–7) | Applied in C revision |
| Open Q2, Q3 | Resolved (see above) |
| Open Q4 | Not implemented |
| Cholesky/variance collapse placement | Still pending |
| docs/ folder | Not updated (decision held throughout) |
| Commit | Pending |
