# ENEL445 Progress Report: Optimisation Methods for Variational Inference[^ai]

**Student Name:** David Ewing  
**Student ID:** 82171165  
**Project:** Gradient-Based Optimisation for Variational Inference  
**Date:** 12 Mar 2026  
**Due Date:** 20 Mar 2026 (Week 5, Term 1)

[^ai]: ChatGPT was used to proofread this document and make recommendations to its content/format.
[^holmes]: Dr. John Holmes, Lecturer in Mathematics and Statistics, University of Canterbury (Faculty of Engineering). Profile: https://profiles.canterbury.ac.nz/John-Holmes

---


## 1. Background & Problem Context

### Problem Description

Variational Inference (VI) is a technique in Bayesian statistics that approximates intractable posterior distributions by solving an optimisation problem. When the posterior distribution cannot be computed directly (the normalising constant is intractable), VI finds the best approximation from a simpler parametric family by maximising the Evidence Lower Bound (ELBO).

This project uses ELBO maximisation as a testbed for comparing gradient-based optimisation methods from ENEL445. The objective function (ELBO) is:

$$\text{ELBO}(\phi) = \mathbb{E}_{q_\phi}[\log p(y, \theta)] - \mathbb{E}_{q_\phi}[\log q_\phi(\theta)]$$

where $\phi$ are variational parameters (means and variances of Gaussian approximations), $p(y,\theta)$ is the joint distribution of data and parameters, and $q_\phi(\theta)$ is the variational approximation. The task is to find $\phi^* = \arg\max_\phi \text{ELBO}(\phi)$ using various optimisation techniques covered in ENEL445. (Note: $\phi$ denotes variational parameters, distinct from $\lambda$ which will denote Lagrangian multipliers if we implement constrained methods.)

This project follows the standard ENEL445 pattern of applying course optimisation techniques to a real engineering problem. Just as other projects might optimise power generation schedules or solve geolocation problems, this project applies the same optimisation methods to statistical inference. The ELBO maximisation provides a realistic testbed with smooth objectives, gradient computation, and constrained variants - directly paralleling the optimisation challenges in traditional ENEL445 projects.

### Key Challenges

The main challenge I'm interested in is that standard VI often produces under-dispersed (overconfident) posteriors. Variance parameters tend to collapse to small values, which raises an important question: can constrained optimisation help maintain adequate uncertainty?

**The under-dispersion issue arises from the reverse KL divergence inherent in VI.** The ELBO can be written as $\mathbb{E}_q[\log p(y,\theta)] + H[q]$, where the entropy term $H[q] = -\mathbb{E}_q[\log q]$ does incentivize the approximation to spread out. However, VI minimizes $\text{KL}(q||p)$ (reverse KL), which exhibits mode-seeking behavior: it heavily penalizes placing mass where the true posterior $p$ has low probability. This causes $q$ to underestimate variance to avoid low-probability regions, even when the entropy term encourages spreading. This is particularly problematic for mean-field VI where the independence assumptions eliminate parameter correlations.

From an optimisation perspective, there are also some practical considerations:
- The ELBO is typically smooth but high-dimensional, which means coordinate ascent (the standard VI approach) can be slow to converge
- Second-order information (Hessian) might improve convergence but is expensive to compute and I'm not sure yet whether it's worth the cost
- Different optimisation methods converge at different rates, and it's unclear which will perform best for this objective

### Objective Function Details

For Bayesian linear regression with conjugate priors, the design variables are $\phi = (\mu_\beta, \Sigma_\beta, a_e, b_e)$ where $\mu_\beta$ is the mean of regression coefficients, $\Sigma_\beta$ is the covariance matrix, and $a_e, b_e$ are parameters of the precision distribution. The objective is to maximise ELBO numerically. For the baseline methods there are no constraints, but I plan to experiment with minimum variance constraints later if time permits (which would introduce Lagrangian multipliers $\lambda$ in the standard ENEL445 sense).

