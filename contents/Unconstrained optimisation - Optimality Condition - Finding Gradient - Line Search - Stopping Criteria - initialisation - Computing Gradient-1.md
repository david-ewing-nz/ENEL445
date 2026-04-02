# Unconstrained Optimization - Optimality Condition - Finding Gradient - Line Search - Stopping Criteria - Initialization - Computing Gradient-1

*Converted from PDF: Unconstrained Optimization - Optimality Condition - Finding Gradient - Line Search - Stopping Criteria - Initialization - Computing Gradient-1.pdf*

---

## Page 1

Chapter
4
Unconstrained Optimization
4.1
Introduction
This chapter focuses O the following unconstrained optimization problem:
minf (x),
(4.1)
where x = [11,32,
Tn]T collects the continuous design variables and f(x) is the objective
function_
We are interested in developing numerical techniques that can generate
a sequence of
solutions X1, X2,
to (4.1)_
In particular; these techniques utilize the gradient information
of the objective function f(x) to find
a local minimum; starting from
an initial solution
guess Xo
In some cases, there exist bound constraints on the design variables.
The constraints
are
often very loose_
Some techniques for handling/eliminating these constraints are given
in Chapter 3.3.1.
4.2
Optimality Conditions
4.2.1
Necessary conditions
We define the conditions that qualify
given
x*
as
a local minimum_
We are
interested in local optimality because global optimality can only be established in limited
cases
The
is a local minimum if f(x*) < f(x) for
x in the neighborhood of x*_
The second-ordler Taylor-series approximation of the objective function f(x) around x
is, according to
3.50)
f(x" + pp) ~ f(x") + pVf(x")p +
zu*p"H,(x")
'Jp;
(4.2)
where p is
anl
arbitrary direction vector with Ilpllz = 1.
For sufficiently small step size
p > 0, we have that when x
is a local minimum;
f(x") < f(x" + pp) ~ f(x*) + pV f(x*)Tp
(4.3)
In other words_
we
require V f(x*)p > 0.
Since p is an arbitrary direction vector; the
gradient of the objective function at a local minimum f(x*) must satisfy
Vf(x") = 0.
(4.4)
25
point
point
any

![Page 1](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_001.png)

---

## Page 2

26
CHAPTER 4
UNCONSTRAINED OPTIMIZATION
This is the first-order necessary optimality condition for
a local minimum of an
UCOn-
strained problem.
Putting (4.4) into (4.2) yields
f(x* + up) ~ f(x") +
2u*p" H;(x")p
(4.5)
Thus, for the point x
that makes the gradient of the objective function zero to be a local
minimum;
we
require
p"H;(x")p 2 0.
(4.6)
With p
an
arbitrary direction vector , the Hessian mnatrix Hf(x*_
must be at least
positive semidefinite (see the definitions of Hessian in (3.25)
and positive semidefinite
matrices in (3.23)).
This is the second-order necessary optimality condition.
In words, the first-order and second-order necessary optimality conditions state that:
if
is
a local minimum;
we cannot find
any direction that
can immediately
decrease the objective function (first-order necessary optimal condition) by taking
ficiently small step along that direction; moreover , if we move slightly farther away from
x , the objective function will increase O1 at least remain the same (second-order necessary
optimality condition).
4.2.2
Sufficient conditions
The sufficient conditions for a
to be
a local minimum is that
Vflx*) = 0,
4.7a)
Hf(x"
is positive definite_
(4.7b)
The positive definiteness of a matrix is defined in (3.22)_
Positive definiteness of the Hessian guarantees that
is not
a weak minimum.
weak minimum,
we can
always find some directions such that pTH;(x")p is zero.
For an illustration of strong andd weak minima, as well as sadldle point and maximum;
see Fig:
4.11 in the textbook_
It is important to examine Example 4.17 in the textbook
as well for
unconstrained optimization problems using (4.7)_
4.3
Gradient-based Methods
The  methods that
will
be presented  focus
OH
producing;  in the current iteration
(iteration k), the solution Xk
on the basis of Xk_1 obtained in
the previous iteration
(iteration k _ 1).
This is usually achieved in two steps, where in the first step, the search
direction is determined, and in the second step, searching along the search dlirection; also
known as line search; is performed to find
Xk:
Mathematically;
we have
Xk = Xk-1 + @pk,
(4.8)
where pk is the search direction and @k is the step size found by the line search_
We are going to consider the use of gradient information; which leads to the develop
ment of
gradient-based methods here
A graphie illustration of this type of optimization
algorithms is given in
4.1 in the textbook.
fact, the optimization algorithms
arc
normally
named aftcr the method
used to find the scarch
direction
being
point
suf-
point
For
solving
Fig:
1Jn

![Page 2](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_002.png)

---

## Page 3

4.3.
GRADIENT-BASED METHODS
27
Recall that as pointed out in Chapter 2.3.1,
each component of the gradient Vf(x
gives the rate of change of the objective function f (x) at x (see an illustration in
4.2
in the textbook and note that the arrowed line pointing to the direction of iucreasing the
objective function)_
In fact,
the gradient  points in the direction of the fastest function increase
the current point.
To verify this, consider the first-order Taylor-series approximation of
the objective function (also called the directional gradient, see Figs.
4.5 and 4.6 in the
textbook for an illustration) , which is, from (3.47) ,
f(x + up) ~ f(x) +
pVf(x) p.
(4.9)
We have that Vf(x)"p =
where p is an arbitrary direction vector
and 0 is the angle between
" Vlx)4p. Theceto
and p. Therefore , the direction vector that maximizes
the increase in the objective function is the one in the same direction of the gradient
(i.e., cos(0) = 0).
In other words, the gradient gives the direction of the fastest function
increase.
It can also be noticed
(4.9) that if 0 € (~w/2,7/2) , moving
the directional
gradient still leads to a larger objective function value.
For |0l
=T/2,
moving
the
directional gradient gives the same function value under sufficiently small step size /l_
When
= T
this directional gradient gives the direction of the steepest descent
4.3.1
Steepest descent
A simple and intuitive
way to determine the search direction is to directly use the
inverse of the gradient at Xk-1; because _ Vf (xk-1) gives the direction of the steepest
decrease.
This method is called steepest descent O1' gradient descent.
In this method,
we
can set
pk:
~Vf(xk-1)
(4.10)
OT
more
commonly;
f
Pk:
(4.11)
IlVf(xk-1)llz
The normalization in (4.11) can mitigate the effect of the varying design variable magni-
tude on the
magnitude of the gradient elements
Another effective way to mitigate this
is to scale the design variables
see
4.4 and Example 4.19 in the textbook).
The rule
of thumb is to try making the objective function and all desigu variables have
an order
of magnitude of
The steepest gradient may be highly inefficient, especially when the curvature of the
objective function varies greatly
with the direction;
which
makes the gradient
a poor
representation of the function behavior beyond
a Siall
neighborhood
In this case
the
steepest gradient could show & zigzagging pattern
see Example 4.10 in the textbook for
all
illustration)
The above   phenomenon
cam
be explained  mathematically:
Suppose
all
exact   line
search strategy is adopted,
which
means that the value of @k is selected to minimize the
objective function
the direction pk -
In other words,
we find &k through solving
df (xk-1 + @pk)
0.
(4.12)
Fig:
from
from
along
along
(Xk
Tip
along
dak

![Page 3](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_003.png)

---

## Page 4

28
CHAPTER 4
UNCONSTRAINED OPTIMIZATION
By Chain rule of the derivative,
we have that
df (xk-1 + @kpk)
df(xk-1 + @kpk)
+ @kpk
+ WPk
(4.13)
Vf(xk_1 + @kpk)
Pk:
Vf (xk+1)" pk:
In other words, each search direction is orthogonal to the previous one (if (4.13_
can be
solved exzactly) .
Again, to mitigate the zigzagging behavior , scaling the design variables
sometimes is an effective technique.
4.3.2
Conjugate gradient
It is known that the gradient descent
can
perform poorly in
nalTow
valleys.
The
conjugate gradient method overcomes this disadvantage by the following insights obtained
from solving &n unconstrained quadratic optimization problem
f(x)
X
bTx.
(4.14)
2
where A is & positive definite matrix:
The above problem has
unique global minimum
that can be found by solving
Ax = b.
(4.15)
Taking inverse of A
can be
comnputationally cumbersome; because this has a complexity
of O(n? _
where n is the dimensionality of x
Instead,
we are
going to determine;
the conjugate gradient method,
a sequence of solutions Xo, X1,
that converges to the
solution satisfying (4.15)
We can notice that if
A is diagonal,
the contours of the objective function f (x) in
(4.14) would be elliptical and their axes are aligned with the coordinate axes_
As
result,
we can start at any point and are able to converge to the desired global minimum through
successively performing
an
exact line search as in (4.13
in each coordinate direction for
a total of n line searches. See
4.38 in the textbook for an illustration_
For the
more
general case
where
is not diagonal
the contours of the objective
function f (x) in
4.14) would still be elliptical but their axes are no longer aligned with
the coordinate axes_
In this case,
we can still converge to the desired global minimum
through successively performing an exact
search as in
4.13-
in each principle curva-
ture direction (i.e , the eigenvector of A
see
Chapter 2.3.23
for a total of n line searches_
See Fig:
4.40 in the textbook for
an
illustration:
However , computing the eigenvectors
of A is still quite costly:
The complexity is
on the order of O(n3
A significant property of the eigenvectors of a symmetric A is that
are conjugate
with respect to A
Mathematically; we have that they satisfy
vAvj = 0,
(4.16)
where Vi and Vj are different eigenvectors of A_
The conjugate gradient method is & more
convenient Way t0 find a sequence of conjugate search directions for the problem in
4.14)_
2The conjugate gradient method presented
can
also be applied to solve the lincar equations Ax = b,
where
is positive definite and
has
large dimensionality:
dxk-1
dak
Oxk-1
dak
TAx -
using
Fig:
line
again
they

![Page 4](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_004.png)

---

## Page 5

4.3.
GRADIENT-BASED METHODS
29
The conjugate gradient method starts with an initial solution guess Xo: Performing an
exact line search along the direction of the steepest descent po
~Vf(xo)
(Axo
b)
vields the step size
Exercise 4.1)
P (Axo
b)
PS Vf (xo)
(4.17)
pS Apo
Pi Apo
The next solution is thus given by X1
Xo + Wopo: The next search direction p1 is found
by setting it to be
P1 = ~Vf(xi) + B1Po;
(4.18)
and requiring that po and p1
are
conjugate with respect to A_
In other words, the new
search direction p1 is
linear combination of the previous search direction po and the
direction of the steepest descent at the current solution X1. B1 is found through applying
the definition of conjugacy in (4.16) , which is
81
PGAVf(xl)
(4.19)
PS Apo
We are going to repeat the above process until the residual Tk
b is sufficiently
small (i.e , Ilrllo
<t) 
The corresponding conjugate gradient algorithm is summarized
in Algorithm B.2 in Appendix B.4.2 of the textbook
The major steps in the k-th iteration
k 2 1) are sumarized here as follows:
PX_1 Vf(xk-1)
@k
4.20a)
Pi_1Apk-1
Xk
Xk-1 + WkPk-1,
(4.20b)
pT_AVf(xk)
Bk
(4.20c)
Pk:
=
~Vf(xi) +
(4.20d)
Two options to compute Bk in (4.20c) exist.
The first
one is the
Fletcher-Reeves
formula, where Bk is calculated
Vf (xk)TV f (Xk)
Bk
(4.21)
f(xk-I)TVf(xk-1)`
The second approach is the Polak-Ribiere formula, which is given by
Vf(xk) (Vf(xk)
Vf(xk_J
fk
(4.22)
f(xk_H)TVf (Xk
The Fletcher-Reeves formula is theoretically established in Appendix B.4.2 in the text-
book:
Some insights can be obtained by examining (4.21).
It can be seen that with the
Fletcher-Reeves formula, Bk is always positive.  Therefore, the search direction pk is guar-
anteed to be
direction, along which the objective function can be decreased
Exercise
4.2) .
On the other hand, with the Polak-Ribiere formula, Bk mnay hecome negative, when
the cost function is nonlinear with respect to the design variables_
To guarantee that pk
is still
a descent
direction,
we can rectify Bk using
Bk
max(0, Bk:).
(4.23)
The method of conjugate gradient
can
be applied to minimize nonlinear objective
functions.
The ouly requirement is that the objective function is smooth and its graclient
is calculable.
The major steps in the k-th iteration can be summarized as follows.
Axk
Apk-1
Pc-1
BxPk-I *
using

![Page 5](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_005.png)

---

## Page 6

30
CHAPTER 4
UNCONSTRAINED OPTIMIZATION
Perform
a line search (see Chapter 4.3.4) to find the step size @k
the search
direction pk-1,
Find the current candidate solution and
update the search direction
as in
4.20b)
and
4.20d) , where Bk is calculated using either (4.21) o
4.22) ,
If the Fletcher-Reeves formula (4.21) is used, reset the search direction pk to the
steepest descent direction every
iterations.
If the Polak-Ribiere formula is used,
the rectification operation in (4.23_
can be adopted to reset the search direction:
It is found empirically that adopting the Polak-Ribiere formula leads to faster convergence
that with the Fletcher-Reeves formula.
4.3.3
Newton's method
The gradient descent and conjugate gradient methods both utilize the gradient in-
formation
(first-order information) only. Line search for step size determination is thus
needed to ensure the decrease of the objective function through moving along these search
directions
On the other hand, Newton s method explores the first-order and second-order
information of the objective function around
point_
It can provide an estimate of the
step size, besicles the search dlirection
Newton $ method approximates the objective function f (x) around the solution ob-
tained in the previous iteration (iteration k-1), Xk-I. using the second-order Taylor-series
expansion given in (3.48).
Mathematically; we have
f(x) ~ f(xk-1) + Vf(xk-1)T (x
Xk_1) +
Zxx -xk-1)TH;(xk-1)x
Xk_1).
(4.24)
Taking the derivative of the right-hand side of (4.24) with respect to x and setting the
result to zero yield
Vf(xk-1) + H; (Xk-1)(x - Xk-1) = 0.
4.25
If the Hessian Hf (Xk-1) (see the definition of Hessian in (3.25)) is invertible, the solution
in the k-th iteration can be found through evaluating
X = Xk-1
Hf(Xk-1)-1Vf(Xk-1).
4.26)
It can be seen that the search direction and step size is obtained through rotating and
stretching the gradient at
using the Hessian.
One important characteristic of Newton's method is that if the original objective
function is quadratic (i.e, f(x) has the form f(x) = %xTAx+bTx+c; where A is positive
definite) . Newton'$ method, starting at any point Xo; converges to the mninimum in
a one
step
Exercise 4.3).
An example is shown in Fig:
4.45 in the textbook; which illustrates
that Newton s method is scale invariant
In practice, Newton's method could suffer from
a few issues
One is that
Newton
step in
4.26)
may necessarily lead to decreasing the objective function:
In particular ,
if the Hessian in (4.24) , Hf(xk-1), is not positive definite; Newton's method in this case
may even increase the objective function:
One typical approach is again to apply the line
search, which results in the following solution update
X = Xk-1
WkH; (xk-1)-IVf(xk-1).
(4.27)
The step size @k can be initialized to 1, when starting the line search:
along
Xk-1

![Page 6](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_006.png)

---

## Page 7

4.3.
GRADIENT-BASED METHODS
31
Levenberg-Marquardt Algorithm
Consider a
quadratic objective function
f(x)
2( - g(x))" (b
g(x)).
4.28)
Minimizing it is in fact
a nonlinear least squares (NLS) problem:
Gradient descent and
cOnjugate gradient methods can be
to this type of problem. But for this particular
type of problems, techniques that explore the specific structure of f (x) in (7.17) do exist_
They
are Gauss-Newton algorithm and Levenberg-Marquardt algorithm:
The idea of the Gauss-Newton algorithm is to approximate the nonlinear function
g(x) using the first-order Taylor-series expansion (see (3.45)) as
g(x)
g(xk-1) + Jg(xk-1)(x
Xk-1).
4.29)
Here, Jg(Xk-1
denotes the Jacobian of the multi-variate function g(x) around the solution
obtained in the previous iteration
It is defined as
91 (Xk-1)T
792(xk-1)T
Jg(Xk-1)
4.30)
Im (Xk-1)
where 9;(x) is the j-th component of g(x).
Putting (4.29
into (7.17) vields
f(x)
2(b
g(xk-1) - Jg(xk-1)(x
Xk-1))T (b - g(xk-1) - Jg(xk-1)(x ~ Xk-1)) (4.31)
The objective function  now  becomes
quadratic function with respect
to the design
variables x_
Following the process that leads to (4.25) and (4.26) yields the solution at
the current iteration_
which is
Exercise 4.4)
Xk
=
Xk-1 +
(Jg(xk-1)TJg(xk-1))
Jg(xk-1)" (b _ g(xk-1))
(4.32)
Comparing (4.32)
with (4.26
reveals that the Gauss-Newton
update is similar, to
so1ne extent , to the
update of Newton s method.
But the Gauss-Vewton method
uses
the first-order information only. In fact _
with the Newton'$ method_
the iteration should
be given in
4.26 ,
with the gradient and Hessian at Xk-1 equal to
Exercise 4.5)
f(xk-1) = -Jg(xk-1)T(b - g(xk-1)).
(4.33)
and
H;(xk-1) = Jg(xk-1) Jg(xk-1) - C(b;
9; (Xk-1))Hg; (Xk-1) ,
(4.34)
where
(Xk-1) is the Hessian of 9;(x) at Xk-1
and it is defined
as,
according to see
3.25),
829,0
Hg; (x) =
(4.35)
axdxT
applied
Xk-
Hy,'

![Page 7](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_007.png)

---

## Page 8

32
CHAPTER 4
UNCONSTRAINED OPTIMIZATION
It can be seen that the Gauss-Newton algorithm can be considered as a& modified version
of the Newton s method if the second term on the right hand side of
4.34) is ignored
This approximation would be effective if the residual b - g(xk-1) is small.
Otherwise, the
Gauss-Vewton update in (4.32_
may be inaccurate
To address this aspect , applying the line search is a
straightforward way:
Another
strategy that can
be adopted is the Levenberg-Marquardt algorithm.
The idea comes
from the following insight. If we replace the second term
on the right hand side of (4.34)
with pI, where I is a n X n
identity matrix.
The Newton' s algorithi in
4.26) becomes
Xk
Xk-1 +
(Jg(xk-1)TJg(Xk-1) + [I) 
Jg(Xk-1)T (b
g(xk-1))_
(4.36)
If p = 0, the above iteration reduces to the Gauss-Newton method
If p
+0, the
Newton's algorithm becomes the steepest gradient with
size of 1/pL.
The intro-
duction of / provides the chance to alternate between the Gauss-Newton's method and
steepest descent algorithm
The Levenberg-Marquardt algorithm replaces pI
pD, where
D
(Jg(xk-1)TJg(xk-1)) _
(4.37)
diag(A) is an operation that generates
diagonal matrix whose diagonal elements are
from the diagonal of A
Roughly speaking, the diagonal elements of D are the curvature
of the objective function
each coordinate axis
see Chapter 2.3.2 for the definition
of curvature)
The value of p is dletermined as follows_
If che current iteration leads t0 a decrease in
the objective funetion;
we may scale down / Using & constant factor p < 1 using /L < plp.
This corresponds to the case that the residual becomes smaller, and the Gauss-Newton
algorithm is effective.
Otherwise,
WC
increasing / by /L
F
p] p until
a decrease in
the objective function is obtained.
This corresponds
to
applying the gradient descent
with
a very small step size to guarantee the improvement in the objective function:
For
an summary of the
Levenburg-Marquardt algorithm; see Algorithm 10.3 in the textbook.
Quasi-Newton Methods
Newton' $ method in (4.26) requires the computation of the Hessian;
which could
be difficult in
some
applications.
On the other hand_
the Gauss-Newton algorithm
or
Levenburg-Marquardt algorithm only needs the gradient information; but their
tion is limited to the NLS problem; as their development exploits the specific structure of
the NLS objective function_
Quasi-Vewton methods attempt to address these drawbacks
through utilizing the gradient information obtained in each iteration only to build
an
approximation of the Hessian
The development of quasi-Vewton methods again starts with the quadlratic approxi-
mation of the objective function around the solution from the previous iteration
f(x) ~ f(xk-1) + Vf(xk-1)T(x
Xk-1) +
Z(x - Xk-1)T H;(xk-1)(x
Xk-1).
(4.38)
Compared
with
the quadratic approximation
adopted
by
the Newton's   method
(see
(4.24)) , the true Hessian H;(Xk
is nOw replaced by its estimate
H;(xk-1).
An advantage of the Gauss-Vewton algorithm
is that it
docs
not   need
to calculate the Hessian
explicitly:
step
using
diag
along
keep
applica -
Xk-1

![Page 8](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_008.png)

---

## Page 9

4.3.
GRADIENT-BASED METHODS
33
The update of the quasi-Newton solution is similar to (4.27) with H; (xk-1) replaced
by Hf(xk-1) ; which is
Xk
Xk-1 _
MkH; (Xk-1)-IVf(Xk-1).
(4.39)
The step size
needs to be found by applying the line search along the search direction
Pk
(Xk-1)-IVf(xk-1) and it must satisfy the strong Wolf condition (see Chapter
4.3) .
The quasi-Newton algorithm also needs to compute the estimate of the Hessian at Xk
to enable the next iteration (i.e , iteration k + 1). The updated Hessian has the form
H;(xk)
H;(xk-1) + AH;(xk, Xk-1).
(4.40)
The update AH; (xk, Xk-1) depends on the gradients of the objective function at Xk and
Xk-1. It is established based 0n the following idea:
with the estimated Hessian Hf(xk)
the quadratic approximation of the objective function at Xk matches the actual
ents of the objective function at Xk and
Xk-1.
Mathematically; the objective function is
approximated at Xk
f(x) ~ f(xk) + Vf(xk)T (x - xk) +
Zkx - x+)"H;(xs)x ~ xc):
(4.41)
Its gradient at Xk is Vf(xk), which is exactly the true gradient of the objective function
at Xk:
The gradient at Xk-1 is equal to
(Exercise 4.6) Vf(xk) + Hf(xk) (Xk-1
Xk:).
We
require that
Vf(xk_1) = Vf(xk)
+H;(x)(xk-1
~Xk)_
(4.42)
Or equivalently;
H;(xk) (xk
Xk_1) = Vf(xk) _ Vf(xk_1):
(4.43)
(4.43) is called the secant equation. It is consistent with the intuition behind the product
of the Hessian with
vector: the change in the gradient due to
from
to Xk
is given by multiplying the Hessian with the vector Xk
Xk-1 (also see Chapter 2.3.2)-
For notation simplicity.
we deline Yk
Vf (xk) _ Vf(Xk-1) and Sk
Xk
Xk-l, whieh
transforms the secant equation into
H; (xk)sk = Yk
(4.44)
We also need the estimated Hessian to be positive definite to ensure that the search
direction computed using the quadratic approximation always points to the descent di-
rection
A necessary condition is thus; from the secant equation in (4.44),
0 < s}H;(xk)sk
sk Yk-
4.45)
This is called the curvature condition:
The   secant   equation
is
linear   system
of
equations:
But to find
the   update
AH; (xk, Xk-1) in (4.40) with n(n + 1)/2 unknowns, it is not sufficient.
To address this
difficulty;
we resort to the idea of low-rank update.
Specifically; it is assumed that the
updated Hessian Hf (xk) is closest to Hf(xk-1) in the sense that the update
AH;(xk, Xk-1)
Exercise 4.7=
Show that the search direction at the (k - 1)th iteration; which is, according to (4.38) ,
Pk:
~Hr(xk-1)-IVf(xk-1), is a descent direction:
@k
~Hfl
gradi-
using
mnoving
Xk-1

![Page 9](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_009.png)

---

## Page 10

34
CHAPTER 4
UNCONSTRAINED OPTIMIZATION
has low rank:
This greatly reduces the number of unknowns to be determined:
The
ra-
tionale bchind this idea is that at cach iteration,
we only obtain one more
gradient of
the objective function:
Therefore, the amount of chauge in the Hessian should hot be
significant.
Among the proposed low-rank quasi-Newton updates, the one independently devel-
oped by Brovden; Fletcher, Goldfard and Shanno; and commonly referred to as the BFGS
update is considered the most effective One_
We shall focus 01 the BFGS update here
and other low-rank quasi-Newton updates are briefly discussed in
Appendix
in the
textbook:
To ensure that the estimated Hessian is positive definite, the BFGS update takes the
form
Xk-1) = a
+b -
4.46)
where u and
V are
linearly independent column vectors, and a and b are coefficients to be
decided.
It can be seen that the BFGS update is & positive semidefinite matrix of rank
Putting (4.46) into (4.40) and using the secant equation in (4.44) ,
we have
H; (xk-1)sk + a . uuTsk + b.vvT sk
= Yk
(4.47)
In the BFGS update,
u = Yk and
V =
Jsk . Substituting these results into (4.47)
and re-arranging
yk(1 _ a . yEsk) = H;(xk-1)sk(1 + b.sF H; (xk-1Js;)
(4.48)
In general,
Yk and Hy (xk-1sk are not parallel:
Therefore, for the equality in (4.48) to
hold
we require
0 =
b =
(4.49)
y} Sk
s} H;(xk-1sk
The BFGS update is thus given by
H;(xk)
Hy(xk-1) +
H;(xk-1Jsks} H;(xk-1)T .
(4.50)
s} H;(xk-1)sk
Combining (4.50) and (4.39 
gives the BFGS quasi-Newton method for continuous
UI-
constrained optimization_
Note that when implementing
'4.39) , the inverse of the estimated Hessian needs to
be found.
With BFGS update;
an efficient approach that updates the inverse of the
estimated Hessian can be established through invoking the Woodury matrix identity
see
Appendix C.3 in the textbook)
In particular; let Vk be the inverse of H;(Xk)
Vk is
related to Vk-1 via
Vk = (1 _ OrSkyK )Vk-1(1 -
OkSkyk ) + GxSksk ,
(4.51)
where
Ok
1/yE sk.
With Vk,
the   search  direction
can
be   easily  computed   using
VkVf (xk) _
The BFGS algorithm starts with Vo = I, which corresponds to the first iteration
gradient descent_
In the practical implementation;
we
might need to reset Vk from time
to time.
This is because the curvature information accumulated far' from the current
solution may be irrelevant and even leads to slow convergence
If the angle between
the current gradient Vf (Xk) and search direction
Vf(xk), which can be calculated
AH; (xk; =
uu"'
vvT ,
H;(Xk-1)
yield
ysrykyt
being
~Vkl

![Page 10](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_010.png)

---

## Page 11

4.3.
GRADIENT-BASED METHODS
35
by their inner product, is smaller than
particular threshold, reset V_
to the identity
matrix
In words, if the search direction becomes close to the gradient direction, which
could lead to increase in the objective function;
we choose to apply the gradient descent
in the current iteration and reset the BFGS update
The BFGS algorithm is summarized in Algorithm 4.7 in the textbook:
4.3.4
Line Search
Line search determines the step size @k after the search direction pk at the solution
is found.
To guarantee the decrease of the objective function, Pk needs to a descent
dlirection such that pK Vf (xk-1)
< 0.
Line search adldresses the following question: how
far to move
the direction pk.
After line search; the next solution is computed
Xk = Xk-I + @pk: (see
4.16 in the textbook for an illustration).
Line search is usually independent of the method for choosing the search direction
and thus, it
can be combined with any search direction determination method.
Along the search direction pk. the objective function has
a value given by f (xk-1 +
@kPk) -
Because both Xk-1 and pk
are
known; the mnultivariate objective function
HOW
depends
on the value of the step size
@k:  only:
That is
it
nOW
becomes
univariate
function, which corresponds t0
one-dlimensional slice of the n-dimensional input space
see
4.17 in the textbook for' an illustration).
The realistic
of the line search is NOT to find the minimum of f (xk-1 + @xpk)-
Instead; it aims at locating & point that is
enough
using the least number of eval-
uations of the objective function. Searching for the value that minimizes f (Xk-1 + @pk
may require many iterations but only result in marginal objective function improvement
To simplify the following presentation;, we define
O(ak) = f(xk_1 + @xPk)_
(4.52)
to make it explicit that line seareh involves the manipulation Ol & univariate lunction: It
is evident that @k corresponds to the start of the line search; since &(0) = f (xk-1) is the
objective function value at the previous solution
More importantly,
we have that
(ak_
=
Vf(xk-1 + WkPk)Tpk-
(4.53)
'(@k) is called the directional derivative
the search direction pk (see also (3.47))-
If & (ck) is positive, this indlicates that increasing the step size Over (k would increase
the objective function_
On the other hand, if
'(Nk_
is
negative, increasing the step size
over
@k would decrease the objective function_
At
@k
0
we have &(0)
0.
since pk
is & descent direction, which guarantees that moving from
cal
always improve the
objective function (see
4.20 fo1 an illustration)_
Sufficient decrease condition
To find a 'good enough' solution; we require that the corresponding step size satisfies
the sufficient decrease condition; also known as Armijo condition;
D(ak) < 0(0) + //10k0 (0) ,
(4.54)
where 0 < p1
is a positive coustant_
We usually set /L1 to be 10-4_
In (4.54) , @k8 (0)
is the expected decrease in the objective function; assuming that the function continues
Xk-]
along
using
Fig:
Fig:
goal
'good
along
Xk-1
Fig:
< 1

![Page 11](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_011.png)

---

## Page 12

36
CHAPTER 4
UNCONSTRAINED OPTIMIZATION
at the same
of
'(0).
The factor /l1 is less than one, indicating that
we consider
solution to be
good one; as
as it achieves
a very small fraction of the expected
decrease
see Fig:
4.21 and Fig:
4.22 for illustrations) .
Note that
we need to evaluate
the objective function before
we know whether
candidate point satisfies the sufficient
decrease condition and becomes a
enough solution.
To find the value of (k that meets (4.54) ,
aml
initial guess of ak is needed:
Some
methods; such as the Newton $ method and BFGS algorithm; provide the initial guess,
which is equal to
In many other cases,
WC
normally start with
guess set to be the
maximum
size and successively shrink it (typically with & factor of 0.5) until &
enough solution is found:
This bisection-like line search method guarantees
enough solution and is summarized in Algorithm 4.2 in the textbook_
The above approach has
few obvious drawbacks_
It may
require
large number
of iterations to yield
solution if the initial
guess is too large.
Or it
could lead to
conservative step size if the initial guess is too small (this becomes more severe il
We
increase the value of [L1 )-
The underlying reason is that we consider the objective function
values only
Strong Wolf conditions
shall account for the gradient information during the line search to improve ef-
ficiency:
The aim is t0 favor
step size with reasonable decrease in the objective
function, which could speed up the convergence and encourage exploring the
vari-
able space. For this purpose;
we include an extra
condition, called the sufficient curvature
condition, which is given by
lo' (ak) < u2lo (0)1.
(4.55)
In  words,
we further
require that if
a solution is
good enough
one
the directional
derivative at the
corresponding step size should have a magnitude smaller than a fraction
of the directional dlerivative at 0 (i.e.
the function
5(ak: ,
should be flattening/shallow
here) . See
4.25 for an illustration.   The typical value for Ul2 is between 0.1 and 0.9.
Setting /l2 to be zero requires the line search to find
a local minimum
along the search
direction
Pk:
But
we
are not going to pursue this,
in order to reduce the number of
objective function evaluations_
To see why the sufficient curvature condition helps find
better step size, consider
the case where 0 (@k)
[820' (0).
This means that at the current step size, the directional
derivative has the same sign and
similar magnitude as
'(0)
0, which indicates that
the current step size is too small.
On the other hand.
if & (ak "
[28 (0) (i.e , the
directional derivative is positive and has
similar magnitude as
'(0)), the current step
size is too big:
The suflicient decrease condition and suflicient
curvature condition
are
collectively
known a8 the strong
Wolf conditions.
Fig_
4.26 in the textbook illustrates the region
of step size values that satisfy the strong Wolf condition.
Note that /2 should be much
larger than
11 .
Bracketing and pinpointing
We present
a line search technique that finds a step size satisfying the strong Wolf
condlitions.  The method has two phases, namely the bracketing phase and the pinpointing
phase.
The bracketing phase aims at finding an interval within
which it is guaranteed
slope
long
good
good
step
finding
good
We
large
desigu
Fig:

![Page 12](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_012.png)

---

## Page 13

4.3.
GRADIENT-BASED METHODS
37
to find
a solution satisfying the strong Wolf conditions_
The pinpointing phase locates
point within the interval provided by the bracketing phase.
The bracketing algorithm is sumarized in Algorithm 4.3 in the textbook:
Essentially;
it starts with an initial guess of the step size Ginit. Then, we need to compute the objective
function value 6
and its derivative
(@init).
If one of the following holds,
6(0) .
@init satisfies the sufficient decrease condition and
'(@init) > ~[28 (0) > 0,
Then,
we have found the desired interval in the bracketing phase.
which is (0, (init) .
If
Qinit satisfies the sufficient decrease condition and |0' (Qinit) |
[2ld (0), we already locate
'good enough
solution that meets the strong Wolf conditions, which is Xk-1 | Qinit + pk.
If
satisfies the suffieient decrease condition but its graclient is even small than //20' (0)
(i.e ,
020 (0)) , this indicates that
we can
enlarge the initial guess of the step
size to find
still satisfying the strong Wolf conditions but with
larger step size
In this case,
we increase the initial guess by
a factor of
and repeat the above process
until (0,Qinit_
is the desired interval 01 GQinit is
solution already.  See
4.28
in the texthook for a1 illustration of those four cases
Once a1 interval is found in the bracketing phase,
bisection search can be invoked
to find a point that satisfies the strong Wolf conditions.
A more complicated method but
with faster convergence is detailed in Algorithm 4.4 in the textbook_
4.3.5
Stopping criteria
The iterative techniques developed s0 far require Some criteria to stop the iterations
and output the obtained solution.
According to Chapter 4.2,
for
solution x
to be
local minimum; the gradient of the objective function at x* should be zero.
Thus,
possible stopping criterion is that the maximum (absolute) component of Vf(x") is
than
a threshold 7, i.e..
IIVf(x")llx <t,
(4.56)
where |l . Ilx is the infinity norm defined in
3.14).
typical value for v is 10-6.
To take
into account the
magnitude of the gradient,
commonly used criterion is
Ivf(x")llo < 7(1 + IIVf(x")llo),
(4.57)
where Vf(xo) denotes the gradient at the initial solution guess Xo_
Normally; it is not   necessary
to examine the Hessian Hf(x*
(see Chapter 4.2.2)_
because the consicered iterative methods all utilize the search direetions that lead t0 the
reduction in the objective function_
In practical applications, the objective function
may be poorly scaled,
or there are
other numerical issues that prevent the algorithm from satisfying (4.56)
Ol'
(4.57).
In
these cases, to keep the algorithm from running indefinitely:
widely used criterion is to
set a
limit 0n the number of iterations O" function calls.
Another useful way is to examine
the progress of the algorithm in terms of the amount of reduction in the objective function
or the
change in the solutions_
Mathematically;
we may stop the iteration if
If(xk+1) _ f(xk) < -(1 + |f(xk));
(4.58a)
Ilxk+1
Xkllo < -(1 + Ilxkllo)
(4.58b)
If you are applying
third-party optimizer,
it is important to keep in mind the Tip
4.1 on
Page 94 of the textbook
( @init
Qinil
@init
(@init
point
good
Fig:
less

![Page 13](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_013.png)

---

## Page 14

38
CHAPTER 4
UNCONSTRAINED OPTIMIZATION
4.3.6
Algorithm Initialization
The gradient-based algorithis presented in Chapter 3.4 are all local search methods
If the objective function is multimodal,
the quality of the local minimum found by the
gradient-based algorithms may heavily depend on the initial solution guess Xo:
straightforward way to improve the performance of the gradient-based method is to
augment them with
a multistart
approach;
where multiple solution guesses are selected
from engineering intuition (i.e , educated guesses
on the basis of vour
understanding of
the optimization problem in consideration) , O" sampling methods
By utilizing multiple
initial solution guesses, we increase the chance of
solution.
If we converge to
the same local minimum, even though we start with multiple well-spaced initial solutions;
the objective function may not be multimodal at all.
naive  full factorial sampling;
where  we  discretize each dimension of the input
to the objective function and generate
containing all the combinations; is highly
inefficient_
This is because it scales exponentially with the number of design variables
(i.e._
it suflers from the curse of dimensionality).
Thus, it is a COmon practice t0 identily
the most influential design variables first , through
sensitivity analysis.
Another straightforward way for sampling is random sampling,
where the samples
are obtained by following
desired distribution such
as uniform distribution to draw
independent samples in the design space. It scales better than the full factorial sampling
hut it is subject to potential clustering of the samples (see
10.3 in the textbook for
all
example). We thus need a
sampling strategy to cover the
space efficiently
than the full factorial sampling O random sampling:
shall describe two commonly used sampling methods in the following:
Latin hypercube sampling (LHS)
The idea behind could be best illustrated by considering
2D case (i.e.-
two design
variables)_
Suppose
we   want  only
8 samples_
We
can first   generate
x 8 grid
by
dliscretizing each dlimension to
8 intervals.
To cover the whole dlesigu space effieiently
using only 8 samples, we can require that each rOw and each column of the
has only
one sample. Therefore, when projecting the samples along any dimension; the histogram
should be uniform, indicating &
coverage.
This concept is called the Latin square
and its extension to higher dimensions is called the Latin hypercube.
Apparently; the Latin square O1 Latin hypercube is not unique (see Fig:   10.6 in the
textbook for two examples).
One approach is to find the desired Latin square/hypercube
through solving
constrained optimization problem.
The problem requires that in any
given TOW
or
column; there is only one sample and the minimum distance between any
sainple
is maximized.
Solving the above problem may be challenging:
much simpler approach typically
used in practice is given in Algorithm 10.1 in the textbook:
We shall illustrate a simplified
version of it  Suppose that
WC
would like to generate ns samples in
design space of nd
dlimensions: For simplicity; assume that the design variable in each dlimension is bounded
in the range [0,1].
The algorithm first discretizes randomly each dimension
Rij
Vij
i = 1,2,
nd;
j = 1,2,
n,8:
(4.59)
nls
ng
Rij represents
sample iucependeutly drawn from the uniform distribution over [0,1].
In words, it partitions each dimension into ns uniform intervals and then draws & sample
finding
good
The
grid
e.g  -
Fig:
good
design
We
grid
good
pair
using

![Page 14](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_014.png)

---

## Page 15

4.3.
GRADIENT-BASED METHODS
39
from each interval
The samples Vij is then collected in
a nd
ng matrix; each
OW of
which corresponds to
a certain dimension and each column of which corresponds to
samnple.
Note that this step produces a Latin square/hypercube already but the samples
are nOW distributed
the `diagonal' of the design space
To improve the coverage of
the design space,
we
randomly permute each row
see
Fig:
10.6 in the textbook
for illustration).
The above process can be repeated
of times and
we select the
Latin square/hypercube with the largest summed
minimum distance between points as
the algorithm output
The above algorithm can be easily generalized to the case where the projection of the
samples
certain dimension needs to satisfy
a distribution other than the uniform
distribution 
The only modlification is to apply the inversion sampling technique to the
samples Vij
the particular dimension before random permutation.
This
can
be
considered as changing the histogram /intervals
that dimension to approximate the
desired distribution.
For more details on the inversion sampling technique, please refer
to
Page 397 and Fig:
10.7 of the textbook_
Halton and Hammersley sequences
Halton and Hammersley sequences both belong to the family of low-discrepancy se-
quences that
are deterministic and well spatially spread.
An attractive property is that
the length of these sequences can be extended in an online mnanner_
In other words; they
need not to be generated beforehand and
nCW
points can be added whenever required:
Moreover ,
each new point added to the sequence maintains low discrepancy.   This prop-
erty is particularly important for iterative procedures such aS quadrature (i.e., numerical
integration) , Monte Carlo simulation, and multistart optimization algorithms
for further
improving the quality of the solution)_
Here, discrepancy means the variation of the point
density throughout the design space.
discrepancy thus refers to even
density.
Halton and Hammersley sequences are generated based on the generalization of the
one-dlimensional van der Corpul sequence.
Let i be an
integer _
We represent
i in base b
as
i = @o + @1b +
+
+ a,br-
(4.60)
where 0 < aj < b -1, j = 0,1,2,
The integer
i is thus a (r + 1)-dligit number in
base b.
When b = 2.
we have the well-known binary representation.
Using (4.60), the i-th element 0 (b) in the generalized
van der
Corput sequence is
found via
(0
Ob(i) =
62
+
+
(4.61)
This method is known
as the radical inverse function for base b, which is summarized in
Algorithm 10.2 in the textbook
An example is given here_
For base 2, the generated
sequence is
5
3 7
(4.62)
2' 4'4
8
8' 8' 8' 16
In words, the interval [0,1] is split in half and then each subinterval is further halved.
Halton sequence for multiple dimensions are produced by using different prime num-
bers for each dimension.
That is; the i-th Halton sequence is generated
[06 (i) , 0b2 (i) ,
(i)]:
(4.63
An example of a two-dimensional Halton sequence is given in Fig: 10.10 in the textbook
along
again
couple
along
along
along
Low
point
(2b2_
br+1
using
Obna '

![Page 15](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_015.png)

---

## Page 16

40
CHAPTER 4
UNCONSTRAINED OPTIMIZATION
Hammersley
sequence
can
be considered
as
special case of Halton
sequence.
It
requires the number of points to be generated np is known beforehand_
Another difference
is that for the first dimension,
spacing is used.
The i-th Hamersley sequence is
generated
pb1
0bz (i) ,
(4.64)
An example of
two-dimensional Hammersley sequence is given in Fig:
10.12 in the
textbook:
4.4
Computing the Gradient /Derivatives
The gradient-based techniques developed in Chapter 4.3 for the unconstrained opti-
mization problems all require the gradient of the objective function with respect to the
design  variables.
Each element of the gradient is simply the partial derivative of the
objective function with respect to a particular desigu variable  Evaluating the derivatives
efficiently is central in the numerical optimization algorithms_
The methods for computing derivatives can be grouped into three categories_
accord-
ing to the amount of the information about the function_
If
we
only
access to the
inputs and outputs of a function (i.e.
the function can be considered as a black box). its
(partial) derivatives can be found using finite dlifferences detailed below_
When
we have
the analytical expression of the function O' have access to every line of code for realizing
the function of interest,
we can find the derivatives through algebraic manipulations
or
perform algorithmic differentiation. In the intermediate case; implicit analytical methods
are used.
See Fig: 6.2 in the textbook for an illustration:
Finite differences
Finite-difference methods are simple but versatile.
They require function values only
for derivative evaluation.
gradient-based optimization software perform finite dif-
ferences by default when the user does not provide the required gradient_
Finite-difference methods compute each element of the gradient individually. Suppose
we are interested in
finding €f(x)/dw;: For this purpose, we first approximate the function
f (x)
the j-th coordlinate axis
the Taylor series expansion, which is
9f(x)
h &? f (x)
h &3 f (x)
f(x + he;) = f(x) + h
(4.65)
2!
dx}
31
dx;
Here, ej dlenotes the j-th colum of a
n X n
identity matrix (i.e., its j-th element is 1 and
other elements are all equal to zero). From (4.65) ,
straightforward way to approximate
the desired partial derivative is given in the following forward difference formulae:
df (x)
f(x +
flx)
(4.66)
where h
0 is commonly called the finite difference
size.
Again from (4.65),
we
have that (4.67_
is a first-order approximation as the truncation error is O(h). Similarly;
we can easily obtain another first-order approximation, which is the backward difference
formulae:
df(x)
f(x - f(x
he;))
(4.67)
regular
using
Obua-1'
have
Many
along
using
dxj
hej
dxj
step
Jxj

![Page 16](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_016.png)

---

## Page 17

4.4.
COMPUTING THE GRADIENT/DERIVATIVES
41
The other elements in the required gradient can be computed in the same manner_
Thus,
the finite differences have a complexity proportional to the dimensionality of the inputs_
We can compute both the forward dlifference and backward difference, and average
them to obtain an improved estimate of the derivative, which is
df (x)
f(x + hej
f(x
4.68)
2h
It can be shown
'Exercise 4.8) that this is
second-order estimate (i.e., the truncation
error is
o(h?)).
Note that according to (4.65) , adding f(x +
and f (x -
he;) cancels out the first-
order and third-order derivatives_
Besides, the second-order derivatives are kept and can
be estimated using
02 f (x)
f(x + hej) _ 2f(x) + f(x _ hej)
(4.69)
8x}
h2
Finite difference methods are subject to the step size  dilemma
It can be observed
from the finite differences have
a truncation
CFTOl
O(h)
0r"
O(h?).
This indicates that
using
smaller  finite difference step size
h can improve the estimate.
Iowever , as
decreases; the subtractive cancellation effect, where the finite difference estimate can be
entirely wrong; becomes more prominant_
See Example 6.3 and Table 6.1 in the textbook
for an example_
There exists an
optimal step size.
To find it.
an iterative search is
required.
One
way to search for
step size is t0 start
with
relatively large value of h
h
0.01) . Every time, the
size is decreased by
a factor
(e.g:.
10) .
Usually;
the derivative estimate would monotonically decrease/increase at the beginning:
The
iteration terminates when the monotonic decrease/inerease stops_
In practice; to tak into
account the
scaling of different design variables,
we   normally use
a step size equal to
h(1 +lv;h)
Complex step
The complex-step derivative approximation computes the partial derivatives using
variables.
The basic idea comes
noting that if we usC
a pure imaginary
step size ih, the Taylor series expansion of the function of interest at x would become
af(x)
h2 &2 f (x)
h3 &3 f (x)
f(x +
=
f(x) +ih
+
(4.70)
21
dx;
31
dx;
By taking the imaginary part on both sides, we arrive at
df(x)
Imf (x +ihej)
(4.71)
with
a truncation error
O(h?).
The
significant advantage of this method is that the complex step method does not
have subtraction, which eliminates the impact of subtractive cancellation.
This enables
the use of a very small value of the step size h; close to the machine precision (in
reasonable choice is the square root of the smallest representable number) .
and improves
the estimation accuracy greatly:
Another byproduct of evaluating f(x + ihej_
is that we
hej
J1j
hej
(e.g .
good
step
complex
from
ihe;)
dxj
dxj
facl .

![Page 17](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_017.png)

---

## Page 18

42
CHAPTER 4
UNCONSTRAINED OPTIMIZATION
can
simultaneously estimate the function value at X with a truncation error
O(h?) ; which
is given by
f(x)
Re{f(x + ihe;)}
4.72)
Here, Re{:} takes the real part_
The challenge of realizing the complex step method is that
we   must   convert the
code and
the associated arithmetic for  function
evaluation
into
one that
can
handle
complex numbers  correctly:
Programming languages such as Python and MATLAB are
overloaded to automatically accept complex numbers_
But necessary changes are needed
if the program has logic operators (Z, <, if, else, max; min, _
Js
Normally;
we must add
the Re{} operations to
make them
correct_
Besides,
some functions
may have to be
replaced undler complex argumnents
For example, for the absolute value function; it does
not output any imaginary part at all.
A reasonable modified version is
C1
iy, if x < 0
abs(w + iy) =
4.73
~8 +iy, if z > 0
Refer to http: / /bit.ly/complexstep for
list   of problematic functions, implementation
and scripts_
guide

![Page 18](../course.material/figs/Unconstrained%20Optimization%20-%20Optimality%20Condition%20-%20Finding%20Gradient%20-%20Line%20Search%20-%20Stopping%20Criteria%20-%20Initialization%20-%20Computing%20Gradient-1/page_018.png)

---

