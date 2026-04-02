# Applied Engineering Optimisation - Constrained Optimisation

*Converted from PDF: Applied Engineering Optimisation - Constrained Optimisation.pdf*

---

## Page 1

Classification: In-Confidence
Nau mai, welcome to
Applied Engineering 
Optimisation
ENEL445


---

## Page 2

Classification: In-Confidence
Weeks 4+: Constrained 
optimisation
• This is a difficult topic.
• The course reader may be helpful, but please do 
attend the lectures and stop me and ask questions
if you are not following the lecture material.


---

## Page 3

Classification: In-Confidence
Topics
We will cover:
• Optimality conditions
• Equality constraints
• Inequality constraints
• KKT conditions
• Algorithms for solving constrained problems
• Penalty methods
• Sequential quadratic programming (SQP)
• Interior point
• Duality


---

## Page 4

Classification: In-Confidence
Which optimiser should I use?


---

## Page 5

Classification: In-Confidence
Constrained optimisation
• Most optimisation problems are constrained
• Most variables (and basically all physical variables) 
have limits, e.g. 
• if you are optimising the power system (something that 
happens every half hour in NZ), each generator and each 
line will have limits.
• if optimising an electrical appliance, there will be 
budget, dimension, power usage constraints, etc.


---

## Page 6

Classification: In-Confidence
Constrained optimisation


---

## Page 7

Classification: In-Confidence
Definition


---

## Page 8

Classification: In-Confidence
Equality constraints
Let’s start by considering the case where we only 
have equality constraints, i.e. no inequality 
constraints of any sort. 
Recap from week 3. A necessary condition for 
optimality was:
(for all p) i.e. in all directions the objective function 
does not improve.


---

## Page 9

Classification: In-Confidence
Equality constraints
What if we have equality constraints? It is now okay 
for the objective function to improve in some 
direction p so long as that direction p is not feasible, 
i.e. we cannot go there. 
So we need                              but only for feasible 
directions p, rather than for all p.


---

## Page 10

Classification: In-Confidence
How to find feasible directions
• Taylor-series:
• Assuming x is feasible, then 
• To remain feasible, 
• We can write this in matrix form using the Jacobian 
matrix


---

## Page 11

Classification: In-Confidence
Optimality conditions
• For 𝑥∗ to be a constrained optimum
• Now, ℎ𝑗𝑥= 0 is a hyper-plane in N space.
• So, if p is a feasible direction, so is –p. Thus
(                   greater than zero implies negativity when 
p is replaced by –p)


---

## Page 12

Classification: In-Confidence
Lagrange multipliers
• We now have two equations:
• The rows of       are gradients of the constraints, so 
the objective function gradient must be a linear 
combination of the gradients of the constraints.


---

## Page 13

Classification: In-Confidence
• In matrix form: 
• It is sometimes convenient to define the Lagrangian 
function
• Taking the gradient of this w.r.t. x and     yields the 
matrix conditions above, so we could try to find the 
critical point(s) of the Lagrangian via unconstrained 
optimisation – but not usually the best way. 
Lagrangian function


---

## Page 14

Classification: In-Confidence
Second-order conditions
• The conditions described are first-order (i.e. no 
second derivatives) and are necessary but not 
sufficient. 
• To make sure the point is a constrained minimum, 
we need to check the Hessian function (similar to 
unconstrained optimisation). 
• Recall that for unconstrained optimisation the 
Hessian had to be positive definite, i.e. 
>


---

## Page 15

Classification: In-Confidence
Second-order conditions
• As before, we only need to check directions p 
which are feasible.


---

## Page 16

Classification: In-Confidence
Example 5.2


---

## Page 17

Classification: In-Confidence
Example 5.3


---

## Page 18

Classification: In-Confidence
Inequality constraints


---

## Page 19

Classification: In-Confidence
Important terminology


---

## Page 20