---

## 2. Overview of Optimisation Methods

I need to compare several optimisation methods for this project. The standard approach in VI is coordinate ascent, which I have working as a baseline. The core question is whether gradient-based methods from ENEL445 can outperform the standard approach by exploiting joint parameter updates and curvature information.

### Baseline: Coordinate Ascent Variational Inference (CAVI)

This is the standard approach - update each variational parameter whilst holding others fixed, cycling through parameter blocks. For my baseline implementation, I use blocked coordinate ascent where all regression coefficients $\mu_\beta$ are updated together, then the covariance $\Sigma_\beta$, then the precision parameters $(a_e, b_e)$. This blocking strategy (adapted from my summer 2025 research code with Dr. John Holmes'[^holmes] guidance) is more efficient than updating individual scalar parameters.

The main advantages are that updates are analytically tractable for conjugate models and ELBO is guaranteed to increase each iteration. The disadvantages are that convergence can be slow when parameters are strongly coupled, and the method doesn't exploit joint curvature information across parameter blocks.

This serves as the performance baseline for comparison.

### Alternative Methods to Implement

**Gradient Ascent with Line Search** - This seems like the natural first alternative. Compute the full ELBO gradient and use line search to determine step size. For strongly convex objectives, gradient ascent achieves linear (geometric) convergence where the error decreases by a constant factor each iteration. This should be faster than CAVI when the objective has strong coupling between parameters. The trade-off is that line search requires multiple ELBO evaluations per iteration (typically 5-10 for backtracking), whereas CAVI only needs one. I'm choosing this method because it's the simplest way to exploit the full gradient, and it will establish whether joint parameter updates help at all.

**Newton's Method** - Uses both gradient and Hessian of ELBO to determine search direction. Expected convergence is quadratic near the optimum (error reduces as $\epsilon_{k+1} \propto \epsilon_k^2$), which could be substantially faster than gradient methods in the final iterations. The trade-off is computational cost: computing and inverting the Hessian is O(d³) per iteration (where d is the total variational parameter count), versus O(d) for gradient-only methods. For p=3 predictors, the full variational parameter dimension is d=11 (3 for $\mu_\beta$, 6 for symmetric $\Sigma_\beta$, 2 for precision parameters), giving roughly 1,300 operations for the Hessian inversion - still manageable. I'm implementing this to see whether the quadratic convergence justifies the Hessian computation cost. Another challenge is that the Hessian may not be positive definite away from the optimum, requiring regularisation or direction modification.

**BFGS (Quasi-Newton)** - Approximates the Hessian using gradient information from previous iterations. Expected convergence is super-linear (faster than linear but slower than quadratic), typically achieving Newton-like performance without the O(d³) Hessian computation. The approximation is built incrementally with O(d²) updates (where d is the variational parameter count), and BFGS maintains positive definiteness by construction. I'm choosing this method because it's widely regarded as the best general-purpose optimiser for smooth unconstrained problems, and I want to see if it outperforms both gradient ascent and full Newton's method for VI. If BFGS doesn't substantially outperform gradient ascent, that would suggest the ELBO surface doesn't have strong curvature or the problem dimension is too small to benefit.

**Penalty Method (Constrained)** - If I have time, I want to try adding a penalty term to the ELBO to discourage variance collapse: $\text{ELBO}(\phi) - \rho \cdot \text{penalty}(g(\phi))$ where $g(\phi) = \min(0, \sigma^2 - \sigma_{\text{min}}^2)$ enforces minimum variance. This converts the constrained problem to a sequence of unconstrained problems with increasing penalty parameter $\rho$. The challenge is that large $\rho$ makes the objective ill-conditioned (condition number grows with $\rho$), potentially slowing convergence. I'm interested in this approach because it directly addresses the under-dispersion problem rather than just comparing optimisation methods.

---

## 3. Solution Plan

### Approach

My primary focus is comparing four unconstrained optimisation methods for ELBO maximisation: Coordinate Ascent VI (baseline), Gradient Ascent with backtracking line search, Newton's method, and BFGS. If there's time at the end, I'll implement a constrained variant using the penalty method to see if it helps with the variance collapse problem.

I'm using Bayesian linear regression with Gaussian likelihood and conjugate Normal-Gamma priors as the test model. This is a good choice because I can compute the true posterior analytically for validation, it allows a clean comparison of optimisation methods, and there's potential to extend to hierarchical models later if time permits.

### Implementation Plan

Phase 1 is complete - I've implemented and validated the blocked coordinate ascent baseline against analytical posteriors for simple test cases. The variational updates use the blocking strategy from Dr. Holmes' research code (updating parameter groups rather than individual scalars), which I've translated from R to Python and verified numerically.

For Phase 2 (weeks 5-7), I need to:
1. Derive the ELBO gradient analytically with respect to all variational parameters (my own derivation)
2. Implement gradient ascent with backtracking line search (my implementation)
3. Derive the ELBO Hessian for Newton's method (my own derivation)
4. Implement Newton's method with appropriate safeguards (my implementation)
5. Implement BFGS using gradient history (my implementation)

Phase 3 (weeks 8-10) is systematic comparison. I'll design an experimental framework with multiple random datasets (varying n from 50 to 500, p from 2 to 10), multiple random initialisations per method to assess robustness, and track several performance metrics:

- **Convergence speed**: Iterations to convergence, wall-clock time, gradient/Hessian evaluations
- **Solution quality**: Final ELBO value, distance to analytical posterior (when available)
- **Posterior calibration**: Coverage probabilities (do 95% credible intervals contain true parameters 95% of the time?), posterior variance compared to MCMC baseline
- **Robustness**: Success rate across different initialisations, sensitivity to convergence tolerance

This comparison framework will show which methods are most efficient for VI problems and under what conditions each method excels. For example, I expect Newton's method to win on iteration count but lose on wall-clock time for small problems, whilst BFGS should show the best overall balance.

If everything goes well, Phase 4 (weeks 10-11) would be implementing the penalty method with minimum variance constraints and comparing against unconstrained methods.

### Challenges I'm Expecting

The Hessian computation worries me - it may be complex to derive and expensive to compute/invert. My plan is to start with small problems and consider a block-diagonal approximation if the full Hessian is too expensive.

Newton's method may produce non-positive-definite Hessians away from the optimum. I'll add a regularisation term and fall back to the gradient direction if needed.

For the line search, I'll need to cache intermediate computations since the backtracking search requires multiple ELBO evaluations. Will use Wolfe conditions appropriately.

Finally, different methods need different convergence criteria for a fair comparison. I'll track multiple metrics: gradient norm, ELBO change, and relative parameter change.

---

## 4. Progress to Date

### What's Done So Far

I've completed the initial problem analysis and literature review, implemented the blocked coordinate ascent baseline in Python (using the parameter blocking strategy from Dr. John Holmes' in my summer 2025 research work), and validated it against analytical posteriors. The project proposal has been written and approved by the professor, with the scope adjusted to focus on demonstrating optimisation methods rather than trying to solve the under-dispersion problem completely (which would be too ambitious for this course).

