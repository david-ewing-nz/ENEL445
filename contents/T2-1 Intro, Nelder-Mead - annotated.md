# T2-1 Intro, Nelder-Mead - annotated

*Converted from PDF: T2-1 Intro, Nelder-Mead - annotated.pdf*

---

## Page 1

Gradient-Free Optimisation
Introduction
and Nelder-Mead
ENEL445 Applied Engineering Optimisation
2025

![Page 1](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_001.png)

---

## Page 2

Plan for the rest of the course 
Week 8 (this week)
●
Gradient-free Intro, Nelder-Mead
●
GPS and DIRECT
●
Nature-Inspired algorithms
Week 9
●
Linear Programming 
●
Discrete optimisation, Assignment problems
●
Simulated annealing
Week 10
●
Game theory
●
Surrogate-based optimisation, Maximum likelihood
●
Le

![Page 2](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_002.png)

---

## Page 3

Plan for the rest of the course 
Week 11
●
Jeremy - Power systems optimisation 1
●
Jeremy - Power systems optimisation 2
●
Our research
Week 12
●
Your research
●
Your research
●
Exam revision
Exam
2Q Joe
1Q Le
1Q Jeremy

![Page 3](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_003.png)

---

## Page 4

Outline
●Gradient-Free Motivation
●Exhaustive Search
●Nelder-Mead Algorithm

![Page 4](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_004.png)

---

## Page 5

Why Gradient-free
●
Gradient-based algorithms are efficient in finding local 
minima for continuous and smooth functions in high 
dimensional spaces.
However:
●
Objective function may not be smooth.
●
Gradients of objective functions may be hard to calculate.
●
Many problems have only a relatively small number of 
dimensions.
- Discrete
problems
- TSP
- Numerically
unisy
-Black
box

![Page 5](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_005.png)

---

## Page 6

Why Gradient-free
●
For gradient-based algorithms, function smoothness is 
essential when deriving the optimality conditions. The 
Karush–Kuhn–Tucker (KKT) conditions require the function be 
continuous in value (𝐶0), gradient (𝐶1), and Hessian (𝐶2) in at 
least a small neighborhood around the optimum.
●
When the objective and constraint functions are not smooth 
enough or when it is not possible to compute derivatives with 
enough precision, gradient-free algorithms are useful.
●
For functions with excessive numerical noise and 
discontinuities, gradient-free algorithms might be the only 
option.
●
Gradient-free algorithms only require evaluation of objective 
function values. Also known as zeroth-order algorithms.

![Page 6](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_006.png)

---

## Page 7

Rosenbrock's (banana) function 
(valley)
Why Gradient-free
Generate-and-Retry 
paradigm
●
However, the cost of gradient-free 
optimisation is sensitive to the 
cost of the function evaluations

![Page 7](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_007.png)

---

## Page 8

Rosenbrock's (banana) function (valley)
Aside: Test Functions
2D
f(x)
= 100(x2
-xi)+ (x, -1)

![Page 8](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_008.png)

---

## Page 9

https://www.sfu.ca/~ssurjano/rosen.html
Aside: Test Functions

![Page 9](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_009.png)

---

## Page 10

https://www.sfu.ca/~ssurjano/
optimization.html
Aside: Test Functions

![Page 10](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_010.png)

---

## Page 11

Local vs Global
●
Some gradient-free methods feature a global search 
that increases the likelihood of finding the global 
minimum. This feature makes gradient-free methods a 
common choice for multimodal problems.
●
However, not all gradient-free methods are global 
search methods; some perform only a local search.
Conversely, even though gradient-based methods are 
by themselves local search methods, they are often 
combined with global search strategies.
●
It is not necessarily true that a global search, 
gradient-free method is more likely to find a global 
optimum than a multistart gradient-based method.
●
As always, problem-specific testing is needed.

![Page 11](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_011.png)

---

## Page 12

