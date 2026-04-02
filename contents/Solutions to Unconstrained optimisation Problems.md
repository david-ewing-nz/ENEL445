# Solutions to Unconstrained Optimization Problems

*Converted from PDF: Solutions to Unconstrained Optimization Problems.pdf*

---

## Page 1

Solution to Exercises
ENEL445 Applied Engineering Optimization
1
Exercise 4.1:
Consider minimizing the cost function f(x) =
1
2xTAx −bTx with respect to the design
variable x, where A is a positive definite matrix.
Denote the initial solution guess as x0. Assume that at x0, an exact line search is car-
ried out along the search direction p0 = −▽f(x0).
Compute the step size a0.
Solution:
It is easy to show that p0 = −▽f(x0) = −(Ax0 −b).
The exact line search finds the step size a0 by minimizing f(x0 + a0p0) with respect to
a0. The loss function is thus
f(x0 + a0p0) = 1
2(x0 + a0p0)TA(x0 + a0p0) −bT(x0 + a0p0)
∝1
2a2
0pT
0 Ap0 + a0pT
0 Ax0 −a0bTp0,
(1)
where all the terms not depending on a0 have been ignored. Note that since A is positive
definite, pT
0 Ap0 is positive. Finding the minimizer for (1) can be achieved by taking the
derivative with respect to a0 and setting the result to zero, which yields
a0 = −pT
0 (Ax0 −b)
pT
0 Ap0
= −pT
0 ▽f(x0)
pT
0 Ap0
,
(2)
where the definition of ▽f(x0) has been substituted. □

![Page 1](../course.material/figs/Solutions%20to%20Unconstrained%20Optimization%20Problems/page_001.png)

---

## Page 2

Solution to Exercises
ENEL445 Applied Engineering Optimization
2
Exercise 4.2:
Consider minimizing, using the method of conjugate gradient, the cost function f(x) =
1
2xTAx −bTx with respect to the design variable x, where A is a positive definite matrix.
The search direction for the (k + 1)th iteration is given by
pk = −▽f(xk) + βkpk−1.
(3)
Show that given that pk−1 is a descent direction at xk−1, pk is a descent direction at xk if
βk ≥0.
Proof:
We express xk as xk = xk−1 + ak−1pk−1, where ak−1 = −
pT
k−1▽f(xk−1)
pT
k−1Apk−1
> 0 is the step size (see
(4.20a) and (4.20b) in the course notes).
Since −▽f(xk) is already a descent direction at xk, we only need to show that pk−1 is
not an ascent direction at xk. For this purpose, we have
pT
k−1▽f(xk) = pT
k−1(Axk −b)
= pT
k−1(A(xk−1 + ak−1pk−1) −b)
= pT
k−1(Axk−1 −b) + ak−1pT
k−1Apk−1
= pT
k−1▽f(xk−1) + ak−1pT
k−1Apk−1
= 0,
(4)
where ak−1 = −
pT
k−1▽f(xk−1)
pT
k−1Apk−1
> 0 has been used in reaching the last equality (also see (2) and
(4.20a) in the course notes). This indicates that pk−1 is orthogonal to ▽f(xk), and it is not
an ascent direction. This completes the proof. □

![Page 2](../course.material/figs/Solutions%20to%20Unconstrained%20Optimization%20Problems/page_002.png)

---

## Page 3

Solution to Exercises
ENEL445 Applied Engineering Optimization
3
Exercise 4.3:
Consider minimizing, using the Newton’s method, the cost function f(x) = 1
2xTAx+bTx+c
with respect to the design variable x, where A is a positive definite matrix.
Suppose the initial solution guess is x0. Show that with Newton’s method, we can con-
verge to the optimal solution in one iteration.
Proof:
The optimal solution is x∗= −A−1b. This can be verified by taking the partial deriva-
tive of f(x) with respect to x and setting the result to zero.
With Newton’s method, we need to calculate the Hessian at x0, H(x0), which is equal
to A.
The next solution x1 can thus be obtained using
x1 = x0 −H(x0)−1▽f(x0)
= x0 −A−1(Ax0 + b)
= x0 −x0 −A−1b
= −A−1b
= x∗,
(5)
where f(x0) = Ax0 +b has been substituted to reach the third equality. This completes the
proof. □

![Page 3](../course.material/figs/Solutions%20to%20Unconstrained%20Optimization%20Problems/page_003.png)

---

## Page 4

Solution to Exercises
ENEL445 Applied Engineering Optimization
4
Exercise 4.4:
Consider minimizing, using the Levenberg-Marquardt (LM) algorithm, the nonlinear least
squares (NLS) cost function f(x) = 1
2(b−g(x))T(b−g(x)) with respect to the design variable
x. Here, b is the measurement vector, and g(·) is the nonlinear vector measurement function.
In iteration k, the LM algorithm first approximates g(x) using the first-order Taylor-series
expansion as g(x) ≈g(xk−1) + J(xk−1)(x −xk−1), where xk−1 is the solution from the pre-
vious iteration and J(xk−1) is the Jacobian matrix.
Putting the above approximation back to the NLS cost function and minimizing it yields
the solution xk in the current iteration, iteration k. Find xk.
Solution:
The NLS cost function becomes, after applying g(x) ≈g(xk−1) + J(xk−1)(x −xk−1),
f(x) ≈1
2(b −g(xk−1) −J(xk−1)(x −xk−1))T(b −g(xk−1) −J(xk−1)(x −xk−1))
∝1
2(x −xk−1)TJ(xk−1)TJ(xk−1)(x −xk−1) −(x −xk−1)TJ(xk−1)T(b −g(xk−1)),
(6)
where the terms not depending on the unknown x have been ignored.
Because xk−1 is known, minimizing f(x) in (6) with respect to x is equivalent to mini-
mizing it with respect to (x −xk−1).
As a result, the minimizer can be shown to satisfy
J(xk−1)TJ(xk−1)(x −xk−1) −J(xk−1)T(b −g(xk−1)) = 0.
(7)
This is obtained by taking partial derivative of f(x) in (6) with respect to (x −xk−1) and
setting the result to zero. Solving (7) for x yields the solution in the kth iteration, which is
xk = xk−1 + (J(xk−1)TJ(xk−1))−1J(xk−1)T(b −g(xk−1)).
(8)
□