Classification: In-Confidence
Optimality conditions
• As before, if x∗ is an optimum, any small enough 
feasible step p from the optimum must result in a 
function increase. Based on Taylor series 
expansion, we had the condition:
• To consider inequality constraints, we use 
linearization as before:


---

## Page 21

Classification: In-Confidence
Optimality conditions
• There are two possibilities for each constraint: 
whether the constraint is inactive                      or 
active                    .
• If a given constraint is inactive, we do not need to 
add any condition for it because we can take a step 
p in any direction and remain feasible as long as the 
step is small enough. 
• Thus, we only need to consider the active 
constraints for the optimality conditions.


---

## Page 22

Classification: In-Confidence
Active inequality constraints
• If constraint j is active                       then the nearby 
point                     is only feasible if                                          
for all constraints j that are active. 
• In matrix form:  
where the Jacobian matrix includes only the 
gradients of the active constraints. 
• We thus have two conditions


---

## Page 23

Classification: In-Confidence
• Farkas’ Lemma states that given this, one of two 
possibilities occur:
 
• In case 1, there is a feasible direction                                
in which we can descend 
• So, case 2 is our optimality condition. 
• See course reader or textbook for proof.
Farkas’ Lemma


---

## Page 24

Classification: In-Confidence
Lagrange multipliers
• Similar to the condition for equality constraints,
σ corresponds to the Langrange multipliers for the 
inequality constraints and carries the additional 
restriction that they are non-negative.


---

## Page 25

Classification: In-Confidence
Slackness
• As in the equality constrained case, we can construct a 
Lagrangian function whose stationary points are 
candidates for optimal points. 
• We need to include all inequality constraints in the 
optimality conditions because we do not know in 
advance which constraints are active.
• To represent inequality constraints in the Lagrangian, 
we replace them with the equality constraints defined 
by:
• where sj is called a slack variable.


---

## Page 26

Classification: In-Confidence
Lagrangian
• The Lagrangian including both equality and 
inequality constraints is then
where σ represents the Lagrange multipliers 
associated with the inequality constraints. We use ⊙ 
to represent the element-wise multiplication of s.


---

## Page 27

Classification: In-Confidence
KKT conditions
• Similar to the equality constrained case, we seek a 
stationary point for the Lagrangian, but now we 
have additional unknowns: the inequality Lagrange 
multipliers and the slack variables.
• Taking partial derivatives of the Lagrangian with 
respect to each set of unknowns and setting those 
derivatives to zero yields the first-order optimality 
conditions.


---

## Page 28

Classification: In-Confidence
KKT conditions


---

## Page 29

Classification: In-Confidence
KKT conditions
• In addition to the conditions for a stationary point 
of the Lagrangian, recall that we require the 
Lagrange multipliers for the active constraints to be 
nonnegative. Putting all these conditions together 
in matrix form, the first-order constrained 
optimality conditions are as follows:


---

## Page 30

Classification: In-Confidence
Second-order conditions
• As in the equality constrained case, these first-
order conditions are necessary but not sufficient. 
The second-order sufficient conditions require that 
the Hessian of the Lagrangian must be positive 
definite in all feasible directions, That is,


---

## Page 31

Classification: In-Confidence
Example 5.4


---

## Page 32

Classification: In-Confidence
Example 5.5


---

## Page 33

Classification: In-Confidence
Practical considerations
• Although these examples can be solved analytically, 
this is often difficult or impractical.
• The KKT conditions quickly become challenging to 
solve analytically  and as the number of constraints 
increases, trying all combinations of active and 
inactive constraints becomes intractable.


---

## Page 34

Classification: In-Confidence
Meaning of Lagrange multipliers
• The Lagrange multipliers quantify how much the 
corresponding constraints drive the design. 
• More specifically, a Lagrange multiplier quantifies 
the sensitivity of the optimal objective function 
value f(x∗) to a variation in the value of the 
corresponding constraint.
• They quantify the relative importance of the 
constraints, e.g. when a constraint is inactive, the 
corresponding Lagrange multiplier is zero.


