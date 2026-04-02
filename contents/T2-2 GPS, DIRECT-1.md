# T2-2 GPS, DIRECT-1

*Converted from PDF: T2-2 GPS, DIRECT-1.pdf*

---

## Page 1

GPS and DIRECT
ENEL445 Applied Engineering Optimisation
2025

![Page 1](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_001.png)

---

## Page 2

Outline
●GPS - Generalised Pattern Search
●Shubert Algorithm
●DIRECT - DIviding RECTangles

![Page 2](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_002.png)

---

## Page 3

GPS

![Page 3](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_003.png)

---

## Page 4

GPS

![Page 4](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_004.png)

---

## Page 5

1.
Start with a point (an initial guess).
2.
Explore nearby points by moving along certain directions 
(like north, south, east, west, or more general patterns).
3.
Evaluate the function at these nearby points.
4.
If one of the new points is better (lower function value for 
minimisation), move there.
5.
If no improvement is found, shrink the step size (search 
smaller neighbourhoods).
6.
Repeat steps 2–5 until you can't find better points or the 
step size gets very tiny.
GPS

![Page 5](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_005.png)

---

## Page 6

1.
Start with a point (an initial guess).
2.
Explore nearby points by moving along certain directions 
(like north, south, east, west, or more general patterns).
3.
Evaluate the function at these nearby points.
4.
If one of the new points is better (lower function value for 
minimisation), move there.
5.
If no improvement is found, shrink the step size (search 
smaller neighbourhoods).
6.
Repeat steps 2–5 until you can't find better points or the 
step size gets very tiny.
GPS
Meshing
Polling

![Page 6](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_006.png)

---

## Page 7

Positive Spanning Set
●
Given a set of vectors 𝐷 = {𝑑1, 𝑑2, ..., 𝑑𝑛}, the set 𝐷 is a 
positive spanning set if the vectors are: 
■
Linearly independent 
■
A non-negative linear combination of these 
vectors spans the 𝑛-dimensional space.

![Page 7](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_007.png)

---

## Page 8

Positive Spanning Set
●
We only consider linear combinations with positive multipliers 
e.g. in 2D, the unit coordinate vectors ê1 and ê2 are not sufficient 
to span the space; however, the set below are sufficient:
●
For a given dimension 𝑛, the largest number of vectors that could 
be used while remaining linearly independent (known as the 
maximal set) is 2𝑛.
●
Conversely, the minimum number of possible vectors needed to 
span the space (known as the minimal set) is 𝑛 + 1.

![Page 8](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_008.png)

---

## Page 9

Positive Spanning Set
●
A common default for a maximal set is the set of all 
coordinate directions ±ê𝑖
●
A potential default minimal set is the positive coordinate 
directions +ê𝑖 and a vector filled with −1 (or more 
generally, the negative sum of the other vectors)

![Page 9](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_009.png)

---

## Page 10

Meshing
●
The vectors from the spanning set are then used to create 
a mesh.
●
Given a mesh size Δ𝑘 and a current centre point 𝑥𝑘 which 
is the best point found so far, the mesh is created by
●
For example, in 2D, if the current point is 𝑥𝑘 = [1, 1], the 
mesh size is Δ𝑘 = 0.5, and we use the minimal spanning 
set in 2D space, the mesh points would be:

![Page 10](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_010.png)

---

## Page 11

GPS

![Page 11](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_011.png)

---

## Page 12

Polling
●
Full polling
Evaluate every point on the mesh.
●
Opportunistic polling
Decide on an order to evaluate each mesh point, stop at 
the first point that offers improvement.
●
Dynamic polling
A successful poll reorders the direction vectors so that 
the direction that was successful last time is checked 
first in the next poll.

![Page 12](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_012.png)

---

## Page 13

GPS convergence
●
The convergence of the GPS algorithm is often 
determined by:
■
A user-specified maximum number of iterations
■
A threshold on mesh size
■
A threshold on the improvement in the function 
value over previous iterations.

![Page 13](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_013.png)

---

## Page 14

GPS with constraints
●
GPS can handle linear and nonlinear constraints. For 
linear constraints, one effective strategy is to change the 
positive spanning directions so that they align with any 
linear constraints that are nearby.

![Page 14](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_014.png)

---

## Page 15

GPS extension - MADS 
●
Mesh Adaptive Direct Search (MADS) algorithm
Increases the number of polling directions 
●
NOMAD software is an open-source implementation of MADS.
Audet & Dennis, “Mesh adaptive 
direct search algorithms for 
constrained optimization”, 2006.
Digabel, “Algorithm 909: NOMAD: Nonlinear optimization with the 
MADS algorithm”, 2011.

![Page 15](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_015.png)

---

## Page 16

Shubert’s Algorithm
Franz Schubert

![Page 16](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_016.png)

---

## Page 17

