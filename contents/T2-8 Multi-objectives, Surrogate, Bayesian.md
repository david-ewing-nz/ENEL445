# T2-8 Multi-objectives, Surrogate, Bayesian

*Converted from PDF: T2-8 Multi-objectives, Surrogate, Bayesian.pdf*

---

## Page 1

Multi-objectives and 
Surrogate-Based 
Optimisation
ENEL445 Applied Engineering Optimisation
2025

![Page 1](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_001.png)

---

## Page 2

Outline
●Multi-Objective Optimisation
●Pareto Optimality
●Surrogate-Based Optimisation
●Maximum Likelihood

![Page 2](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_002.png)

---

## Page 3

Outline
●Multi-Objective Optimisation
●Pareto Optimality
●Surrogate-Based Optimisation
●Maximum Likelihood

![Page 3](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_003.png)

---

## Page 4

Speak UP_
STAND TOGE TFER
SToP BULLYING
KORERO MAI ; KORERO ATU, MAURI TU, MAURI ORA

![Page 4](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_004.png)

---

## Page 5

Multi-objective Optimisation
●
Multi-objective optimisation problems - Problems whose 
formulations have more than one objective function:
■
Risk versus reward
■
Profit versus environmental impact
■
Acquisition cost versus operating cost
■
Drag versus noise
●
A common technique when presented with multiple 
objectives is to assign weights to the various objectives and 
combine them into a single objective.
●
More generally, multi-objective optimisation helps explore the 
trade-offs between different metrics.

![Page 5](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_005.png)

---

## Page 6

●
Example: In designing an aircraft, we may decide that 
maximising fuel tank volume and minimising weight are 
important. However, these metrics compete with each other 
and cannot be optimised simultaneously.
●
Instead, we may conclude that maximising range (the 
distance the aircraft can fly) is the underlying metric that 
matters most for our application and appropriately balances 
the trade-offs between weight and fuel.
●
Or perhaps maximising range is not the right metric. Range 
may be important, but only insofar as we reach some 
threshold. Increasing the range does not increase the value 
because the range is a constraint. The underlying objective 
in this scenario may be some other metric, such as operating 
costs.
Multi-objective Optimisation

![Page 6](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_006.png)

---

## Page 7

Multi-objective Optimisation
●
Multiobjective optimisation can quantify the trade-off between 
different objectives.
●
Multiobjective optimisation provides a “family” of designs 
rather than a single design.
●
For some problems, the underlying objective is either 
unknown or too difficult to compute.

![Page 7](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_007.png)

---

## Page 8

Multi-objective Optimisation
●
The objective function in a multi-objective optimisation can 
be expressed as
●
This multi-objective formulation may require trade-offs 
because, beyond some point, further reduction in one 
objective can only be achieved by increasing one or more of 
the other objectives.
●
With multiple objectives, we have to reconsider what it 
means for a point to be optimal.

![Page 8](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_008.png)

---

## Page 9

Outline
●Multi-Objective Optimisation
●Pareto Optimality and Finding the Pareto Front
●Surrogate-Based Optimisation
●Maximum Likelihood

![Page 9](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_009.png)

---

## Page 10

Pareto Optimal
●
One design is said to dominate another design if it is 
superior in all objectives (design A dominates any design in 
the shaded rectangle).
●
A point is said to be nondominated if none of the other 
evaluated points dominate it

![Page 10](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_010.png)

---

## Page 11

●
If a point is nondominated by any point in the entire domain, 
then that point is called Pareto optimal.
●
This does not imply that this point dominates all other points; 
it simply means no other point dominates it.
●
The set of all Pareto optimal points is called the Pareto set. 
Pareto Optimal

![Page 11](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_011.png)

---

## Page 12

Pareto Front
●
The Pareto set refers to the vector of points 𝑥∗, whereas the 
Pareto front refers to the vector of functions 𝑓(𝑥∗).

![Page 12](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_012.png)

---

## Page 13

●
The two objectives are maximising power production and 
minimising noise.
●
The Pareto front tells us how much power we have to 
sacrifice for a given reduction in noise. If the slope is steep, 
as is the case in the figure below, we can see that a small 
sacrifice in power production can be exchanged for 
significantly reduced noise. 
Example - Wind Farm Optimisation 
●
Understanding the magnitude 
of these trade-off sensitivities 
helps make high-level design 
decisions.