No Free Lunch Theorem
Wolpert & Macready (1997)
●
“Any two optimization algorithms are equivalent when their 
performance is averaged across all possible problems.”
●
Each "restaurant" (problem-solving procedure) has a "lunch 
plate" (problem) with a "price" (the performance of the 
procedure in solving the problem). The menus of restaurants 
are identical except in one regard – the prices are shuffled from 
one restaurant to the next. For an omnivore who is as likely to 
order each plate as any other, the average cost of lunch does 
not depend on the choice of restaurant. But a vegan or a 
carnivore who seeks economy might pay a high average cost 
for lunch. To methodically reduce the average cost, one must 
use advance knowledge of a) what one will order and b) what 
the order will cost at various restaurants. That is, improvement 
of performance in problem-solving hinges on using prior 
information to match procedures to problems.

![Page 12](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_012.png)

---

## Page 13

Wolpert, D. H. & Macready, W. G. (1997). "No Free Lunch 
Theorems for Optimization". IEEE Transactions on Evolutionary 
Computation. 1: 67–82.
Wolpert, David (1996). "The Lack of A Priori Distinctions between 
Learning Algorithms". Neural Computation. Vol. 8. pp. 1341–1390.
Schaffer, Cullen (1994). "A conservation law for generalization 
performance". In Willian, H.; Cohen, W. (eds.). International 
Conference on Machine Learning. San Francisco: Morgan 
Kaufmann. pp. 259–265.
No Free Lunch Theorem

![Page 13](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_013.png)

---

## Page 14

Search
Algorithm
Function
Stochas -
evaluation
3
3
]
]
1
IlL
Nelder-Mead
GPS
MADS
Trust region
Implicit filtering
DIRECT
MCS
EGO
Hit and run
Evolutionary
Simulated Annealing
ticity

![Page 14](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_014.png)

---

## Page 15

Exhaustive Search

![Page 15](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_015.png)

---

## Page 16

Exhaustive Search
●
Also called brute-force search
●
Discretise the search space (grid)
●
Systematically check all possible points
●
Advantages:
■
Easy to implement
■
Embarrassingly parallelisable

![Page 16](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_016.png)

---

## Page 17

Exhaustive Search
●
Example: TSP with 20 cities: (20-1)! = 19! possibilities 
●
Disadvantage: Performance of the algorithm scales 
exponentially (or worse) with the number of design variables

![Page 17](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_017.png)

---

## Page 18

Nelder-Mead

![Page 18](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_018.png)

---

## Page 19

Nelder-Mead
https://www.npmjs.com/package/@nwaltham/fmin

![Page 19](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_019.png)

---

## Page 20

https://www.npmjs.com/package/@nwaltham/fmin
Nelder-Mead

![Page 20](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_020.png)

---

## Page 21

Nelder-Mead
●
The Nelder-Mead algorithm is based on a simplex, 
which is a geometric shape defined by a set of n+1 
points in the design space of n variables
●
In two-dimensions, the simplex is a triangle, and in 
three-dimensions, it becomes a tetrahedron
Nelder and Mead, “A simplex method for 
function minimization”, 1965.

![Page 21](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_021.png)

---

## Page 22

Nelder-Mead
●
The objective 𝑓 is evaluated for every point, and the 
points are ordered based on the respective values of 𝑓, 
from the lowest to the highest, giving an ordered list of 
simplex points 𝑋 = {𝑥(0), 𝑥(1), . . . , 𝑥(𝑛−1), 𝑥(𝑛)}
●
Each iteration aims to replace the worst point with a 
better one to form a new simplex
●
The algorithm modifies the simplex at each iteration 
using five simple operations
f(x()(
f(x))
smallest it best
biggest
it
worst

![Page 22](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_022.png)

---

## Page 23

Nelder-Mead
- reflection
#
·
-
inner
contraction ·
·a
wars) pone
- outer
contraction
F
- expansion
- Shrink ·
·