Lipschitz Continuity
●
A function 𝑓 is said to be Lipschitz continuous if
●
Graphically, this condition means that we can draw a cone 
with slope 𝐿 from any point such that the function is always 
bounded by the cone.

![Page 17](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_017.png)

---

## Page 18

k=0
k=1
k=2
k=3
Shubert’s Algorithm

![Page 18](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_018.png)

---

## Page 19

Shubert’s Algorithm

![Page 19](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_019.png)

---

## Page 20

Shubert’s Algorithm
●
The Lipschitz cone intersections are the lower bounds!
●
The lower bound on the function increases at each 
iteration and ultimately converges to the global minimum
●
The two significant shortcomings of Shubert’s algorithm 
are: 
■
A Lipschitz constant is usually not available 
■
It is not easily extended to 𝑛 dimensions
The DIRECT algorithm addresses these two shortcomings.

![Page 20](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_020.png)

---

## Page 21

DIRECT
DIviding RECTangles
Jones, Perttunen, & Stuckman, (1993). “Lipschitzian optimization without 
the Lipschitz constant”. Journal of optimization Theory and Applications, 
79, 157-181.
Jones & Martins, (2021). “The DIRECT algorithm: 25 years Later”. Journal 
of global optimization, 79(3), 521-566.

![Page 21](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_021.png)

---

## Page 22

DIRECT
●
A deterministic method guaranteed to converge to the 
global optimum (although it might still require a prohibitive 
number of function evaluations).
●
Like many other gradient-free methods, DIRECT requires 
upper and lower bounds on all the design variables.
●
An exhaustive search finds the global optimum within a 
finite design space by dividing this space into a grid and 
evaluating every point on this grid. The DIRECT method 
also relies on a grid, but it adaptively chooses which grid 
points to evaluate, dramatically reducing the cost.

![Page 22](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_022.png)

---

## Page 23

DIRECT
●
Because DIRECT assumes lower and upper bounds, 
we can, without loss of generality, normalise the design 
variables to [0, 1] so that the search space becomes the 
unit hypercube.
●
DIRECT works by subdividing the unit hypercube into 
subrectangles and evaluating each rectangle’s centre 
point.
●
Then “potentially optimal” rectangles are selected.
●
The selected potentially optimal rectangles are further 
subdivided and the objective function is evaluated at the 
centre points of the newly-formed subrectangles

![Page 23](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_023.png)

---

## Page 24

f
X1
X2
X1
X3
X
+L
f(c) - ZL(b _ a)
d =
2(b _ a)
C =
Z(a + b)
C =
Z(a + b)

![Page 24](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_024.png)

---

## Page 25

Iteration
Select rectangles
Trisect and sample
Point-shift
2
3

![Page 25](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_025.png)

---

## Page 26

Potentially Optimal Rectangles
●
Definition: Suppose we have a partition of the unit 
hypercube into m rectangles. Let:
ci denote the centre point of the i th rectangle.
di denote the distance from the centre to the vertices.
ε > 0 be a small positive constant. 
A rectangle j is said to be potentially optimal if there exists 
some K > 0 such that:
(1)
(2)

![Page 26](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_026.png)

---

## Page 27

●
We don’t have the Lipschitzian constant K: Use an f-d plot
f(c)
(1)
Potentially Optimal Rectangles
Convex hull

![Page 27](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_027.png)

---

## Page 28

f(c)
●
We don’t have the Lipschitzian constant K: Use an f-d plot
Potentially Optimal Rectangles
These are the rectangles 
that will be subdivided next
(2)

![Page 28](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_028.png)

---

## Page 29

Aside: Wrapping Gifts
https://en.wikipedia.org/wiki/Gift_wrapping_algorithm
●
Efficient algorithms for finding the convex hull of an arbitrary 
set of points in two dimensions, such as the Jarvis march
Jarvis, “On the identification of the 
convex hull of a finite set of points in 
the plane” (1973).

![Page 29](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_029.png)

---

## Page 30

DIRECT Results
Branin test problem
Six-hump Camel test problem

![Page 30](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_030.png)

---

## Page 31

DIRECT Results
Simultaneous search for multiple QTL using the
OIL
global optimization algorithm DIRECT
FREE
More images
K Ljungberg >
S.
Holmgren, 0. Carlborg
Bioinformatics, Volume 20, Issue 12,August 2004,Pages 1887-1895, https:| Idoi.org/
Quantitative trait locus
Abstract
A quantitative trait locus is a locus that correlates with
Motivation: A simultaneous search is necessary for maximizing the power to
variation of a quantitative trait in the phenotype of a
detect epistatic quantitative trait loci (QTL) The computational complexity
population of organisms. QTLs are mapped by
demands that the traditional exhaustive search be replaced by a more efficient
identifying which molecular markers correlate with an
observed trait: Wikipedia
global optimization algorithm:
2200
2200
2100
2100
2000
2000
"8
1900
1900
3
1800
3
1800
3
8
1700
8
1700
1600
1600
L
1500
L
1500
1400
1400
1300
4
1300
GA
DIRECT
1200
1200
400
600
800
1000
1200
1400
1600
400
600
800
1000
1200
1400
1600
Position QTL IlcM
Position QTL 1 /cM