Currently working on: ELBO gradient derivation (analytical derivation is complete, now implementing it in code). Still to do: alternative optimiser implementations and the experimental comparison framework.

### Baseline Results: Coordinate Ascent VI

For the baseline tests, I'm using simple Bayesian linear regression: n=100 observations with p=3 predictors, model is $y = X\beta + \epsilon$ where $\epsilon \sim N(0, \tau_e^{-1})$, with flat (improper) priors on $\beta$ and $\tau_e$.

CAVI converges in about 10-15 iterations using convergence criterion $\max|\phi^{(t)} - \phi^{(t-1)}| / |\phi^{(t)}| < 10^{-5}$. Final ELBO varies by problem but is tracked for each run. The posterior means match least squares estimates (which is reassuring), though the posterior variances are smaller than the MCMC baseline - this is the expected under-dispersion.

What I've noticed: CAVI is stable and monotonically increases ELBO at each iteration. Convergence is relatively fast for this simple conjugate model. It provides a solid baseline for comparison.

### Initial Gradient Ascent Experiments

Status: Gradient computation implemented, initial testing underway.

So far the ELBO gradient can be computed analytically (I've derived the expressions), and numerical gradient checking confirms the analytical derivatives are correct. Initial tests show that gradient ascent finds a similar optimum to CAVI. Convergence appears comparable in terms of iterations, but with fewer objective evaluations per iteration since we're not cycling through parameters.

### Development Setup

I'm using Python 3.12.3 with a virtual environment (`.venv` in the workspace root). Key packages are NumPy and SciPy (particularly scipy.stats and scipy.special). For report compilation I have MiKTeX 25.12 with XeLaTeX. VS Code extensions: Python, Pylance, LaTeX Workshop, and Markdown Preview Enhanced.

### Code Organisation

Current workspace structure:

```
ENEL445/
├── python/
│   ├── vb_algorithms_py.py    # Baseline CAVI (300 lines)
│   │                          # SimpleLinearVB + SimpleLinearGibbs classes
│   ├── vb_utils_py.py         # Utility functions
│   └── vb_optimizers.py       # NEW: Alternative optimisers (planned)
│                              # Will contain: GradientAscentVB, NewtonVB, BFGSVB
├── contents/                  # Course MATLAB and Python files
├── reference/
│   ├── project_jeremy/        # Power Systems project (8 screenshots)
│   ├── project_fdoa_geolocation/  # FDOA project (7 screenshots)
│   └── Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf
├── scripts/                   # Utility scripts
├── report/
│   └── progress_report/       # This document
└── project.proposal/          # LaTeX proposal
```

**Currently implemented:** `vb_algorithms_py.py` has the baseline CAVI with coordinate ascent (`SimpleLinearVB.fit()` method for main optimisation loop, `compute_elbo()` for objective evaluation), plus `SimpleLinearGibbs` for MCMC validation. `vb_utils_py.py` has support utilities.

**In development:** ELBO gradient computation (analytical derivation done, coding it up now), gradient ascent with line search, numerical gradient verification.

**Planned:** Newton's method with Hessian computation, BFGS quasi-Newton, penalty method for constrained optimisation, and the experimental comparison framework.

---

## 5. Next Steps

### This Week (Week 5-6)

By the progress report due date (20 Mar): Finish this report, finalise gradient ascent implementation with line search, run initial comparison between CAVI and Gradient Ascent, and document the gradient derivation properly.

Week 6: Derive the ELBO Hessian analytically, implement Newton's method with safeguards (for when Hessian isn't positive definite), and begin BFGS implementation.