![Page 13](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_013.png)

---

## Page 14

Finding the Pareto Front
●
Various solution methods exist for solving multiobjective 
optimisation problems:
■
Weighted-sum method
■
Epsilon-constraint method
■
Normal Boundary Intersection (NBI) method 
■
Evolutionary algorithms

![Page 14](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_014.png)

---

## Page 15

Weighted Sum Method
●
Combine all of the objectives into a single objective using a 
weighted sum:
where 𝑛𝑓 is the number of objectives, and the weights are 
usually normalised such that

![Page 15](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_015.png)

---

## Page 16

●
Two objectives example:
●
At the extremes 𝑤 = 0 and 𝑤 = 1, the optimisation returns the 
designs that optimise one objective while ignoring the other.
Weighted Sum Method

![Page 16](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_016.png)

---

## Page 17

●
Advantage: 
●
Drawbacks: 
Weighted Sum Method
■
Uniform spacing in 𝑤 leads to non-uniform spacing along 
the Pareto set.
■
Not apparent which values of 𝑤 should be used to sweep 
out the Pareto set evenly
■
This method can only return points on the convex portion of 
the Pareto front.
■
It is easy to use

![Page 17](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_017.png)

---

## Page 18

Epsilon-Constraint Method
●
Choose an 𝜀 for each constraint.
●
Minimise one objective while setting all other objectives as 
additional constraints.
●
Repeat this procedure for different values of 𝜀𝑗

![Page 18](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_018.png)

---

## Page 19

●
Reveals the non-convex portions of the Pareto front.
●
Like the weighted-sum method, a uniform spacing in 𝜀 does 
not generally yield a uniform spacing of the Pareto front 
(though it is usually much better spaced than weighted-sum) 
therefore it might still be inefficient, particularly with more 
than two objectives.
Epsilon-Constraint Method

![Page 19](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_019.png)

---

## Page 20

Normal Boundary Intersection
●
The NBI method is designed to address the issue 
of nonuniform spacing along the Pareto front.
●
First find the extremes of the Pareto set; in other words, 
minimise the objectives one at a time.
Das & Dennis, “Normal-boundary 
intersection: A new method for 
generating the Pareto surface in 
nonlinear multicriteria optimization 
problems”, 1998.
●
Construct a plane that passes 
through the extreme points.
●
Space points along this plane.
●
Starting from those points, 
solve optimisation problems 
that search along directions 
normal to this plane.

![Page 20](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_020.png)

---

## Page 21

●
Mathematically, we start by determining the anchor points, 
which are just single-objective optimisation problems.
●
From the anchor points, we define the utopia point - every 
objective reaches its minimum simultaneously.
Normal Boundary Intersection

![Page 21](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_021.png)

---

## Page 22

●
We search along a direction perpendicular to the line defined 
by the anchor points. We seek to find the point along this 
direction that is the farthest away from the anchor points line 
(a maximisation problem), with the constraint that the point is 
consistent with the objective functions:
●
The resulting optimal point found along this direction is a 
point on the Pareto front.
●
We then repeat this process for another set of weighting 
parameters in 𝑏.
Normal Boundary Intersection

![Page 22](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_022.png)

---

## Page 23

●
The idea is that even spacing along this plane is more likely 
to lead to even spacing along the Pareto front.
●
Yields a more uniformly spaced Pareto front
●
Desirable for computational efficiency, albeit at the cost of a 
more complex methodology.
●
For most multiobjective design problems, additional 
complexity beyond the NBI method is unnecessary. 
However, even this method can still have deficiencies for 
problems with unusual Pareto fronts, and new methods 
continue to be developed [1-3]. A more recent improvement 
performs an even more efficient generation of the Pareto 
front by avoiding regions of the Pareto front where minimal 
trade-offs occur [3].
Normal Boundary Intersection

![Page 23](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_023.png)

---

## Page 24

