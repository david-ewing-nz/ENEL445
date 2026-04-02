# Chapter 5 Constrained Optimisation-1

*Converted from PDF: Chapter 5 Constrained Optimisation-1.pdf*

---

## Page 1

Chapter 5
Constrained Optimization
Many (most) engineering optimisation problems are subject to constraints.
For example,
any problem involving voltages and currents will have maximum voltages that the circuit
can tolerate, maximum currents due to wire material and thickness. etc
Constraints may
be
physical limitations, O1" even equations which guarantee that the design does what it
is supposed.
if
we  are
optimizing
an electric vehicle design,
we   will
likely
have
constraints O features
we want , e.g.
the range of the car should be at least 200 km
Or
300 km
O1' whatever we want
This chapter is a summarisation of Chapter 5 ofthe course textbook (Martin & Nings)
and
as such; text and equations are (at times) copied
verbatim
without further
attribution. The author therefore claims no credit for the material in this chapter, only
responsibility for any errors
0O1'
mistakesl
5.1
Introduction
This chapter focuses 0n  constrained optimization problems which can be expressed as
min f (x)
subject to _i < Ti < #i,i = 1,2,
(5.1)
9;(x) < 0, j = 1,2,
ng
h(x)
0,1 =1,2,
nh -
where ng  denotes the number of inequality constraints
while
nh
represents the
number of equality constraints_
The optimality condlitions for constrained optimization problems
are nol as
straight-
forward
as those for  unconstrained optimization_
We begin with equality
constraints
because the mathematics and intuition are simpler, then add inequality constraints_
Both equality and inequality constraints state
condition that must be satisfied in
order for the problem to be solved
If it is not possible to satisfy these constraints, the
optimisation problem is infeasible. Equality constraints can be thought of as constraining
the solution to lie on a line O plane in n-space (in a problem with 2 design variables and
one
equality constraint, it is exactly
line; whereas if there are 3 decision variables and
one equality constraint, the solution must like 0n
plane)_
In-equality constraints define
region in which the solution
must lie.
Therefore, the optimal value of the objective
function
canl
never
improve (i.e.
decrease,
since
we
have  formulated
a   minimization
problem) via adding constraints_
41
E.g:

![Page 1](../course.material/figs/Chapter%205%20Constrained%20Optimisation-1/page_001.png)

---

## Page 2

