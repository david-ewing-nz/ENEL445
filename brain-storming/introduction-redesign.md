# Introduction Redesign — Discussion Record

**Date:** 10 May 2026  
**Status:** Decisions agreed, awaiting LaTeX edits (not yet applied — user approval required before touching any .tex file)

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