### Weeks 7-10

Weeks 7-8: Finish all four unconstrained optimisers, implement robust convergence monitoring (need to make sure I'm comparing fairly), and design the experimental comparison framework.

Week 9: Run methods on multiple problems with varying n and p, generate convergence plots, compile performance tables, assess posterior calibration.

Week 10: Analyse results and identify patterns, document when each method works best, begin drafting final report. If there's time, attempt the penalty method implementation.

### Timeline

Approximate timeline to final report:
- Week 5: Progress report submission, gradient ascent completion (in progress)
- Week 6: Newton's method implementation (planned)
- Week 7: BFGS implementation (planned)  
- Week 8: Experimental framework, initial comparisons (planned)
- Week 9: Comprehensive experiments and results (planned)
- Week 10: Analysis, constrained method if time permits, draft report (planned)
- Week 11: Presentation preparation, final experiments (planned)
- Week 12: Final report submission (planned)

---

## 6. Connection to Course Material

This project applies optimisation techniques from ENEL445 directly. From Chapter 4 (Unconstrained Optimisation), I'm using gradient descent and line search methods, Newton's method and second-order optimisation, quasi-Newton methods (BFGS), and will need to think carefully about convergence analysis and stopping criteria. From Chapter 5 (Constrained Optimisation), the penalty methods for enforcing constraints will be relevant if I get to that part, and possibly augmented Lagrangian formulation as a stretch goal. Chapter 3 (Numerical Methods) is relevant for numerical gradient verification and thinking about the trade-offs between solution accuracy vs computational cost.

The VI problem provides a good realistic optimisation challenge where these methods can be compared systematically. It should demonstrate practical understanding of the course techniques whilst also being relevant to real statistical problems.

---

## 7. References

1. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer. Chapter 10: Approximate Inference. (Available in workspace: `reference/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf`)

2. Blei, D. M., Kucukelbir, A., & McAuliffe, J. D. (2017). Variational Inference: A Review for Statisticians. *Journal of the American Statistical Association*, 112(518), 859-877.

3. Martins, J. R. R. A., & Ning, A. (2021). *Engineering Design Optimisation*. Cambridge University Press. Chapters 4-5. (ENEL445 course textbook)

4. Nocedal, J., & Wright, S. J. (2006). *Numerical Optimisation* (2nd ed.). Springer. Chapters 2-3, 6.

5. Gelman, A., et al. (2013). *Bayesian Data Analysis* (3rd ed.). Chapman & Hall/CRC. Chapters 11-13.

Course materials: ENEL445 lecture notes (Terms 1 & 2) in `contents/` folder, standard project specifications in `reference/project_jeremy/` and `reference/project_fdoa_geolocation/`, MATLAB reference implementations in `contents/` (BFGS_Bisection.m, Bisection.m, Bound.m).

---

## Appendix A: ELBO Gradient Derivation (Summary)

For Bayesian linear regression with Normal-Gamma variational family:

$$q(\beta, \tau_e) = \mathcal{N}(\beta | \mu_\beta, \Sigma_\beta) \cdot \text{Gamma}(\tau_e | a_e, b_e)$$

The ELBO decomposes as:
$$\text{ELBO} = \mathbb{E}_q[\log p(y|\beta, \tau_e)] + \mathbb{E}_q[\log p(\beta)] + \mathbb{E}_q[\log p(\tau_e)] - \mathbb{E}_q[\log q(\beta)] - \mathbb{E}_q[\log q(\tau_e)]$$

Gradients with respect to variational parameters:
- $\nabla_{\mu_\beta} \text{ELBO} = \mathbb{E}[\tau_e] X^T(y - X\mu_\beta) + \ldots$
- $\nabla_{\Sigma_\beta} \text{ELBO}$ involves trace terms
- $\nabla_{a_e} \text{ELBO}$ involves digamma functions
- $\nabla_{b_e} \text{ELBO}$ involves moment matching

*(Full derivation available in code documentation)*

---

**Notes:**
- This report focuses on demonstrating understanding of optimisation methods
- The VI framework serves as the problem domain (analogous to power systems or FDOA geolocation in standard projects)
- Code emphasises algorithm implementation and comparison
- Final report will include comprehensive convergence analysis and method comparison

---

## Development Notes

**Workspace Setup:** 25 Feb 2026  
**Progress Report Created:** 12 Mar 2026  
**Python Environment:** Virtual environment at `.venv` with scipy, numpy, and optimisation dependencies  
**Documentation Tools:** Markdown with KaTeX math rendering, LaTeX Workshop for final report compilation

**Key Workspace Resources:**
- Blocked coordinate ascent baseline (parameter blocking strategy from Dr. John Holmes' summer 2025 research, implementation and Python translation my own work)
- Course lecture materials covering unconstrained/constrained optimisation methods
- Reference projects demonstrating expected code structure and deliverables
- Bishop's PRML textbook for VI theory and implementation details
