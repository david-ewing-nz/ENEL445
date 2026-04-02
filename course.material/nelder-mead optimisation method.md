Technical Specification & Repo Guide: Gradient-Free Optimisation

This document serves as a machine-readable technical specification and repository guideline for zeroth-order (gradient-free) optimisation algorithms. It focuses on the mathematical foundations and implementation logic required for engineering-grade software, specifically highlighting the Nelder-Mead Simplex method.

1. Repository Architecture & Project Structure

The project is structured to separate core algorithmic logic from utility metrics, benchmarking suites, and documentation. This modularity ensures the repository is suitable for automated testing and machine interpretability.

.
├── docs/                      # Technical specifications and mathematical derivations
├── src/                       # Core algorithm implementations
│   ├── algorithms/            # Nelder-Mead, GPS, DIRECT implementations
│   └── utils/                 # Convergence metrics (Simplex size, function variance)
├── tests/                     # Unit tests for algorithmic components
├── benchmarks/                
│   └── virtual_library/       # Virtual Library of Simulation Experiments (Rosenbrock, Ackley, etc.)
├── examples/                  # Usage scripts for 1D and 2D design spaces
└── requirements.txt           # Dependency references (SciPy, NumPy)


* /docs: Formal documentation of theoretical constraints, including the "No Free Lunch Theorem."
* /src: Houses the primary IF-THEN-ELSE logic flows for the optimisation engines.
* /src/utils: Contains the mathematical implementations of termination criteria like \Delta_x and \Delta_f.
* /benchmarks/virtual_library: A curated collection of standard test functions used to evaluate performance across various topologies.
* /tests: Automated verification scripts to ensure code changes do not break convergence properties.

2. Optimisation Algorithm Classification Matrix

The following matrix classifies gradient-free methods by their search properties and evaluation strategies.

Algorithm	Search Type	Methodology	Evaluation Type	Stochasticity
Nelder-Mead	Local	Heuristic	Direct	Deterministic
GPS	Global	Mathematical	Direct	Deterministic
MADS	Global	Mathematical	Direct	Stochastic
Trust Region	Local	Mathematical	Surrogate	Deterministic
Implicit Filtering	Local	Mathematical	Surrogate	Deterministic
DIRECT	Global	Mathematical	Direct	Deterministic
MCS	Global	Mathematical	Direct	Deterministic
EGO	Global	Mathematical	Surrogate	Deterministic
Hit and Run	Global	Heuristic	Direct	Stochastic
Evolutionary	Global	Heuristic	Direct	Stochastic
Simulated Annealing	Global	Heuristic	Direct	Stochastic

Note on Methodology: Surrogate-based methods (EGO, Trust Region, Implicit Filtering) are specifically architected for scenarios where function evaluations are computationally expensive, as they build internal models to approximate the objective function.

3. Technical Motivation & Scope

Baseline: Exhaustive Search (Brute Force)

Exhaustive search discretizes the search space into a grid and systematically checks every point. While it is easy to implement and embarrassingly parallelizable, it suffers from the "Curse of Dimensionality." Performance scales exponentially (O(e^n) or worse) with the number of design variables. For example, a Traveling Salesperson Problem (TSP) with 20 cities results in (20-1)! \approx 1.21 \times 10^{17} possibilities, rendering exhaustive search impractical for high-dimensional engineering problems.

Preferred Conditions for Zeroth-Order Methods

Gradient-free algorithms are preferred when the Karush–Kuhn–Tucker (KKT) conditions cannot be derived due to a failure of C^1 and C^2 continuity requirements. Specific conditions include:

* Non-Smoothness: The objective function is C^0 continuous but lacks the smoothness (gradients) required for first-order methods.
* Numerical Noise: High-frequency noise makes derivative approximations (e.g., Finite Difference) unreliable.
* Discontinuities: The design space contains discrete jumps.
* Derivative Complexity: Gradients are either analytically unavailable or too costly to compute.

Constraints

* No Free Lunch (NFL) Theorem: Per Wolpert & Macready (1997), all optimisation algorithms perform equally when averaged over all possible problems. Improvement in performance on one class of problems is strictly offset by performance on another, necessitating problem-specific testing.

4. Nelder-Mead Mathematical Specification

The Nelder-Mead method is a heuristic search using a simplex of n+1 points in an n-dimensional space (e.g., a triangle in 2D or a tetrahedron in 3D).

Initialisation and Ordering

At each iteration k, the objective f is evaluated for every point, and points must be ordered such that: f(x^{(0)}) \leq f(x^{(1)}) \leq \dots \leq f(x^{(n)})

Centroid Calculation

The centroid x_c is calculated using the n best points, excluding the worst point x^{(n)}: x_c = \frac{1}{n} \sum_{i=0}^{n-1} x^{(i)}