Normal Boundary Intersection
[1] Ismail-Yahaya and Messac, “Effective generation of the Pareto 
frontier using the normal constraint method”, 2002.
[2] Messac and Mattson, “Normal constraint method with guarantee 
of even representation of complete Pareto frontier”, 2004.
[3] Hancock and Mattson, “The smart normal constraint method for 
directly generating a smart Pareto set”, 2013.

![Page 24](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_024.png)

---

## Page 25

Evolutionary Algorithms
●
A GA is amenable to an extension that can handle multiple 
objectives because it keeps track of a large population of 
designs at each iteration.
●
If we plot two objective functions for a given population of a 
GA iteration, we get something shown in the figure below.
●
The points represent the 
current population, and the 
highlighted points in the 
lower left are the current 
nondominated set. As the 
optimisation progresses, the 
nondominated set 
converges toward the actual 
Pareto front.

![Page 25](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_025.png)

---

## Page 26

Evolutionary Algorithms
●
Elitist Nondominated Sorting Genetic Algorithm (NSGA-II)
●
In addition to determining the 
nondominated set, we want 
to rank all members by their 
dominance depth, which is 
also called nondominated 
sorting. In this approach, all 
nondominated points in the 
population (i.e., the current 
approximation of the Pareto 
set) are given a rank of 1. 
Those points are then 
removed from the set, and 
the next set of nondominated 
points is given a rank of 2, 
and so on.

![Page 26](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_026.png)

---

## Page 27

Evolutionary Algorithms
●
The main advantage of this multiobjective approach is that if 
an evolutionary algorithm is appropriate for solving a given 
single-objective problem, then the extra information needed 
for a multiobjective problem is already there, and solving the 
multiobjective problem does not incur much additional 
computational cost.
●
However, solving multiple gradient-based problems may be 
more efficient than solving one gradient-free problem, 
especially for problems with a large number of design 
variables.

![Page 27](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_027.png)

---

## Page 28

Multi-objective Optimisation - Summary
●
Multiobjective optimisation is particularly useful in quantifying 
trade-off sensitivities between critical metrics. It is also useful 
when we seek a family of potential solutions rather than a 
single solution.
●
Some scenarios where a family of solutions might be 
preferred include when the models used in optimisation are 
low fidelity and higher-fidelity design tools will be applied or 
when more investigation is needed.
●
A multiobjective approach can produce candidate solutions 
for later refinement.

![Page 28](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_028.png)

---

## Page 29

Outline
●Multi-Objective Optimisation
●Pareto Optimality and Finding the Pareto Front
●Surrogate-Based Optimisation
●Maximum Likelihood

![Page 29](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_029.png)

---

## Page 30

Surrogate Models
●
A surrogate is an approximate model that represents a curve 
fit to some underlying data. Also known as:
■
Response surface
■
Metamodel
●
The goal of a surrogate model is to build a model that is much 
faster to compute than the original function, but still retains 
sufficient accuracy away from known data points.
●
Surrogate-based optimisation (SBO) performs optimisation 
using the surrogate model.
●
Instead of aiming for a globally accurate surrogate, SBO just 
needs the surrogate model to be accurate enough to lead the 
optimiser to the true optimum.

![Page 30](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_030.png)

---

## Page 31

Figure from “Surrogate modelling for the forecast of Seveso-type atmospheric pollutant dispersion”
https://www.researchgate.net/publication/360665374_Surrogate_modelling_for_the_forecast_of_Seveso-type_at
mospheric_pollutant_dispersion?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6Il9kaXJlY3QiLCJwYWdlIjoiX2RpcmV
jdCJ9fQ

![Page 31](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_031.png)

---

## Page 32

Why Surrogates
●
This approach is often used when the function is expensive 
and the number of evaluations needed to build a sufficiently 
accurate surrogate model is less than that needed to optimise 
the original model directly.
●
Surrogate modeling can be effective in handling noisy models 
because they create a smooth representation of noisy data.
●
One scenario that leads to both expensive evaluation and 
noisy output is experimental data.
●
Surrogate models are also helpful when we want to 
understand the design space. By constructing a continuous 
model over discrete data, we obtain functional relationships 
that can be visualised more effectively.

![Page 32](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_032.png)

---

## Page 33