![Page 31](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_031.png)

---

## Page 32

Dynamic Primitives Facilitate Manipulating a Whip
DIRECT
by
Results
Moses C. Nah
Submitted to the Department of Mechanical Engineering
on
15, 2020, in partial fulfillment of the
requirements for the degree of
Master of Science in Mechanical Engineering
Abstract
Human dexterity far exceeds that of modern robots, despite a much slower neuromus-
cular system.
Understanding how this is accomplished may lead to improved robot
control_
The slow neuromuscular system of humans implies that prediction based on
some form of internal model plays a prominent role
However , the nature of the model
itself remains unclear. To address this problem; we focused on one ofthe most complex
and exotic tools humans can manipulate
a whip. We tested (in simulation) whether
a distant target could be reached with a
(small) number of dynamic
primitives, whose parameters could be learned through optimization: This approach
was able to manage the complexity of an (extremely) high degree-of-freedom system
and
discovered the optimal parameters of the upper-limb
movement that achieved
the task:
A detailed model of the whip dynamics was not needed for this approach,
which thereby significantly relieved the computational burden of task representation
and performance optimization:
These results support our hypothesis that compos-
control using dynamic motor primitives may be a strategy which humans use to
enable their remarkable dexterity:
A similar approach
may contribute to improved
robot control
May
whip
using
ing

![Page 32](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_032.png)

---

## Page 33

*[Page appears blank or contains only images]*

![Page 33](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_033.png)

---

## Page 34

(A.l)
(A.2)
(A.3)
(B.1)
(B.2)
(B.3)
(C.1)
(C.2)
(C.3)
Figure 7-9:
Time sequence of the simulation of the whip task:
(A) Short-whip (B)
Medium-whip (C) Long-whip.
Each upper-limb movement
was
generated with the
optimal movement parameters, which yielded the minimum distance L* [Table 7.3].

![Page 34](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_034.png)

---

## Page 35

Short-whip
Medium-whip
whip
2.4
1.8
1
+
1.2
0.6
120
240
360
480
600
Iteration [~]
Figure 7-10: Optimization results for the three whip models. 600 iterations were conducted with the DIRECT-L algorithm.
Long-

![Page 35](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_035.png)

---

## Page 36

DIRECT
●
DIRECT always subdivides one of the largest rectangles 
during each iteration. Therefore, as the iterations go to 
infinity, the size of the largest rectangle must approach zero. 
●
As a result, for any point x in the initial hypercube and for any 
small δ > 0, DIRECT is guaranteed to sample a point within a 
distance δ of x after some finite (possibly very large) number 
of iterations.
●
While DIRECT does have one hyperparameter (the desired 
accuracy), this parameter’s purpose is not so much to set the 
overall local-global balance as it is to make sure that 
DIRECT does not get too local in its search, wasting function 
evaluations in pursuit of very small improvements.

![Page 36](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_036.png)

---

## Page 37

https://repository.lib.ncsu.edu/items/cfdebcfc-8f51-4dbe-a7b8-9634a9b0f9a5

![Page 37](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_037.png)

---

## Page 38

DIRECT Advantages
●
No need to assume the availability of gradients or other 
special information about the objective function.
●
It is guaranteed to converge to the global minimum if the 
function is continuous.
●
Deterministic algorithm, so there is no need for multiple runs.
●
All function evaluations can be done in parallel.
●
No hyperparameters that set the balance between local and 
global search needed. This is accomplished by selecting all 
those rectangles that would have the lowest lower bound for 
some Lipschitz constant, where small constants select 
rectangles good for local search, and large constants select 
those good for global search.

![Page 38](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_038.png)

---

## Page 39

https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.direct.html

![Page 39](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_039.png)

---

## Page 40

Exercises
●
Go through the lecture slides and note down all the 
terminologies unfamiliar to you and make sure you 
understand them.
●
Select a dimension and draw a maximal/minimal 
positive spanning set of vectors in that dimension.
●
Take 15 min to read Jones & Martins (2021) and 
understand how the DIRECT algorithm works.
Jones & Martins, (2021). “The DIRECT algorithm: 25 years Later”. Journal 
of global optimization, 79(3), 521-566.

![Page 40](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_040.png)

---

## Page 41

SSitev sutttss stovies , sbiight to yOut
DOxIDIRECT
No. 01
MoxDAx , SEPTEMBER 3 OTE 2013
FREE
Doxcirect FREE posters help fnd MOWvellous Sebby:
CAT
ASTROPHE
AVERTED
scctn !

![Page 41](../course.material/figs/T2-2%20GPS%2C%20DIRECT-1/page_041.png)

---