Standard Operations

Transformation of the simplex is governed by the update rule x = x_c + \alpha(x_c - x^{(n)}), using the following standard constants:

* Reflection (\alpha = 1): x_r = x_c + 1(x_c - x^{(n)})
* Expansion (\alpha = 2): x_e = x_c + 2(x_c - x^{(n)})
* Outside Contraction (\alpha = 0.5): x_{oc} = x_c + 0.5(x_c - x^{(n)})
* Inside Contraction (\alpha = -0.5): x_{ic} = x_c - 0.5(x_c - x^{(n)})

Shrink Operation

If no transformation improves the worst point, the simplex is reduced towards the best point x^{(0)} using the constant \gamma = 0.5: x^{(i)} = x^{(0)} + 0.5(x^{(i)} - x^{(0)}) \quad \text{for } i = 1, \dots, n

5. Implementation Logic Flow (GitHub Copilot Directive)

The following structured logic defines one iteration of the algorithm to ensure deterministic code generation.

# 1. ORDER POINTS
# Ensure points are sorted: f(x[0]) <= f(x[1]) <= ... <= f(x[n])

# 2. CALCULATE CENTROID (xc)
# Exclude the worst point x[n]
xc = (1/n) * sum(x[i] for i in 0 to n-1)

# 3. ATTEMPT REFLECTION (xr)
xr = xc + 1 * (xc - x[n])

IF f(xr) < f(x[0]):
    # 4. ATTEMPT EXPANSION (xe)
    xe = xc + 2 * (xc - x[n])
    IF f(xe) < f(xr):
        x[n] = xe
    ELSE:
        x[n] = xr
ELIF f(x[0]) <= f(xr) < f(x[n-1]):
    # Accept Reflection
    x[n] = xr
ELIF f(x[n-1]) <= f(xr) < f(x[n]):
    # 5. ATTEMPT OUTSIDE CONTRACTION (xoc)
    xoc = xc + 0.5 * (xc - x[n])
    IF f(xoc) <= f(xr):
        x[n] = xoc
    ELSE:
        # EXECUTE SHRINK
        FOR i IN 1..n:
            x[i] = x[0] + 0.5 * (x[i] - x[0])
ELSE: # Case: f(xr) >= f(x[n])
    # 6. ATTEMPT INSIDE CONTRACTION (xic)
    xic = xc - 0.5 * (xc - x[n])
    IF f(xic) < f(x[n]):
        x[n] = xic
    ELSE:
        # EXECUTE SHRINK
        FOR i IN 1..n:
            x[i] = x[0] + 0.5 * (x[i] - x[0])


6. Convergence Metrics & Termination Criteria

Convergence must be monitored via the stability of the design space and the objective function values.

* Simplex Size (\Delta_x): The sum of Euclidean distances between the best points and the worst point. \Delta_x = \sum_{i=0}^{n-1} \|x^{(i)} - x^{(n)}\|
* Standard Deviation of Function Values (\Delta_f): Measure of the "flatness" of the simplex in the objective space. \Delta_f = \sqrt{\frac{\sum_{i=0}^n (f^{(i)} - \bar{f})^2}{n+1}}
* Value Stability: The absolute difference between the best and worst objective values. \Delta_{best-worst} = f(x^{(n)}) - f(x^{(0)})

Validation Warning: McKinnon (1996) demonstrated that Nelder-Mead may converge to non-stationary points. All results should be verified against problem-specific physical constraints.

7. Standard Benchmarking Functions

Primary Benchmark: Rosenbrock (Banana) Function

The Rosenbrock function tests the algorithm's ability to navigate narrow, parabolic valleys toward the optimum. f(\mathbf{x}) = \sum_{i=1}^{d-1} [100(x_{i+1} - x_i^2)^2 + (x_i - 1)^2]

* Global Optimum: f(\mathbf{x}^*) = 0 at \mathbf{x}^* = (1, \dots, 1).

Secondary Benchmarks: Multimodal Topologies

For testing global search capabilities and resistance to local minima, use:

* Ackley Function: Characterized by a nearly flat outer region and a deep central hole.
* Rastrigin Function: A highly multimodal function with many regularly distributed local minima.

8. Development & Dependency References

* Baseline API: scipy.optimize.minimize(method='Nelder-Mead') is the gold standard for validation. Implementations should match the disp, maxiter, and maxfev interface.
* Academic References:
  * Nelder, J. A., & Mead, R. (1965). "A simplex method for function minimization." The Computer Journal.
  * Wolpert, D. H., & Macready, W. G. (1997). "No free lunch theorems for optimization." IEEE Transactions on Evolutionary Computation.
  * McKinnon, K. I. M. (1996). "Convergence of the Nelder-Mead simplex method to a non-stationary point." SIAM Journal on Optimization.