Why Surrogates
●
A lower-fidelity surrogate can guide the optimiser to 
promising regions of the larger design space.
●
Used in conjunction with other algorithms like GPS or 
Nelder-Mead.
●
When multiple sources of data are available, surrogate 
models can fuse the data to build a single model. The data 
could come from numerical models with different levels of 
fidelity or experimental data. For example, surrogate 
models can calibrate numerical model data using 
experimental data. This is helpful because experimental 
data is usually much more scarce than numerical data. The 
same reasoning applies to low- vs high-fidelity numerical 
data.

![Page 33](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_033.png)

---

## Page 34

Downsides
●
One potential issue with surrogate models is the curse of 
dimensionality, which refers to poor scalability with the 
number of design variables. The larger the number of 
design variables, the more model evaluations are needed 
to construct a surrogate model that is accurate enough. 
Therefore, the reasons for using surrogate models cited 
earlier might not be enough if the optimisation problem has 
a large number of design variables.

![Page 34](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_034.png)

---

## Page 35

Surrogate Modelling Example
●
When performing trajectory optimisation of an aircraft, we 
need to evaluate the lift and drag of the aircraft at each 
point of the trajectory. 
●
This typically requires many points, and computing the lift 
and drag at each point might be prohibitive. Therefore, it 
might be worthwhile to use surrogate models that predict 
the lift and drag as functions of the angle of attack. 
●
If the optimisation design variables 
include parameters that change the 
lift and drag characteristics, such as 
the wing shape, then the surrogate 
model needs to be rebuilt at every 
optimisation iteration.

![Page 35](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_035.png)

---

## Page 36

Surrogate Process
●
Choose initial points to evaluate 
the function or conduct 
experiments. These points are 
sometimes referred to as training 
data. Next, we build a surrogate 
model from the sampled points. 
We can then perform optimisation 
by querying the surrogate model.
●
Based on the results of the 
optimisation, we include 
additional points in the sample 
and reconstruct the surrogate 
(infill). We repeat this process 
until some convergence criterion 
or a maximum number of 
iterations is reached.

![Page 36](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_036.png)

---

## Page 37

Surrogate
Sample
Process
Construct
surrogate
Perform
optimization
No
Converged?
Infill
Yes
Done

![Page 37](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_037.png)

---

## Page 38

Sampling
●
Full factorial sampling - Not efficient because it scales 
exponentially with the number of input variables.
●
Latin hypercube sampling
●
Low-Discrepancy Sequences
■
Halton Sequence
■
Hammersley Sequence 
Hammersley sequence with base 2 
for the 𝑥2-axis.

![Page 38](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_038.png)

---

## Page 39

Sampling
●
Sampling strategies on the previous slide are useful in 
many other applications: 
■
Initializing a genetic algorithm
■
Particle swarm optimization
■
Multistart gradient-based algorithm
■
Choosing the points to run in a Monte Carlo 
simulation
●
Because the function behaviour at each sample is 
independent, we can efficiently parallelise the evaluation of 
the functions.

![Page 39](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_039.png)

---

## Page 40

Surrogate
Sample
Process
Construct
surrogate
Perform
optimization
No
Converged?
Infill
Yes
Done

![Page 40](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_040.png)

---

## Page 41

Constructing Surrogates
●
Regression models do not try to match the training data 
points exactly; instead, they minimize the error between a 
smooth trend function and the training data. Useful when 
the data are noisy.
●
Interpolation builds a function that exactly matches the 
provided training data. Useful when the data are highly 
multimodal (and not noisy). This is because regression may 
smooth over variations that are actually physical.

![Page 41](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_041.png)

---

## Page 42

Linear Least Squares Regression 
●
A linear regression model does not mean that the surrogate 
is linear in the input variables but rather that the model is 
linear in its coefficients (i.e., linear in the parameters we 
are estimating). For example:
●
In general 
where 𝑤 is a vector of weights, and 𝜓 is a vector of basis 
functions.

![Page 42](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_042.png)

---

## Page 43

