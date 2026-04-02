# Wk1Lecture2

*Converted from PDF: Wk1Lecture2.pdf*

---

## Page 1

Yhin
flx)
Design variables
7
x = {0 6,2 ~f
Design variables can be continuous or discrete, or a
mixture.
R=810,27,47,(0o_
Design variables should be independent; otherwise
there may be an infinite number of equivalent
min
(7
solutions.
3C
Solution
X( + 7C2 =0
boui
Don't forget to add physically meaningful bounds:
lowec
Xi 4 %,47
Tip: when starting to solve a problem, try to use as few
design variables as possible:
Classification: In-Confidence
+x)2
lper
boudA

![Page 1](../course.material/figs/Wk1Lecture2/page_001.png)

---

## Page 2

Objective function
(cost {unction)
(hin
fo)
7
These is the objective by which we measure the
quality of a solution:
In this course, we will usually have a closed-form
9 duaction
function f(x) which serves as the objective to be
minimised lor maximised.
converts
7/2 + 371
t >
ve €Tor
X
However; in
many applications, the objective
nx (
to scalGc
function could be the output of a simulation or
number
physical system/experiment:
Classification: In-Confidence
72

![Page 2](../course.material/figs/Wk1Lecture2/page_002.png)

---

## Page 3

Khaz
ftz) &=>
Min
~foc)
Objective function
7
7
We will look at minimisation problems in this course. If
you have a maximization problem, you can always
simply reverse the sign of the objective function!
The choice of objective function is crucial for successful
design optimization. If this is done poorly, the
mathematical optimum will be non-optimal from the
engineering point of view:
A bad choice for the objective function is a common
mistake in design optimization.
Classification: In-Confidence

![Page 3](../course.material/figs/Wk1Lecture2/page_003.png)

---

## Page 4

iin   f()
7
Constraints
X1 < 372
Constiaints
71 = 0
Many optimisation problems involve constraints:
when designing a car you are limited by the
available parts, by road rules governing size, by safety
requirements etc
When grocery shopping you are limited by stock
availability, budget limits, item limits, etc.
%-372 <o|
There are two types of constraints:
Inequality constraints
0
Equality constraints (equivalent to two inequality
x2 2 0
constraints)
h(oc)
=
Xz = 0 6
4
0
Classification: In-Confidence
St
E.g:
9(x) =
36) <
71

![Page 4](../course.material/figs/Wk1Lecture2/page_004.png)

---

## Page 5

Constraints
Inequality constraints can belactivelorlinactivelat
the optimum point. An active inequality constraint
means that
g(xt)
=
0, whereas for an inactive one,
g(x*) < 0.
Value
o >*
2
5
x2
<
inactive
active
7
Classification: In-Confidence
Opfinum
3()
9(*) = 0

![Page 5](../course.material/figs/Wk1Lecture2/page_005.png)

---

## Page 6

91 < 72
Constraints
KN
92 2 0
7
ALSS
The region in which all constraints are satisfied is
called the feasible region:
If there are too many constraints, there may be no
feasible region and this makes the problem also
infeasible:
Example: if there are more independent equality
constraints than design variables, the problem is
infeasible.
Classification: In-Confidence
fecsible
Regicn

![Page 6](../course.material/figs/Wk1Lecture2/page_006.png)

---

## Page 7

Putting it all together (+notation)
obyective
dos diemin f(x)
of
2
subject to @i < Ti < #i,i = 1,2,
boundls
of
9j (x) < 0, j = 1,2,
hi(x)
=
0,7 = 1,2,
2
Ita
Classification; In-Confidence
Aumber
VGcsatle
Val
"n
number
"ng
treint
ihequal -
Con;
nh -
equG 5

![Page 7](../course.material/figs/Wk1Lecture2/page_007.png)

---

## Page 8

Notation
Yo
Ox|
point
Vectors
TA,
Ai
Matrices and elements of matrices
Aou
Ann
Optimum point x*
Classification: In-Confidence
slarting

![Page 8](../course.material/figs/Wk1Lecture2/page_008.png)

---

## Page 9

Vector and matrix norms
Ilxll >
Ilxllz
=
J5o2
nim
Il xll;
30
Ilzil
tff > = 0
Ilxllo
=
20
IIizcIl z
=
2 7*)"=
(71
2
+
+
=
4
=
(1x,f + Ixzl P+
~ -
+
L=
absolute
va lue
Suh
To
P = (
2=
Io
Max imu m
abso lute
Valu e
Ih
Vecto c
~2o
P =0 :
Classification: In-Confidence
x) h
+ 9C2
Ixa)P) '
Ix;1P ) 
Iz Ilp

![Page 9](../course.material/figs/Wk1Lecture2/page_009.png)

---

## Page 10

Mlatrices
T+
diagonal
X
A;=0   f i #j
1
In  -
Oof mh
Il I
Maz
2,
|As|
Ic
absolnte
Column
Sum
I4j< n
C= |
(
Max
IaI
OO
MG7
I< T <m
A5l
COc
23
I=1
A;
icenti-v&
0' (0 |
IAllz
(ATA)) 
2
0A Ie

![Page 10](../course.material/figs/Wk1Lecture2/page_010.png)

---

## Page 11

Ii)
Taylor
Seci-es
St)
fo) ~
f(o)
f (x0) (x-x0)
Hessica
slope
H(-)= 328 fc)
O( x-xo )
[2,fo)
22
8x,2
Bx*z
T3e4
31
Jlx) =
3 f()
=
Ox8x ,
Jf
07
Ox
3 f")(-Z)?
@xj

![Page 11](../course.material/figs/Wk1Lecture2/page_011.png)

---