![Page 23](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_023.png)

---

## Page 24

Nelder-Mead
Orang
best -> and Worst yout-
11)
&
Y a
linear
Worst
&
equation
point
⑨
I
slic
x(z)
⑧

![Page 24](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_024.png)

---

## Page 25

Nelder-Mead
I
↓[ / · x()
U=2
&-
x(2)
U = 0. 5

![Page 25](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_025.png)

---

## Page 26

Nelder-Mead
k=k+1
flxp) < f(x())
f(xe) < f(x())
x(n)
Xe
else
f(xr) < f(xln-1))
x(n)
Xr
f(x) 2 f(xln))
f(xic) < f(xln))
Xc
x(n)
Xic
else
else
else
f(xoc) < f(xr)
x(n)
Xoc

![Page 26](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_026.png)

---

## Page 27

·

![Page 27](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_027.png)

---

## Page 28

·

![Page 28](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_028.png)

---

## Page 29

Nelder-Mead - Convergence Metrics
●
Size of the simplex:
●
Standard deviation of objective function values:
●
Difference between the best and worst values in the simplex.
Nelder-Mead can converge to non-stationary points - so check 
your results! [1]
[1] McKinnon (1996), “Convergence of the Nelder-Mead simplex method to a 
non-stationary point”

![Page 29](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_029.png)

---

## Page 30

Nelder-Mead
2D
3
2
Xo
X2
1
~2
1
2
3
X1

![Page 30](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_030.png)

---

## Page 31

Nelder-Mead - 1D
f
M·.
-
In
ID triangle"
is just
an interval

![Page 31](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_031.png)

---

## Page 32

Nelder-Mead
Extension
0.5
-0,5
"2
-1.5
1
-0.5
05
15
2

![Page 32](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_032.png)

---

## Page 33

User
API
Building
Release
SciPy
Installing L
Development
Guide
reference
source
notes
Section Navigation
SciPy API
Optimization and root finding
scipy.optimize
minimize(met ..
scipy
scipy cluster
scipy constants
minimize(method='Nelder-Mead')
scipy datasets
minimize
X0
args= ( ) ,
method-None
jac-None
hess-None
scipy differentiate
hessp-None
bounds-None
constraints-( )
tol-None
callback-None
scipy fft
options-None)
scipy fftpack
Minimization of scalar function of one or more variables using the Nelder-Mead
scipy integrate
algorithm:
scipy interpolate
scipy.io
See also
scipy linalg
For documentation for the rest of the parameters, see
scipy ndimage
scipy_@ptimize_minimize
scipy odr
scipy optimize
Options:
scipy signal
'sparse
disp
bool
scipy spatial
Set to True to print convergence messages_
scipy special
maxiter; maxfev
int
from
fun ,
scipy:s

![Page 33](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_033.png)

---

## Page 34

●
Gradient-free algorithms only require the evaluation of 
function values.
●
Useful when the objective and constraint functions are not 
smooth enough or when it is not possible to compute 
derivatives with enough precision.
●
Often easier to implement.
●
However, the overall cost of gradient-free optimisation is 
sensitive to the cost of the function evaluations because 
they require many iterations for convergence, and the 
number of iterations scales poorly with the number of 
design variables.
●
The Nelder-Mead algorithm is based on a simplex
Summary

![Page 34](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_034.png)

---

## Page 35

Exercises
●
List the pros and cons of gradient-based vs 
gradient-free optimisation methods 
●
Write out the key equations for the Nelder-Mead method 
and understand what each equation means
●
Find a 2D contour map, choose a starting point, draw 
out one iteration of Nelder-Mead

![Page 35](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_035.png)

---

## Page 36

conour
DZEEP
SPACES_PLARLIZF
Thanks!
4X
cat

![Page 36](../course.material/figs/T2-1%20Intro%2C%20Nelder-Mead%20-%20annotated/page_036.png)

---