42
CHAPTER
CONSTRAINED OPTIMIZATION
5.2
Equality constraints
Let
uS
consider the problem (5.1) with
n; ng
0 i.e. only equality constraints. From the
previous section, recall that
f(x)Tp > 0
was a necessary condition for optimality; i.e_
in all directions the objective function does not improve:
Of course,
a local minimum
as
opposed to the global minimum x
would satisfy this condition as well,
s0 this is not
sufficient condition for optimality:
What happens if we have equality constraints? We still need V f (x*)p > 0 but now p
is not every possible direction, but only feasible directions_
Why?
It does not matter if the
objeetive funetion improves if we are barred
that region via an equality constraint_
How do we find feasible directions p?
We use the same Tavlor-series approach:
h;(x + p) ~ h;(x) +
Vhs(x)p,l = 1,2,
(5.2)
Assuming that x is a feasible point, then h;(x) = 0 for all constraints
h;(x +p) ~ Vh;(x)Tp,l = 1,2,
nh.
(5.3)
To remain feasible, h;(x + p) = 0 for all j.
We can write this in matrix form
the Jacobian matrix Jh as:
Jh(x)p = 0_
(5.4)
This equation
states that any feasible direction has to lie in the nullspace of the
Jacobian of the constraints
What does this mean?   Assuming that the constraints
are
linearly independent. Jh
full row rank and thus reduces the feasible space
In fact,
for optimisation to be possible;
nh (otherwise the feasible space reduces to
single
point ) .
See Fig: 5.8 in the textbook for illustration
Having worked out our feasible directions,
we now have that for x* to be a constrained
optimum
Vf(x")Tp Z 0 for all p such that Jh (x" )p = 0.
(5.5)
Now, if p is a feasible direction, so is ~p (think of a line
if we can g0 in one direction;
we can also g0 in the other) . Therefore,
WC
require
Vf(x*)p -
= 0 for all p such that Jh (x*)p = 0
(5.6)
Now
we have
Lwo
equations; Vf(x*)Tp
0 and Jh (x* )p = 0 which ohviously bear
resemblance
to each other_
This has
mathematical interpretation.
Mathematically;
(5.2)
shows that p is in the
nullspace of Jh.
The row space of
matrix contains all
the vectors that are orthogonal to its nullspace, and the rows of Jh are gradients of the
constraints
Thus, the objective function gradient must be
linear combination of the
gradients of the constraints_
5.2) can thus be written as:
f(x") = -ZA;Vh;(x")
(5.7)
j=[
where
are called the Lagrange multiplicrs.
In matrix notation;
we therefore have:
Vf(x) = -Jh(x)A
(5.8)
h(x) = 0
from
Tlh :
using
has
nh

![Page 2](../course.material/figs/Chapter%205%20Constrained%20Optimisation-1/page_002.png)

---

## Page 3

5.3.
INEQUALITY CONSTRAINTS
43
In constrained optimization; it is sometimes convenient to use the Lagrangian func-
tion, which is a scalar function defined as
L(x,A) = f(x) + h(x)TA
(5.9)
Taking the gradicnt of L with respect to both x and
and setting them to zero yields
(5.8).
We have therefore transformed an
dimension constrained optimisation problem
to an n + nh dimension unconstrained problem.
However
this is not usually
way
to solve constrained optimization problems 
The optimality conditions just described are first-order conditions that are necessary
but not sufficient_
To make sure that
a point is
constrained minimum; we also need to
satisfy second-order conditions.
For the unconstrained
the Hessian of the objective
function has to be positive definite.
This is also sufficient for the constrained case; but
we can get
conservative condition since we only need to check the Hessian of the
Lagrangian in the space of feasible directions.
We therefore require the Hessian of the
Lagrangian function to be positive for any feasible direction p.
Do Example 5.2 and Example 5.3 in the textbook
5.3
Inequality constraints
We will re-use many of the same concepts, but must recall some
terminology to begin:
constraint is active if 9; (x*) = 0.
constraint is inactive if 9;(x*) < 0.
A constraint is feasible when 9;(x*) < 0.
As before; if &* is an optimum; any Small enough feasible
p from the optimum
must
result in a function increase_
Based on Taylor series expansion, we have the condi-
tion:
f(x")Tp z 0
(5.10)
which is the same a8 for the equality constrained case
To consider inequality constraints,
we use the same linearization as the equality
con-
straints (5.2) , but now we enforce an inequality to get:
9;(x + p) ~ 9;(x) + Vg;(x)Tp < 0,j = 1,2,
(5.11)
For a given candidate point that satisfies all constraints; there are two possibilities to
consider for each inequality constraint: whether the constraint is inactive (9;(x*) < 0) or
active (9;(x"*) = 0). If a given constraint is inactive; we do not need to add any condition
for it because
we can take & step p in any direction and remain feasible as
as the step
is small enough. Thus;
we only need to consider the active constraints for the optimality
conditions.
For the equality constraint.
we found that all first-order feasible directions are in the
nullspace of the Jacobian matrix: Inequality constraints are not as restrictive. From
5.3)-
if constraint
j is active (9;(x)
0) , then the nearby
9; (x
+p) is only feasible if
Vg;(x)Tp < 0 for all constraiuts j that are active. In matrix fori;
we can write
Jg(x)p <
0, where the Jacobian matrix includes only the gradients of the active constraints_
good
case,
less
step
nlg"
long
point

![Page 3](../course.material/figs/Chapter%205%20Constrained%20Optimisation-1/page_003.png)

---

## Page 4

44
CHAPTER
CONSTRAINED OPTIMIZATION
The set of feasible directions that satisfies all active constraints is the intersection of
all the closed half-spaces defined by the inequality constraints, that is, all p such that
Jg(x)p < 0.
This intersection of the feasible directions forms a polyhedral cone_
To find the cone of feasible directions, let
us first consider the cone formed by the
active inequality constraint gradients.
This cone is defined by all vectors d such that:
n9
d =
Jo = Co;Vgj, where Gj 2 0.
(5.12)
j=1
A direction p is feasible if pTd < 0 for all d in the cone_
The set ofall feasible
directions forms the polar cone of the cone defined by (5.3)-
5.3.1
Farkas' Lemma
Now that we have established some intuition about the feasible directions, we need to es-
tablish under which conditions there is no feasible descent direction (i.e.
we have reached
ah
optimum)_
In other words, when is there no intersection between the cone of feasible
directions and the open half-space of descent directions?
To answer this question, we can
use Farkas ' lemma_
This lemma states that given a rectangular matrix A with size m X n
and
vector b with length m (i.e. the same length as the rows of the matrix), one (and
only one) of two possibilities occurs:
There exists an m
X 1 vector y sueh that ATy > 0 and bTy < 0.
There exists an n X 1 vector x sueh that Ax
b and x > 0.
In our case, replace
A by the rectangular (i.e.
m
=n) matrix
JI , b by _ Vf,xby 0_
and y by
~P, and we have the following two possibilities:
There exists an n X 1 vector p such that Jgp < 0 and
Vf"p < 0.
There exists an n X 1 vector
such that
JF o = Vf and 0 2 0.
In the first case, this means there is
a feasible direction Jg(x*)p < 0 for which
we
can descend
Vf(x*)Tp < 0.
In the second case; we can rearrange to state Our optimality
criterion:
Vf(x") + Jg(x")T o =
=
0,with 0 > 0.
(5.13)
This is similar t0 the conditions (5.8) for equality constraints.
corresponds to the
Lagrange multipliers for the inequality constraints and carries the additional restriction
that
2 0.
5.3.2
Slackness
Similar to the equality constrained case, we can construct
Lagrangian function whose
stationary points are candidates for optimal points:
We need to include all inequality
constraints in the optimality conditions because we dlo not know in advance which
COI -
straints are active.
To represent inequality constraints in the Lagrangian;
we replace
them with the equality constraints defined by:
9; +
s; = 0,j = 1,
ng
(5.14)
"

![Page 4](../course.material/figs/Chapter%205%20Constrained%20Optimisation-1/page_004.png)

---

## Page 5

5.4.
KKT CONDITIONS
45
where Sj is
new  unknown  associated
with
each inequality
constraint
called
slack:
variable.
The slack variable is squared to ensure it is nonnegative; i.e.
if (5.14) then
9j
and the inequality coustraint j is feasible
The Lagrangian including both equality and inequality constraints is then
L(x,A,0,s) = f(x) + ATh(x) +
oT(g(x) +s 0 s)
(5.15)
where
represents the Lagrange multipliers associated with the inequality constraints_
Here, we use
to represent the element-wise multiplication of s_
5.4
KKT conditions
Similar to the equality constrained case,
we seek
stationary
for the Lagrangian
but nOw we have additional unknowns: the inequality Lagrange multipliers and the slack
variables.
Taking partial derivatives of the Lagrangian with respect to each set of
uIl -
knowns and setting those derivatives to zero vields the first-order optimality conditions:
ng
JL
d f
dht
89;
L=0
LA;
+Zoj
0,i = 1,
nx
(5.16)
dxi
dx;
dxi
(=1
j=1
This criterion is the same as before but with additional Lagrange multipliers and
con -
straints_
the derivatives with respect to the equality Lagrange multipliers,
we
have:
JL
VaL = 0
h = 0,1 =1,
nh
(5.17)
Ox
which enforces the equality constraints as before   Taking derivatives with respect to the
inequality Lagrange multipliers,
we get=
8L
cL =0
3
=9; + 8} = 0,j = 1,
ng
(5.18)
which enforces the inequality constraints_
Finally, differentiating the Lagrangian with
respect to the slack variables, we obtain:
aC
VsL _ 0
S
0,j = 1,
(5.19)
which is called the complementary slackness condition:
This condition helps us to distin-
the active constraints from the inactive ones _
For each inequality constraint, either
the Lagrange multiplier is zero
which means that the constraint is inactive) , O the slack
variable is zero (which means that the constraint is active).
Unfortunately;
the complementary
slackness   condition introduces
combinatorial
problem.
The complexity of this problem grows exponentially with the number of in-
equality constraints because the number of possible combinations of active versus inactive
constraints is 2n9
In addition to the conditions for & stationary
of the Lagrangian (5.16)-(5.19).
recall that
we
require the Lagrange multipliers
the active constraints to be noneg-
ative   Putting all these conditions together in matrix form; the first-order constrained
< 0
point
Ox;
Taking
doj
20j8j
nlg*
"Jsj
guish
point
for

![Page 5](../course.material/figs/Chapter%205%20Constrained%20Optimisation-1/page_005.png)

---

## Page 6

46
CHAPTER
CONSTRAINED OPTIMIZATION
optimality conditions are as follows:
'$ + JEA+J9o = 0
(5.20a)
h = 0
(5.20b)
9 + $ 0 $ = 0
5.20c)
s = 0
5.20d)
2 0
5.20e)
As in the equality constrained case,
these first-order conditions
are necessarv
but
not  sufficient _
The   second-order  sufficient   conditions require that the Hessian of the
Lagrangian must be positive definite in all feasible directions, that is,
p" Hap > 0
(5.21a)
Jhp = 0
(5.21b)
Jgp < 0
5.2le)
In other words, we only require positive definiteness in the intersection of the nullspace
of the equality constraint Jacobian with the feasibility cone of the active inequality
COll -
straints_
Do Example 5.4 and Example 5.5 in the textbook.
Although these examples can be solved analytically; this is often difficult
01'
imprac-
tical.
The KKT conditions quickly become challenging to solve analytically
and as the
number of constraints increases, trying all combinations of active and inactive constraints
becomes intractable. Furthermore, engineering problems usually involve functions defined
by models with implicit equations, which are impossible to solve analytically:
The reason
we include these analytic examples is to gain
better understanding of the KKT condi-
tions.
For the rest; of the section;
we focus On numerical methods_
which are necessary
for the vast mnajority of practical problems
5.5
Lagrange multipliers
The
Lagrange multipliers quantify how much
the corresponding  constraints drive the
More specifically;
Lagrange multiplier quantifies the sensitivity of the optimal
objective function value f (x*
to a variation in the value of the corresponding constraint_
Here
we
explain why that is the case.
We discuss only inequality constraints, but the
same analysis applies to equality constraints_
When
constraint is inactive; the corresponding Lagrange multiplier is zero_
This
indicates that ehanging the value of an inactive constraint does not aflect the optimum
a5
expected.
This is only valid t0 the first order because the KKT conditions are based
Onl
the linearization of the objective and constraint functions  Because small changes are
assumed in the linearization,
we do not consider the case where an inactive constraint
becomes active after perturbation_
It can be derived
see Section 5.3.3 of the textbook) that:
0;
(5.22)
dgi
Thus, the Lagrange multipliers can predict how much improvement Can be expected if
given constraint is relaxed_
For inequality constraints; because the Lagrange multipliers
again
desigu:

