# T2-4 Linear programming

*Converted from PDF: T2-4 Linear programming.pdf*

---

## Page 1

Linear Programming
ENEL445 Applied Engineering Optimisation
2025

![Page 1](../course.material/figs/T2-4%20Linear%20programming/page_001.png)

---

## Page 2

Outline
●Linear Programs - Examples and Geometry
●Simplex Algorithm

![Page 2](../course.material/figs/T2-4%20Linear%20programming/page_002.png)

---

## Page 3

What

![Page 3](../course.material/figs/T2-4%20Linear%20programming/page_003.png)

---

## Page 4

Linear Programming
●
Linear Programming (LP) is a special case of the general 
constrained optimisation problem.
●
Objective function is linear 
●
Constraints are also linear
●
m constraints and n variables

![Page 4](../course.material/figs/T2-4%20Linear%20programming/page_004.png)

---

## Page 5

Linear Programming
minimize
+
Le
+xs
S
X1
3
+ X4
Xs
5
subject to
X3
4
X[
20, Xz 2 0, X3 > 0,
X4 2 0,
Xs > 0,
X6
20.
2x1
3x2
5x4
2x6
4x3
2x2
7x6
2x5
3x2
4x6
2x6
-3x5

![Page 5](../course.material/figs/T2-4%20Linear%20programming/page_005.png)

---

## Page 6

Why

![Page 6](../course.material/figs/T2-4%20Linear%20programming/page_006.png)

---

## Page 7

Linear Programming Applications
●
Example applications include:
■
Manufacturing and production planning
■
Telecommunications network design
■
Portfolio selection
■
Airline crew scheduling
■
DC power flow optimisation

![Page 7](../course.material/figs/T2-4%20Linear%20programming/page_007.png)

---

## Page 8

Linear Programming Applications
●
Example applications include:
■
Manufacturing and production planning
■
Telecommunications network design
■
Portfolio selection
■
Airline crew scheduling
■
DC power flow optimisation 
Objectives: The objectives typically involve minimising costs while 
ensuring operational efficiency and crew satisfaction. Costs include 
crew salaries, hotel and transportation expenses, penalties for 
violations of regulations, and potential revenue losses due to 
inefficient scheduling
Constraints: These include legal regulations (e.g., maximum duty 
time, rest requirements), crew qualifications (e.g., type ratings, 
language proficiency), operational restrictions (e.g., minimum layover 
times, crew base locations)

![Page 8](../course.material/figs/T2-4%20Linear%20programming/page_008.png)

---

## Page 9

Linear Programming Applications
●
In the 1990’s American Airline employs more than 25,000 
pilots and flight attendants to fly its fleet of over 600 aircraft.
●
Crew cost is over 1.3 billion dollars/year and is second only 
to fuel cost.
●
American Airlines spent 6000 hours of CPU time running its 
crew-pairing code to find an optimal solution.
●
Estimated savings from implementing the solution are in 
excess of 20 million dollars per year.
“Few problems studied in optimisation theory 
have greater applications in the real world”

![Page 9](../course.material/figs/T2-4%20Linear%20programming/page_009.png)

---

## Page 10

Example

![Page 10](../course.material/figs/T2-4%20Linear%20programming/page_010.png)

---

## Page 11

Linear Programming
●He is paid $10 an hour tutoring
●He is paid $7 an hour babysitting
●He wants to spend at least 3 hours, but no more than 8 
hours a week tutoring
●He wants to work for no more than 20 hours per week in 
total
How long should Elon work in each 
job to maximise his weekly earnings?

![Page 11](../course.material/figs/T2-4%20Linear%20programming/page_011.png)

---

## Page 12

●He is paid $10 an hour tutoring
●He is paid $7 an hour babysitting
●He wants to spend at least 3 hours, but no more than 8 
hours a week tutoring
●He wants to work for no more than 20 hours per week in 
total
3 ≤ T ≤ 8
B ≥ 0
T + B ≤ 20
T: Tutoring hours
B: Babysitting hours
E = 10T + 7B
Constraints
E: Earnings
Design variables
Objective function
How long should Elon work in each 
job to maximise his weekly earnings?
Linear Programming

![Page 12](../course.material/figs/T2-4%20Linear%20programming/page_012.png)

---

## Page 13

3 ≤ T ≤ 8
B ≥ 0
T + B ≤ 20
T: Tutoring hours
B: Babysitting hours
E = 10T + 7B
E: Earnings
T
B
3
8
How long should Elon work in each 
job to maximise his weekly earnings?
Linear Programming

![Page 13](../course.material/figs/T2-4%20Linear%20programming/page_013.png)

---

## Page 14

T: Tutoring hours
B: Babysitting hours
E = 10T + 7B
E: Earnings
T
B
3
8
3 ≤ T ≤ 8
B ≥ 0
B ≤  –T + 20
How long should Elon work in each 
job to maximise his weekly earnings?
Linear Programming

![Page 14](../course.material/figs/T2-4%20Linear%20programming/page_014.png)

---

## Page 15

3 ≤ T ≤ 8
B ≥ 0
E = 10T + 7B
T
B
3
8
B ≤  –T + 20
T: Tutoring hours
B: Babysitting hours
Feasible 
Region
E: Earnings
How long should Elon work in each 
job to maximise his weekly earnings?
Linear Programming

![Page 15](../course.material/figs/T2-4%20Linear%20programming/page_015.png)

---

## Page 16

E = 10T + 7B
T
B
3
8
T: Tutoring hours
B: Babysitting hours
Feasible 
Region
A
B
C
D
3 ≤ T ≤ 8
B ≥ 0
B ≤  –T + 20
E: Earnings
How long should Elon work in each 
job to maximise his weekly earnings?
Linear Programming

![Page 16](../course.material/figs/T2-4%20Linear%20programming/page_016.png)

---

## Page 17

E = 10T + 7B
T
B
3
8
T: Tutoring hours
B: Babysitting hours
Feasible 
Region
A
B
C
D
3 ≤ T ≤ 8
B ≥ 0
B ≤  –T + 20
EA(T=3,B=17) = 149
EB(T=8,B=12) = 164  
EC(T=8,B=0)   = 80  
ED(T=3,B=0)   = 30  
  
🥳
E: Earnings
How long should Elon work in each 
job to maximise his weekly earnings?
Linear Programming

![Page 17](../course.material/figs/T2-4%20Linear%20programming/page_017.png)

---

## Page 18

E = 10T + 7B
T
B
3
8
T: Tutoring hours
B: Babysitting hours
Feasible 
Region
A
B
C
D
3 ≤ T ≤ 8
B ≥ 0
B ≤  –T + 20
EA(T=3,B=17) = 149
EB(T=8,B=12) = 164  
EC(T=8,B=0)   = 80  
ED(T=3,B=0)   = 30  
  
🥳
E: Earnings
How long should Elon work in each 
job to maximise his weekly earnings?
Linear Programming

![Page 18](../course.material/figs/T2-4%20Linear%20programming/page_018.png)

---

## Page 19

The Geometry
●
Equality constraints give lines, planes, and hyperplanes.
●
Inequality constraints divide space into a halfspace in which 
the constraint is satisfied and another in which it is not.
●
Feasible set is the intersection of all halfspaces, this is called a 
polyhedron. If it's bounded and nonempty it's a polytope
●
The problem in linear programming is to find the point that lies 
in the feasible set and minimises the cost.

![Page 19](../course.material/figs/T2-4%20Linear%20programming/page_019.png)

---

## Page 20

The Geometry
●
The optimal solution occurs at a corner of the feasible set.
This is guaranteed by geometry because the constraints are 
linear.
●
Every linear programming problem falls into one of three 
possible categories:
1.
The feasible set is empty
2.
The cost function is unbounded on the feasible set
3.
The cost reaches its minimum on the feasible set

![Page 20](../course.material/figs/T2-4%20Linear%20programming/page_020.png)

---

## Page 21

How

![Page 21](../course.material/figs/T2-4%20Linear%20programming/page_021.png)

---

## Page 22

The Simplex Algorithm
Derivation Not Examinable!
Too tedious!

![Page 22](../course.material/figs/T2-4%20Linear%20programming/page_022.png)

---

## Page 23

Simplex Algorithm
●
Top 10 algorithm of the 20th century
●
Invented by George Dantzig in 1947
https://algorithmsun.wordpress.com
/4-top-10-algorithms-of-the-20th-ce
ntury-and-algorithms-in-the-news/
https://pi.math.cornell.edu/~ajt/pres
entations/TopTenAlgorithms.pdf

![Page 23](../course.material/figs/T2-4%20Linear%20programming/page_023.png)

---

## Page 24

George Dantzig
In 1939, a misunderstanding brought about surprising results. 
Near the beginning of a class, Professor Neyman wrote two 
problems on the blackboard. Dantzig arrived late and 
assumed that they were a homework assignment.
According to Dantzig, they “seemed to be a little harder than 
usual,” but a few days later he handed in completed solutions for 
both problems, still believing that they were an assignment that 
was overdue. Six weeks later, an excited Neyman eagerly told 
him that the "homework" problems he had solved were two of 
the most famous unsolved problems in statistics, and that he had 
prepared one of Dantzig's solutions for publication in a 
mathematical journal [1].
[1] Dantzig, George (1940). "On the non-existence of tests of "Student's" 
hypothesis having power functions independent of σ". The Annals of 
Mathematical Statistics. 11(2): 186–192.
https://en.wikipedia.org/wiki/George_Dantzig

![Page 24](../course.material/figs/T2-4%20Linear%20programming/page_024.png)

---

## Page 25

This story began to spread and was used as a motivational 
lesson demonstrating the power of positive thinking. Over time, 
some facts were altered, but the basic story persisted in the form 
of an urban legend and as an introductory scene in the movie 
Good Will Hunting.
George Dantzig
https://en.wikipedia.org/wiki/George_Dantzig

![Page 25](../course.material/figs/T2-4%20Linear%20programming/page_025.png)

---

## Page 26

Simplex Algorithm
●
Geometrically, travel along the vertex (corner) of polytope in 
a direction that always decrease the objective function
■
Phase I: Locate a vertex of the feasible set.
■
Phase II: Move from vertex to vertex along the edges 
of the feasible set - always go along an edge that is 
guaranteed to decrease the cost.

![Page 26](../course.material/figs/T2-4%20Linear%20programming/page_026.png)

---

## Page 27

Simplex Algorithm
1.
Convert to standard form.
2.
Gaussian eliminate until you get m solutions, Set the rest n – m 
variables to 0. This is a basic solution - you are now on a vertex.
3.
Calculate the reduced-cost coefficients, rk. 
Get the index k = q, corresponding to the minimum rk.
4.
Calculate the ratios
Get the index i = p, corresponding to minimum of those ratios.
5.
Sub                         in, reducing       to zero. This is pivoting - you 
are now on another vertex with a smaller objective function value.
6.
Goto step 3, repeat until all r are positive - You are now at the 
vertex with the smallest objective value - the optimal solution!

![Page 27](../course.material/figs/T2-4%20Linear%20programming/page_027.png)

---

## Page 28

Simplex Algorithm
1.
Convert to standard form.
2.
Gaussian eliminate until you get m solutions, Set the rest n – m 
variables to 0. This is a basic solution - you are now on a vertex.
3.
Calculate the reduced-cost coefficients, rk. 
Get the index k = q, corresponding to the minimum rk.
4.
Calculate the ratios
Get the index i = p, corresponding to minimum of those ratios.
5.
Sub                         in, reducing       to zero. This is pivoting - you 
are now on another vertex with a smaller objective function value.
6.
Goto step 3, repeat until all r are positive - You are now at the 
vertex with the smallest objective value - the optimal solution!

![Page 28](../course.material/figs/T2-4%20Linear%20programming/page_028.png)

---

## Page 29

Standard Form
●
LP problem of the form below is said to be in standard form
●
An example of non-standard form is

![Page 29](../course.material/figs/T2-4%20Linear%20programming/page_029.png)

---

## Page 30

Standard Form - Slack and Surplus Variables

![Page 30](../course.material/figs/T2-4%20Linear%20programming/page_030.png)

---

## Page 31

Standard Form - Slack and Surplus Variables

![Page 31](../course.material/figs/T2-4%20Linear%20programming/page_031.png)

---

## Page 32

Standard Form - Free Variables 
●
Free variables - variables not constrained to be ≥ 0
●
There are two ways for treating free variables:
■
Introduce two other variables that are not free
■
Get rid of free variables by Gaussian eliminations

![Page 32](../course.material/figs/T2-4%20Linear%20programming/page_032.png)

---

## Page 33

Standard Form
Example
maximize
+ 4x3
subject to
+
=X3
+
+
=
5,
+
5
2 10,
X120
X}
Xz free.
3x1
2x2
Txi
Sxz
<9,
2X1
2x2
3x3
Sxi
8x3
6x2
20,