---

## Page 35

Classification: In-Confidence
Algorithms for solving constrained 
optimization problems
• In general, if we can solve the KKT conditions, we 
have solved the optimization problem.
• However, as mentioned previous, there is a 
combinatorial issue with directly solving the KKT 
conditions for many problems, so we need an 
algorithm.
• Most important algorithms are interior-point and 
SQP.


---

## Page 36

Classification: In-Confidence
Penalty methods
• The concept behind penalty methods is intuitive: to 
transform a constrained problem into an 
unconstrained one by adding a penalty to the 
objective function when constraints are violated or 
close to being violated.
• Exterior vs interior penalty methods


---

## Page 37

Classification: In-Confidence
Penalty methods
• We can use unconstrained optimization techniques to 
minimize
• However, instead of just solving a single optimization 
problem, penalty methods usually solve a sequence of 
problems with different values of μ to get closer to the 
actual constrained minimum. 
• As μ tends to infinity, we get the exact solution. 
However, we cannot start with a large value for μ 
because this results in the Hessian being ill-
conditioned.
• Instead, we start with a small μ and gradually increase 
it, using the previous solution as the starting point.


---

## Page 38

Classification: In-Confidence
Sequential Quadratic 
Programming
• Main idea: 
• solve the KKT conditions rather than the original 
problem
• this gives a system of equations r(x,λ) = 0, which, using 
Newton’s method, can be solved by via solving a 
sequence of linear systems.


---

## Page 39

Classification: In-Confidence
SQP
• In turns out this is equivalent to solving a local 
quadratic problem (QP) approximation
• In practice, SQP requires the Hessian -> quasi-
Newton approximation used e.g. BFGS formula, 
with line search, similarly to last week*.
* However, things are slightly more complicated in line search as not only are we trying to 
reduce the objective function, we are also trying to “steer away” from infeasibility.


---

## Page 40

Classification: In-Confidence
Interior point
• These methods form an objective similar to the 
interior penalty but with the key difference that 
instead of penalizing the constraints directly, they 
add slack variables to the set of optimization 
variables and penalize the slack variables.


---

## Page 41

Classification: In-Confidence
Interior point
• Similar to SQP, Newton’s method is used to solve 
KKT conditions.
• However, instead of solving the KKT conditions of 
the original problem, we solve the KKT conditions 
of the interior-point formulation.


---

## Page 42

Classification: In-Confidence
Interior point
• If µb = 0, then the interior-point formulation is 
equivalent to the original constrained problem. 
•  Similarly to penalty methods, we have to move 
slowly to prevent issues with conditioning due to 
the gradients.


---

## Page 43

Classification: In-Confidence
Interior point
• Determining the correct step-size (line search 
again!) is a crucial part of any interior-point 
algorithm, and it should be noted that this is used 
to enforce s > 0 implicitly.
• Hence, at each iteration, the parameters µb, x, and 
s are updated until we converge.


---

## Page 44

Classification: In-Confidence
Duality
• We have shown a barrier function interior point 
algorithm.
• In practice, the most successful algorithms are 
primal-dual ones, which are based on the concept 
of the Lagrangian dual function. 
• Why?
• The dual problem is always a convex problem
• The dual problem is unconstrained
• If certain (fairly common) conditions are satisfied, the 
solution of the dual problem is equal to the original 
(“primal”) problem, i.e. zero duality gap.


---

## Page 45

Classification: In-Confidence
Duality derivation


---

## Page 46

Classification: In-Confidence
Duality example 1
min
𝑥(𝑥−2)2 
subject to 𝑥≤1


---

## Page 47

Classification: In-Confidence
Duality example 2
min
𝑥
𝑥4 –  50𝑥2 +  100𝑥
subject to 𝑥≥−4.5


---

## Page 48

Classification: In-Confidence
Duality example 2


---