![Page 6](../course.material/figs/Chapter%205%20Constrained%20Optimisation-1/page_006.png)

---

## Page 7

5.6.
ALGORITHMS FOR SOLVING CONSTRAINED OPTIMIZATION PROBLEMS47
are
positive at an Optimum; this equation correctly predicts & decrease in the objective
function value when the constraint value is increased.
The derivative defined in (5.22
has practical value because it tells us how much
given constraint drives the design.
In this interpretation of the Lagrange multipliers,
we
need to consider the scaling of the problem and the units.
Still,
for similar quantities,
they quantify the relative importance of the constraints_
5.6
Algorithms for solving constrained optimization
problems
In general, if we
Call
solve the KKT conditions
WC
have solved the optimization problem.
However , as mentioned previous, there is a combinatorial issue with directly solving the
KKT conditions for many problems;
SO
we need an
algorithm _
There are several methods used to solve constrained optimisation problems, however
the most important solvers are the interior point and SQP methods_
We do not have
time to describe any method in detail, but will give
quick introduction here to interior
point   methods.
We start by discussing the fundamental coucept of penalty methods
which underpin interior
solvers
5.6.1
Penalty methods
The concept behind penalty methods is intuitive:
to transform
constrained problem
into an unconstrained one by adding a penalty to the objective function when constraints
are
violated or close to
violated.
As mentioned in the introduction to this chapter,
penalty methods are no
used directly in gradient-based optimization algorithms
because
have  dlilliculty converging to the true solution:
However , these methods
are still valuable because, among other reasons; (1) they
are
simple and thus ease the
trausition into understanding constrained optimization; (2) penalty concepts are used in
itnerior poiints methods:
The penalized function can be written as:
f(x) = f(x) + pt(x)
(5.23)
where "(x) is a penalty function; and the scalar / is a penalty parameter_
This is similar
in form to the Lagrangian, but one difference is that / is fixed instead of
variable_
Various forms for T(x)
cal
be used,
to different penalty methods:
There
are tWO main types of penalty funetions:
exterior penalties_
which impose
penalty only
when constraints are violated, and interior penalty functions, which impose a penalty that
increases as
a constraint is
approached:
The exterior penalty leads to slightly infeasible
solutions, whereas an interior penalty leads to
feasible solution but underpredicts the
objeetive.
We can use the unconstrained optimization techniques to minimize f(x).
However ,
instead of just solving
single optimization problem, penalty methods usually solve
sequence of problems with dlifferent values of
pL to get closer to the actual constrained
mninimum.
The value of the penalty parameter /l must be chosen carefully.
Mathemati-
cally; we recover the exact solution to the constrained problem only as /L tends t0 infinity:
However, starting with a
value
p is not practical.
This is because the larger the
value of p the larger the Hessian condition number; which corresponds to the curvature
point
being
longer
they
being
leading
Jarge
for

![Page 7](../course.material/figs/Chapter%205%20Constrained%20Optimisation-1/page_007.png)

---

## Page 8

48
CHAPTER
CONSTRAINED OPTIMIZATION
varying greatly with direction:
This behavior makes the problem difficult to solve
nU-
merically.
To solve the problem more effectively; we begin with
small value of p and
solve the unconstrained problem
We then increase
pl and solve the new unconstrained
problem; using the previous solution as the starting
We repeat this process until
the optimality conditions (Or some other approximate convergence criteria) are satisfied.
By gradually increasing /6 and reusing the solution
the previous problem;
we
avoid some of the ill-conditioning issues_
Thus, the original constrained problem is trans-
formed into
sequence of unconstrained optimization problems
5.6.2
Interior point solvers
These methods form an objective similar to the interior penalty but with the key difference
that instead of penalizing the constraints dlireetly, they add slack variables to the set of
optimization variables and penalize the slack variables. The resulting formulation is:
f(x)
[b
8j
J=I
(5.24)
subject to  g(x) + s = 0
h(x) = 0
Instead of solving the KKT conditions of the original problem; we solve the KKT condi-
tions of the interior-
formulation (5.24) .
This results in
a linear
problem that can
he easily solved
see Equation 5.100 in the textbook)_
These slack variables in (5.24) do not need to be squared, as was done in deriving the
KKT conditions, because the logarithm is only defined for positive
s values and acts as
barrier preventing negative values of $.
Similarly to penalty methods,
we have to move slowly to prevent issues with condi-
tioning due to the gradients
Determining the correct step-size is
a  crucial part of any
interior-point algorithm; and it should be noted that this is used to enforce $
implic-
itly. Hence, at each iteration; the parameters (also the barrier coefficient pb_
are
updated
until we conerge
Time prevents
discussion of convergence;
OT
indeed further discussion of interior-
methods,
but
the textbook has
an
excellent
and detailed   description
for those
wanting to know more: See especially Algorithmn 5.7 in the textbook:
Interior
solvers are common in
practice and are implemented in multiple soft-
ware
packages;
e.g
fmincon in  MATLAB
or
SciPy; IPOPT
Knitro;
etc_
Note:
for
those interested to make the comparison with SQP; SQP methods are also available in
MATLAB
sqp option in fmincon) , SNOPT; Knitro, and other packages a8 well. Reading
https:_
'au.mathworks com /help/optim/ug/choosing-the-algorithm.html may be helpful.
point_
from
n19
min;,$
log =
point
point
point

![Page 8](../course.material/figs/Chapter%205%20Constrained%20Optimisation-1/page_008.png)

---