![Page 33](../course.material/figs/T2-4%20Linear%20programming/page_033.png)

---

## Page 34

Tableau
minimize
+
+xs
~
X1
3
+ X4
Xs
5
subject to
X3
4
X[
Xz 2 0, Xy 20, x4 2 0, Xs > 0, X6
X1  X2
X3
X4
Xs   X6
b
Tableau
8 &
0
0
0
3
4
;
2
3
~4
55
1
22
2x1
3x2
4x3
5x4
2x6
2x2
2x5
7x6
3x2
4x6
2x6
-3xs
2 0,
2 0.

![Page 34](../course.material/figs/T2-4%20Linear%20programming/page_034.png)

---

## Page 35

Simplex Algorithm
1.
Convert to standard form.
2.
Gaussian eliminate until you get m solutions, Set the rest n – m 
variables to 0. This is a basic solution - you are now on a vertex.
3.
Calculate the reduced-cost coefficients, rk. 
Get the index k = q, corresponding to the minimum rk.
4.
Calculate the ratios
Get the index i = p, corresponding to minimum of those ratios.
5.
Sub                         in, reducing       to zero. This is pivoting - you 
are now on another vertex with a smaller objective function value.
6.
Goto step 3, repeat until all r are positive - You are now at the 
vertex with the smallest objective value - the optimal solution!

![Page 35](../course.material/figs/T2-4%20Linear%20programming/page_035.png)

---

## Page 36

Simplex Algorithm
1.
Convert to standard form.
2.
Gaussian eliminate until you get m solutions, Set the rest n – m 
variables to 0. This is a basic solution - you are now on a vertex.
3.
Calculate the reduced-cost coefficients, rk. 
Get the index k = q, corresponding to the minimum rk.
4.
Calculate the ratios
Get the index i = p, corresponding to minimum of those ratios.
5.
Sub                         in, reducing       to zero. This is pivoting - you 
are now on another vertex with a smaller objective function value.
6.
Goto step 3, repeat until all r are positive - You are now at the 
vertex with the smallest objective value - the optimal solution!

![Page 36](../course.material/figs/T2-4%20Linear%20programming/page_036.png)

---

## Page 37

Basic Solution
●
Perform Gaussian elimination to get m solutions, then set the 
rest n – m variables to 0. This is a basic solution

![Page 37](../course.material/figs/T2-4%20Linear%20programming/page_037.png)

---

## Page 38

Simplex Algorithm
1.
Convert to standard form.
2.
Gaussian eliminate until you get m solutions, Set the rest n – m 
variables to 0. This is a basic solution - you are now on a vertex.
3.
Calculate the reduced-cost coefficients, rk. 
Get the index k = q, corresponding to the minimum rk.
4.
Calculate the ratios
Get the index i = p, corresponding to minimum of those ratios.
5.
Sub                         in, reducing       to zero. This is pivoting - you 
are now on another vertex with a smaller objective function value.
6.
Goto step 3, repeat until all r are positive - You are now at the 
vertex with the smallest objective value - the optimal solution!

![Page 38](../course.material/figs/T2-4%20Linear%20programming/page_038.png)

---

## Page 39

Reduced-cost Coefficients
●
We want to now move to another vertex, where the solution 
may not necessarily be basic.
●
Write the first m variables in terms of the n – m as

![Page 39](../course.material/figs/T2-4%20Linear%20programming/page_039.png)

---

## Page 40

Reduced-cost Coefficients
●
Substituting the system on the previous slide back into the 
objective function, we obtain
where
And rk are known as the reduced-cost coefficients

![Page 40](../course.material/figs/T2-4%20Linear%20programming/page_040.png)

---

## Page 41

Reduced-cost Coefficients
●
f can be decreased by increasing the value of any variable 
for which rk < 0
●
In practice it is common to choose the smallest (most 
negative) reduced-cost coefficient rk  so pick the index q, 
corresponding to the minimum rk and increase xq

![Page 41](../course.material/figs/T2-4%20Linear%20programming/page_041.png)

---

## Page 42

Simplex Algorithm
1.
Convert to standard form.
2.
Gaussian eliminate until you get m solutions, Set the rest n – m 
variables to 0. This is a basic solution - you are now on a vertex.
3.
Calculate the reduced-cost coefficients, rk. 
Get the index k = q, corresponding to the minimum rk.
4.
Calculate the ratios
Get the index i = p, corresponding to minimum of those ratios.
5.
Sub                         in, reducing       to zero. This is pivoting - you 
are now on another vertex with a smaller objective function value.
6.
Goto step 3, repeat until all r are positive - You are now at the 
vertex with the smallest objective value - the optimal solution!

![Page 42](../course.material/figs/T2-4%20Linear%20programming/page_042.png)

---

## Page 43

Simplex Algorithm
1.
Convert to standard form.
2.
Gaussian eliminate until you get m solutions, Set the rest n – m 
variables to 0. This is a basic solution - you are now on a vertex.
3.
Calculate the reduced-cost coefficients, rk. 
Get the index k = q, corresponding to the minimum rk.
4.
Calculate the ratios
Get the index i = p, corresponding to minimum of those ratios.
5.
Sub                         in, reducing       to zero. This is pivoting - you 
are now on another vertex with a smaller objective function value.
6.
Goto step 3, repeat until all r are positive - You are now at the 
vertex with the smallest objective value - the optimal solution!

![Page 43](../course.material/figs/T2-4%20Linear%20programming/page_043.png)

---

## Page 44

Pivoting
●
Question: How much can xq be increased?
xq  cannot change arbitrarily. Need to satisfy Ax=b and x ≥ 0
●
For example consider variable
●xq  can only increase until x1 = 0
Giving us an increase of 
●
And similarly for all variables. So search for index p 
corresponding to the smallest of those ratios, 
●
And set

![Page 44](../course.material/figs/T2-4%20Linear%20programming/page_044.png)

---

## Page 45

Pivoting

![Page 45](../course.material/figs/T2-4%20Linear%20programming/page_045.png)

---

## Page 46

Simplex Algorithm
1.
Convert to standard form.
2.
Gaussian eliminate until you get m solutions, Set the rest n – m 
variables to 0. This is a basic solution - you are now on a vertex.
3.
Calculate the reduced-cost coefficients, rk. 
Get the index k = q, corresponding to the minimum rk.
4.
Calculate the ratios
Get the index i = p, corresponding to minimum of those ratios.
5.
Sub                         in, reducing       to zero. This is pivoting - you 
are now on another vertex with a smaller objective function value.
6.
Goto step 3, repeat until all r are positive - You are now at the 
vertex with the smallest objective value - the optimal solution!

![Page 46](../course.material/figs/T2-4%20Linear%20programming/page_046.png)

---

## Page 47

Simplex Algorithm and Beyond 
●
In practice quite fast - typically O(m) pivots.
In worst case it is exponential. 
●
For a long time it wasn’t known if there was a polynomial time 
algorithm until Khachiyan’s Algorithm
■
Exterior-point method
■
“Mathematical Sputnik of 1979”
●
Karmakar’s Method (1984)
■
Interior-point method
■
Competes viably with the simplex algorithm on 
real-world problems.

![Page 47](../course.material/figs/T2-4%20Linear%20programming/page_047.png)

---

## Page 48

https://docs.scipy.org/doc/scipy/refe
rence/optimize.linprog-simplex.html
Simplex Method

![Page 48](../course.material/figs/T2-4%20Linear%20programming/page_048.png)

---

## Page 49

https://docs.scipy.org/doc/scipy/refe
rence/optimize.linprog-highs.html#o
ptimize-linprog-highs
Simplex Method (with HiGHS)

![Page 49](../course.material/figs/T2-4%20Linear%20programming/page_049.png)

---

## Page 50

HiGHS
https Ilhighs devl
HiGHS
Linear optimization soitware
HiGHS
high performance software
HiGHS
for linear
optimization
Get started
Open source serial and parallel solvers for large-scale
Documentation
sparse linear programi
(LP) ,
Workshop 2024
mixed-integer programming (MIP), and quadratic programming (QP) Iodels
Newsletter
Download
Background
HiGHS team
iming

![Page 50](../course.material/figs/T2-4%20Linear%20programming/page_050.png)

---

## Page 51

HiGHS
https://github.com/ERGO-Code/HiGHS

![Page 51](../course.material/figs/T2-4%20Linear%20programming/page_051.png)

---

## Page 52

HiGHS
https://en.wikipedia.org/wiki/HiGHS_optimization_solver

![Page 52](../course.material/figs/T2-4%20Linear%20programming/page_052.png)

---

## Page 53

Summary
●
Linear Programming (LP) is the process of minimising a linear 
objective function subject to linear constraints.
●
Intuitively through geometry
●
Computationally through the simplex method
●
Widely applicable
●
Well-established numerical packages

![Page 53](../course.material/figs/T2-4%20Linear%20programming/page_053.png)

---

## Page 54

Exercises
●
Convert the following LP problem into standard form
●
Look up the terms that are new to you in this lecture and 
understand them.
●
Think of an LP problem that might be useful for you in 
real life with two design variables (so that it’s in 2D). 
Sketch the feasible region and solve it graphically.
≤

![Page 54](../course.material/figs/T2-4%20Linear%20programming/page_054.png)

---

## Page 55

Thanks!

![Page 55](../course.material/figs/T2-4%20Linear%20programming/page_055.png)

---