Basis 1 - Polynomial 
●
Consider a quadratic fit: 𝑓(𝑥) = 𝑎𝑥2 + 𝑏𝑥 + 𝑐. This can be 
posed as a linear regression model where the coefficients 
we wish to estimate are 𝑤 = [𝑎, 𝑏, 𝑐] and the basis functions 
are 𝜓 = [𝑥2, 𝑥, 1]. 
●
For a 𝑛-dimensional polynomial model, the basis functions 
would be polynomials with terms combining the 
dependencies on all input variables 𝑥 up to the 𝑛-th order. 
For example, for two input variables up to second order, the 
basis functions would be  
and 𝑤 would consist of six coefficients. 
●
In general, the basis functions can be any set of functions. 
It is usually desirable for these functions to be orthogonal.

![Page 43](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_043.png)

---

## Page 44

Basis 2 - Radial Basis Functions (RBF) 
●
RBFs are functions whose values depend only on the distance 
between the input and some fixed point.
●
Captures the idea that ability to predict function behavior is 
related to how close we are to known function values.

![Page 44](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_044.png)

---

## Page 45

https://www.cs.jhu.edu/~misha/Fall05/Papers/carr01.pdf
Basis 2 - Radial Basis Functions (RBF)

![Page 45](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_045.png)

---

## Page 46

http://www.aranz.co.nz/
Basis 2 - Radial Basis Functions (RBF)

![Page 46](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_046.png)

---

## Page 47

Aside: Quantum Harmonic Potential

![Page 47](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_047.png)

---

## Page 48

Aside: Quantum Harmonic Potential 
●
Wavepacket evolving in time in the harmonic well
https://github.com/marl0ny/QM-Simulator-1D

![Page 48](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_048.png)

---

## Page 49

Least Squares Solution 
●
We want to choose coefficients to minimise the error 
between our predicted function values f̂ and the actual 
function values 𝑓(𝑖)
●
The solution to this optimisation problem is called a least 
squares solution.

![Page 49](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_049.png)

---

## Page 50

Linear Case 
●
If the regression model is linear, we can simplify this 
objective and write the optimisation in matrix form as
●
Example:

![Page 50](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_050.png)

---

## Page 51

Linear Case 
●
The optimisation on the previous slide becomes a quadratic 
programming problem, with the solution:

![Page 51](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_051.png)

---

## Page 52

Nonlinear Case
●
A nonlinear least squares regression model means that 
the model is nonlinear in the parameters we are estimating. 
Example:
●
We still seek to minimise the sum of errors
where 𝑤 is a vector of parameters.
●
Use methods like Levenberg-Marquardt

![Page 52](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_052.png)

---

## Page 53

Regularisation 
●
A common variation is to use regularised least squares 
which adds a term in the objective:
●
The rationale is that we may want to accept a higher error 
in exchange for smaller values of the coefficients.
●
A related extension uses a second term of the form 
∥𝑤 − 𝑤0∥2. The idea is that we want a good fit, while 
maintaining parameters that are close to some known 
nominal values 𝑤0.
●
This approach is particularly beneficial if the data contain 
strong outliers or are particularly noisy.

![Page 53](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_053.png)

---

## Page 54

Regularisation 
●
Can rewrite the above as
●
This is of the same linear form as before (∥𝐴𝑤 − 𝑏∥2), so 
we can write
●
Also known as: 
■
Ridge regression
■
Tikhonov regularization

![Page 54](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_054.png)

---

## Page 55

Outline
●Multi-Objective Optimisation
●Pareto Optimality and Finding the Pareto Front
●Surrogate-Based Optimisation
●Maximum Likelihood

![Page 55](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_055.png)

---

## Page 56

●
It can be shown that min sum squared error = max likelihood 
under certain conditions 
Maximum Likelihood Interpretation

![Page 56](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_056.png)

---

## Page 57

*[Page appears blank or contains only images]*

![Page 57](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_057.png)

---

## Page 58

*[Page appears blank or contains only images]*

![Page 58](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_058.png)

---

## Page 59

Exercises
●
Look up all the terms and derivations that are new to 
you in this lecture and understand them.
●
Think of an optimisation situation when surrogates 
would be useful.
●
Think of another way to commute the Pareto front.
Thanks!

![Page 59](../course.material/figs/T2-8%20Multi-objectives%2C%20Surrogate%2C%20Bayesian/page_059.png)

---