![Page 4](../course.material/figs/Solutions%20to%20Unconstrained%20Optimization%20Problems/page_004.png)

---

## Page 5

Solution to Exercises
ENEL445 Applied Engineering Optimization
5
Exercise 4.5:
Consider minimizing the nonlinear least squares (NLS) cost function f(x) = 1
2(b−g(x))T(b−
g(x)) with respect to the design variable x. Here, b is the measurement vector, and g(·) is
the nonlinear vector measurement function.
Derive the gradient of the cost function f(x).
Solution:
We re-write the cost function as
f(x) ∝1
2g(x)Tg(x) −bTg(x),
(9)
where the terms independent of the design variable vector x are all ignored.
Recall that the Jacobian is defined as
J(x) = ∂g(x)
∂x
=


▽g1(x)T
▽g2(x)T
...
▽gd(x)T

,
(10)
with g(x) = [g1(x), g2(x), ..., gd(x)]T.
As a result, we have
∂g(x)Tg(x)
∂x
= ∂Pd
i=1 gi(x)2
∂x
= 2
d
X
i=1
gi(x)▽gi(x) = 2J(x)Tg(x),
(11)
and
∂bTg(x)
∂x
= ∂Pd
i=1 bigi(x)
∂x
=
d
X
i=1
bi▽gi(x) = J(x)Tb,
(12)
where b = [b1, b2, ..., bd]T has been used.
Therefore, we arrive at
▽f(x) = −J(x)T(b −g(x)).
(13)
□

![Page 5](../course.material/figs/Solutions%20to%20Unconstrained%20Optimization%20Problems/page_005.png)

---

## Page 6

Solution to Exercises
ENEL445 Applied Engineering Optimization
6
Exercise 4.6:
In the quasi-Newton method, the cost function f(x) is approximated in the kth iteration as
f(x) ≈f(xk) + ▽f(xk)T(x −xk) + 1
2(x −xk)T ˜H(x)(x −xk),
(14)
where ˜H(x) is the approximated Hessian of f(x) at xk.
Find the gradient of the approximated cost function in (14) at xk−1.
Solution:
The gradient of the approximated cost function in (14) is
▽f(x) = ▽f(xk) + ˜H(x)(x −xk).
(15)
Setting x = xk−1 in (15) yields the desired result
▽f(xk −1) = ▽f(xk) + ˜H(x)(xk−1 −xk) = ▽f(xk) −˜H(x)(xk −xk−1).
(16)
□

![Page 6](../course.material/figs/Solutions%20to%20Unconstrained%20Optimization%20Problems/page_006.png)

---

## Page 7

Solution to Exercises
ENEL445 Applied Engineering Optimization
7
Exercise 4.7:
In the quasi-Newton method, the cost function f(x) is approximated in the kth iteration as
f(x) ≈f(xk) + ▽f(xk)T(x −xk) + 1
2(x −xk)T ˜H(x)(x −xk),
(17)
where ˜H(x) is the approximated Hessian of f(x) at xk.
Minimizing the above cost function yields the solution for the next iteration, which is
xk+1 = xk −αk ˜H(xk)−1▽f(xk),
(18)
where αk is the step size.
Show that the search direction in (18), which is pk = −˜H(xk)−1▽f(xk) is a descent direction.
Proof:
With the quasi-Newton method, the approximated Hessian ˜H(x) is always positive defi-
nite. As a result, we have
pT
k ▽f(xk) = −▽f(xk)T ˜H(xk)−1▽f(xk) < 0.
(19)
The last inequality comes from the positive definiteness of ˜H(x), which indicates that the
intersection angle between pk and ▽f(xk) is larger than 90o, and pk is a descent direction.
□

![Page 7](../course.material/figs/Solutions%20to%20Unconstrained%20Optimization%20Problems/page_007.png)

---

## Page 8

Solution to Exercises
ENEL445 Applied Engineering Optimization
8
Exercise 4.8:
The derivative of a scalar function f(x) can be numerically approximated using
df(x)
dx
= f(x + h) −f(x −h)
2h
,
(20)
which is an average of the forward difference and backward difference.
Show that the estimation error of (20) is O(h2).
Proof:
We can the third-order Taylor series expansions
f(x + h) = f(x) + df(x)
dx h + 1
2!
d2f(x)
dx2
h2 + 1
3!
d3f(x)
dx3
h3 + O(h4),
(21)
and
f(x −h) = f(x) −df(x)
dx h + 1
2!
d2f(x)
dx2
h2 −1
3!
d3f(x)
dx3
h3 + O(h4).
(22)
□
Therefore, we have
f(x + h) −f(x −h) = 2df(x)
dx h + 2
3!
d3f(x)
dx3
h3 + O(h4),
(23)
and
f(x + h) −f(x −h)
2h
= df(x)
dx
+ 1
3!
d3f(x)
dx3
h2 + O(h3).
(24)
The estimation error, which is mainly 1
3!
d3f(x)
dx3 h2, is thus O(h2).

![Page 8](../course.material/figs/Solutions%20to%20Unconstrained%20Optimization%20Problems/page_008.png)

---

