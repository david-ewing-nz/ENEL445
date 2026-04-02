# T2-5 Discrete

*Converted from PDF: T2-5 Discrete.pdf*

---

## Page 1

Diet Problem Formulation
https://www.youtube.com/watch?v=O8Nu_yLaTMs

![Page 1](../course.material/figs/T2-5%20Discrete/page_001.png)

---

## Page 2

https://www.youtube.com/watch?v=O8Nu_yLaTMs

![Page 2](../course.material/figs/T2-5%20Discrete/page_002.png)

---

## Page 3

Two Linear Programming Applications

![Page 3](../course.material/figs/T2-5%20Discrete/page_003.png)

---

## Page 4

Two special LP problems
●
Two special linear programming problems that have been 
applied in many real life situations are:
■
Transportation Problems
■
Assignment Problems
●
They usually require a very large number of constraints and 
variables
●
However, the coefficient matrices of both problems have 
special structures. Because of this we can develop very 
simplified versions of the Simplex method for solving these 
problems that achieve dramatic computational savings

![Page 4](../course.material/figs/T2-5%20Discrete/page_004.png)

---

## Page 5

Transportation Problem

![Page 5](../course.material/figs/T2-5%20Discrete/page_005.png)

---

## Page 6

Transportation Problem
●
A commodity is available at 
each of the m sources in 
a1, a2, …, am units
●
This commodity is required at 
each of the n destinations in 
b1, b2, …, bn units 
●
cij are the per unit cost of 
transportation of commodity 
from the ith source to the jth 
destination. 
●
Problem: How many units of the given commodity should be 
transported from each source to each destination so that the 
total cost of the transportation is minimum and meet the 
requirements?

![Page 6](../course.material/figs/T2-5%20Discrete/page_006.png)

---

## Page 7

Transportation Problem
●
Design variables: xij units of commodity to be transported 
from the i th source to the j th destination, costing:
●
Constraints:
1.
From any source, we should not transport more than 
what is available.
2.
To every destination we should transport at least what 
is required.
3.
We cannot transport negative units of commodity.

![Page 7](../course.material/figs/T2-5%20Discrete/page_007.png)

---

## Page 8

Transportation Problem
●
The transportation problem is balanced if all source and 
destination constraints are equalities.
●
Such a condition is feasible if and only if:
●
This means the total supply from all sources is equal to the 
total demand from all destinations

![Page 8](../course.material/figs/T2-5%20Discrete/page_008.png)

---

## Page 9

Transportation Problem
n
Xij = Qi
Xij = bj
1
31
i =1
X11 +
t.+
=
41
X21
+ X22 + .
+
=
02
+
+
+
=
am
=
b1
X11
=
b2
X12
=
2
Xin
X12
X2n
Xmn
Xm2
Xml
+Xml
+X21
+Xm2
+X22
bm:
+Xmn
+X2n
Xin

![Page 9](../course.material/figs/T2-5%20Discrete/page_009.png)

---

## Page 10

Transportation Problem
●
Northwest Corner Rule
●
Vogel’s Approximation Method

![Page 10](../course.material/figs/T2-5%20Discrete/page_010.png)

---

## Page 11

Assignment Problem

![Page 11](../course.material/figs/T2-5%20Discrete/page_011.png)

---

## Page 12

Example 1: Job Assignment 
●
Assigning n persons to n jobs.
●
The i th person charges cij to complete the j th job.
Problem: Determine the assignment of persons to jobs so that 
the total cost of completing all jobs is minimised
Constraints: 
1.
Only one person is to be assigned to one job
2.
Only one job is to be assigned to a person

![Page 12](../course.material/figs/T2-5%20Discrete/page_012.png)

---

## Page 13

Example 2: TA Assignment to Courses

![Page 13](../course.material/figs/T2-5%20Discrete/page_013.png)

---

## Page 14

Example 3: Hospital-Patient Matching

![Page 14](../course.material/figs/T2-5%20Discrete/page_014.png)

---

## Page 15

Example 4: Flights-to-Gates Assignment

![Page 15](../course.material/figs/T2-5%20Discrete/page_015.png)

---

## Page 16

Example 5: Student-Project Allocation

![Page 16](../course.material/figs/T2-5%20Discrete/page_016.png)

---

## Page 17

Hungarian Algorithm
●
Published in 1955 by Harold Kuhn, who gave it the name 
“Hungarian method” because the algorithm was largely 
based on the earlier works of two Hungarian 
mathematicians, Dénes Kőnig and Jenő Egerváry.
●
Also called the Munkres assignment algorithm
●
O(n3) vs O(n!)

![Page 17](../course.material/figs/T2-5%20Discrete/page_017.png)

---

## Page 18

Hungarian Algorithm
Example 1

![Page 18](../course.material/figs/T2-5%20Discrete/page_018.png)

---

## Page 19

Hungarian Algorithm 
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.
Flowers
Cake
Photographer
Alice
55
30
25
Bob
40
60
15
Charlie
25
30
45

![Page 19](../course.material/figs/T2-5%20Discrete/page_019.png)

---

## Page 20

Hungarian Algorithm 
Flowers
Cake
Photographer
Alice
55
30
25
Bob
40
60
15
Charlie
25
30
45
30    5     0
25  45     0
  0    5   20
1.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 20](../course.material/figs/T2-5%20Discrete/page_020.png)

---

## Page 21

Hungarian Algorithm 
Flowers
Cake
Photographer
Alice
55
30
25
Bob
40
60
15
Charlie
25
30
45
30    5     0
25  45     0
  0    5   20
1.
30    0     0
25  40     0
  0    0   20
2.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 21](../course.material/figs/T2-5%20Discrete/page_021.png)

---

## Page 22

Hungarian Algorithm 
Flowers
Cake
Photographer
Alice
55
30
25
Bob
40
60
15
Charlie
25
30
45
30    5     0
25  45     0
  0    5   20
1.
30    0     0
25  40     0
  0    0   20
2.
3.
30    0     0
25  40     0
  0    0   20
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 22](../course.material/figs/T2-5%20Discrete/page_022.png)

---

## Page 23

Hungarian Algorithm 
Flowers
Cake
Photographer
Alice
55
30
25
Bob
40
60
15
Charlie
25
30
45
30    5     0
25  45     0
  0    5   20
1.
30    0     0
25  40     0
  0    0   20
2.
3.
30    0     0
25  40     0
  0    0   20
4.
30    0     0
25  40     0
  0    0   20
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 23](../course.material/figs/T2-5%20Discrete/page_023.png)

---

## Page 24

Hungarian Algorithm 
Flowers
Cake
Photographer
Alice
55
30
25
Bob
40
60
15
Charlie
25
30
45
30    5     0
25  45     0
  0    5   20
1.
30    0     0
25  40     0
  0    0   20
2.
3.
30    0     0
25  40     0
  0    0   20
4.
30    0     0
25  40     0
  0    0   20
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 24](../course.material/figs/T2-5%20Discrete/page_024.png)

---

## Page 25

Hungarian Algorithm 
Flowers
Cake
Photographer
Alice
55
30
25
Bob
40
60
15
Charlie
25
30
45
30    5     0
25  45     0
  0    5   20
1.
30    0     0
25  40     0
  0    0   20
2.
3.
30    0     0
25  40     0
  0    0   20
4.
30    0     0
25  40     0
  0    0   20
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 25](../course.material/figs/T2-5%20Discrete/page_025.png)

---

## Page 26

Hungarian Algorithm 
Flowers
Cake
Photographer
Alice
55
30
25
Bob
40
60
15
Charlie
25
30
45
30    5     0
25  45     0
  0    5   20
1.
30    0     0
25  40     0
  0    0   20
2.
3.
30    0     0
25  40     0
  0    0   20
4.
30    0     0
25  40     0
  0    0   20
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 26](../course.material/figs/T2-5%20Discrete/page_026.png)

---

## Page 27

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
55
30
25
Bob
40
60
15
Charlie
25
30
45
30    5     0
25  45     0
  0    5   20
1.
30    0     0
25  40     0
  0    0   20
2.
3.
30    0     0
25  40     0
  0    0   20
4.
30    0     0
25  40     0
  0    0   20
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 27](../course.material/figs/T2-5%20Discrete/page_027.png)

---

## Page 28

Hungarian Algorithm
Example 2

![Page 28](../course.material/figs/T2-5%20Discrete/page_028.png)

---

## Page 29

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
30
25
10
Bob
15
10
20
Charlie
25
20
15
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 29](../course.material/figs/T2-5%20Discrete/page_029.png)

---

## Page 30

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
30
25
10
Bob
15
10
20
Charlie
25
20
15
20  15     0
  5    0   10
10    5     0
1.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 30](../course.material/figs/T2-5%20Discrete/page_030.png)

---

## Page 31

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
30
25
10
Bob
15
10
20
Charlie
25
20
15
20  15     0
  5    0   10
10    5     0
1.
15  15     0
  0    0   10
  5    5     0
2.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 31](../course.material/figs/T2-5%20Discrete/page_031.png)

---

## Page 32

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
30
25
10
Bob
15
10
20
Charlie
25
20
15
20  15     0
  5    0   10
10    5     0
1.
15  15     0
  0    0   10
  5    5     0
2.
15  15     0
  0    0   10
  5    5     0
3.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 32](../course.material/figs/T2-5%20Discrete/page_032.png)

---

## Page 33

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
30
25
10
Bob
15
10
20
Charlie
25
20
15
20  15     0
  5    0   10
10    5     0
1.
15  15     0
  0    0   10
  5    5     0
2.
15  15     0
  0    0   10
  5    5     0
3.
10  10     0
  0    0     5
  0    0     0
4.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 33](../course.material/figs/T2-5%20Discrete/page_033.png)

---

## Page 34

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
30
25
10
Bob
15
10
20
Charlie
25
20
15
20  15     0
  5    0   10
10    5     0
1.
15  15     0
  0    0   10
  5    5     0
2.
15  15     0
  0    0   10
  5    5     0
3.
10  10     0
  0    0     5
  0    0     0
4.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 34](../course.material/figs/T2-5%20Discrete/page_034.png)

---

## Page 35

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
30
25
10
Bob
15
10
20
Charlie
25
20
15
20  15     0
  5    0   10
10    5     0
1.
15  15     0
  0    0   10
  5    5     0
2.
15  15     0
  0    0   10
  5    5     0
3.
10  10     0
  0    0     5
  0    0     0
4.
10  10     0
  0    0     5
  0    0     0
5.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 35](../course.material/figs/T2-5%20Discrete/page_035.png)

---

## Page 36

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
30
25
10
Bob
15
10
20
Charlie
25
20
15
20  15     0
  5    0   10
10    5     0
1.
15  15     0
  0    0   10
  5    5     0
2.
15  15     0
  0    0   10
  5    5     0
3.
10  10     0
  0    0     5
  0    0     0
4.
10  10     0
  0    0     5
  0    0     0
5.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 36](../course.material/figs/T2-5%20Discrete/page_036.png)

---

## Page 37

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
30
25
10
Bob
15
10
20
Charlie
25
20
15
20  15     0
  5    0   10
10    5     0
1.
15  15     0
  0    0   10
  5    5     0
2.
15  15     0
  0    0   10
  5    5     0
3.
10  10     0
  0    0     5
  0    0     0
4.
10  10     0
  0    0     5
  0    0     0
5.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 37](../course.material/figs/T2-5%20Discrete/page_037.png)

---

## Page 38

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
30
25
10
Bob
15
10
20
Charlie
25
20
15
20  15     0
  5    0   10
10    5     0
1.
15  15     0
  0    0   10
  5    5     0
2.
15  15     0
  0    0   10
  5    5     0
3.
10  10     0
  0    0     5
  0    0     0
4.
10  10     0
  0    0     5
  0    0     0
5.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 38](../course.material/figs/T2-5%20Discrete/page_038.png)

---

## Page 39

Hungarian Algorithm
Flowers
Cake
Photographer
Alice
30
25
10
Bob
15
10
20
Charlie
25
20
15
20  15     0
  5    0   10
10    5     0
1.
15  15     0
  0    0   10
  5    5     0
2.
15  15     0
  0    0   10
  5    5     0
3.
10  10     0
  0    0     5
  0    0     0
4.
10  10     0
  0    0     5
  0    0     0
5.
1.
Subtract min of row from each row.
2.
Subtract min of col from each col.
3.
Draw lines to cover all zeros.
4.
If number of lines is equal to the number of 
rows and cols, then an optimal assignment 
is an unique zeros assignment to each row 
and col
Else, subtract the min of all uncovered 
elements in step 4. Go back to step 3.

![Page 39](../course.material/figs/T2-5%20Discrete/page_039.png)

---

## Page 40

Num Worker ≠ Num Tasks
https://en.wikipedia.org/wiki/Assignment_probl
em#/media/File:Hungarian_algorithm_unbalan
ced_assignment_problem_example.svg

![Page 40](../course.material/figs/T2-5%20Discrete/page_040.png)

---

## Page 41

Hungarian Algorithm
https://docs.scipy.org/doc/scipy/reference/genera
ted/scipy.optimize.linear_sum_assignment.html

![Page 41](../course.material/figs/T2-5%20Discrete/page_041.png)

---

## Page 42

Extensions and More to Explore
●
Very close connections between the transportation and 
assignment problems to graph theory.
●
A very natural extension of the transportation problem is the 
multi-commodity transportation problem.
●
If we allow that an item may reach a destination via another 
source or via another destination or a combination of these, 
then the transportation problem is called the transhipment 
problem. The transhipment problem can be transformed into 
the usual transportation problem with m+n sources and m+n 
destination and then solved by the usual algorithm.
●
The assignment problem is also related to the travelling 
salesperson problem (TSP). Solving an n-city TSP is 
equivalent to finding a cyclic solution to the usual n-person, 
n-jobs assignment problem.

![Page 42](../course.material/figs/T2-5%20Discrete/page_042.png)

---

## Page 43

The Job Assignment Example LP Formulation
●
Assigning n persons to n jobs.
●
The i th person charges cij to complete the j th job.
Problem: Determine the assignment of persons to jobs so that 
the total cost of completing all jobs is minimised
Constraints: 
1.
Only one person is to be assigned to one job
2.
Only one job is to be assigned to a person

![Page 43](../course.material/figs/T2-5%20Discrete/page_043.png)

---

## Page 44

The Job Assignment Example LP Formulation

![Page 44](../course.material/figs/T2-5%20Discrete/page_044.png)

---

## Page 45

Assignment Problem 
●
Design variables: xij

![Page 45](../course.material/figs/T2-5%20Discrete/page_045.png)

---

## Page 46

Discrete Optimisation

![Page 46](../course.material/figs/T2-5%20Discrete/page_046.png)

---

## Page 47

Outline
●Discrete Optimisation Motivation
●Branch and Bound
 
●Greedy Algorithm

![Page 47](../course.material/figs/T2-5%20Discrete/page_047.png)

---

## Page 48

Discrete Optimisation
●
Common examples of discrete optimisation include:
■
Scheduling
■
Network problems
■
Resource allocation
●
Concrete examples include:
■
Power plants on/off
■
Number of wheels on a vehicle
■
The material in a structure that is restricted to 
titanium, steel, or aluminum
■
The traveling salesperson problem (TSP)
●
Discrete optimization is also known as: 
integer programming or combinatorial optimisation
●
Problems with both continuous and discrete variables are 
referred to as mixed-integer programming

![Page 48](../course.material/figs/T2-5%20Discrete/page_048.png)

---

## Page 49

Discrete Optimisation Complexity
●
Discrete optimisation is nondeterministic polynomial-time 
complete, or NP-complete: we can easily verify a solution, 
but there is no known approach to find a solution efficiently. 
●
The time required to solve discrete problems become much 
worse as the problem size grows. So exhaustive search is 
well, exhausting!
●
Example: TSP with 20 cities: (20-1)! = 19! possibilities

![Page 49](../course.material/figs/T2-5%20Discrete/page_049.png)

---

## Page 50

Avoiding Discrete Optimisation
●
Even though a discrete optimisation problem limits the options 
and thus conceptually sounds easier to solve, discrete 
optimisation problems are usually much more challenging to 
solve than continuous problems.
●
Methods to avoid discrete optimisation include:
■
Exhaustive search: We may have only a few discrete 
variables with few options. In that case, enumerating all 
options is possible.
■
Rounding: We can optimise the discrete design 
variables as if they were continuous and round the 
optimal design variable to integer values afterward.
■
Dynamic rounding: Round only a subset of the 
discrete variables, fix them, and re-optimizes the 
remaining variables using continuous optimisation. The 
process is repeated until all discrete variables are fixed.

![Page 50](../course.material/figs/T2-5%20Discrete/page_050.png)

---

## Page 51

●
We can convert a discrete optimisation problem into a binary 
discrete one by adding additional variables and constraints. 
Although the new problem is larger, it is usually far easier to 
solve.
●
Example: An engineering structure may use one of 𝑛 different 
materials. Convert the problem to have 𝑛 binary variables 𝑥𝑖
●
We would also need to add an additional constraint to make 
sure that one (and only one) material is selected:
Embracing Discrete Optimisation

![Page 51](../course.material/figs/T2-5%20Discrete/page_051.png)

---

## Page 52

Branch and Bound
(B&B)

![Page 52](../course.material/figs/T2-5%20Discrete/page_052.png)

---

## Page 53

Branch and Bound
●
B&B was first proposed by Ailsa Land and Alison Doig at the 
London School of Economics in 1960 for discrete 
programming and has become the most commonly used tool 
for solving NP-hard optimisation problems.
●
B&B algorithm involves:
■
Branching: Splits the search space into smaller spaces, 
then minimise f(x) in these smaller spaces.
■
Bounding: Keeps track of the minimum so far and use 
this to eliminate branches
■
Relaxation: Aims to construct an approximation of the 
original optimisation problem that is easier to solve.

![Page 53](../course.material/figs/T2-5%20Discrete/page_053.png)

---

## Page 54

●
Splits the search space into smaller spaces, then minimise 
f(x) in these smaller spaces.
●
Branching is done by adding constraints
Branching

![Page 54](../course.material/figs/T2-5%20Discrete/page_054.png)

---

## Page 55

●
Branching by itself would amount to brute-force enumeration 
of candidate solutions and testing them all. 
●
To improve on the performance of an exhaustive search, the 
B&B algorithm keeps track of bounds on the minimum, and 
uses this bound to prune the search space, eliminating 
candidate solutions that we know will not contain an optimal 
solution.
Bounding

![Page 55](../course.material/figs/T2-5%20Discrete/page_055.png)

---

## Page 56

●
Approximate the original optimisation problem such that is 
easier to solve.
●
Such approximations are often accomplished by removing, 
or ”relaxing” constraints.
●
For example if 𝑥𝑖 = 0 or 1 relax this to 
Relaxation

![Page 56](../course.material/figs/T2-5%20Discrete/page_056.png)

---

## Page 57

Example 1
●
Relax the binary problem and solve with continuous bounds: 
0 ≤ 𝑥𝑖 ≤ 1

![Page 57](../course.material/figs/T2-5%20Discrete/page_057.png)

---

## Page 58

Example 1
X
=
[1,0.53,0.50,1]t
f*
=
55.03

![Page 58](../course.material/figs/T2-5%20Discrete/page_058.png)

---

## Page 59

Example 1
●
Branch on the variable with the most fractional component

![Page 59](../course.material/figs/T2-5%20Discrete/page_059.png)

---

## Page 60

Example 1
●
Branch on the variable with the most fractional component.
●
Add the constraints 𝑥3 = 0 and 𝑥3 = 1 to form two branches.

![Page 60](../course.material/figs/T2-5%20Discrete/page_060.png)

---

## Page 61

Example 1
●
Branch on the variable with the most fractional component.
●
Add the constraints 𝑥3 = 0 and 𝑥3 = 1 to form two branches.
●
Solve

![Page 61](../course.material/figs/T2-5%20Discrete/page_061.png)

---

## Page 62

Example 1
●
Neither of these optimizations yields all binary values, so we 
have to branch both of them.

![Page 62](../course.material/figs/T2-5%20Discrete/page_062.png)

---

## Page 63

Example 1
●
Neither of these optimizations yields all binary values, so we 
have to branch both of them.
●
In this case, the left node branches on 𝑥2 (the only fractional 
component), and the right node also branches on 𝑥2 (the 
most fractional component).
𝑥2 =

![Page 63](../course.material/figs/T2-5%20Discrete/page_063.png)

---

## Page 64

Example 1
●
The first branch yields a feasible binary solution. The 
corresponding objective function value 𝑓 = −4 is saved as the 
best value so far. There is no need to continue on this branch 
because the solution cannot be improved on this particular 
branch.
𝑥2 =

![Page 64](../course.material/figs/T2-5%20Discrete/page_064.png)

---

## Page 65

Example 1
●
Solve branch 2
𝑥2 =

![Page 65](../course.material/figs/T2-5%20Discrete/page_065.png)

---

## Page 66

Example 1
●
Solve branch 3 - yields a feasible binary solution.
𝑥2 =

![Page 66](../course.material/figs/T2-5%20Discrete/page_066.png)

---

## Page 67

Example 1
●
Branch 1 and 2 have a lower-bound that is worse than the 
best solution so far. Thus, we can prune both of these 
branches.
𝑥2 =
x
x

![Page 67](../course.material/figs/T2-5%20Discrete/page_067.png)

---

## Page 68

Example 1
●
Solve branch 4
𝑥2 =
x
x

![Page 68](../course.material/figs/T2-5%20Discrete/page_068.png)

---

## Page 69

Example 1
●
Branch 4 has a lower bound that is worse than the best 
solution so far. Thus, we can prune that branch too.
𝑥2 =
x
x
x

![Page 69](../course.material/figs/T2-5%20Discrete/page_069.png)

---

## Page 70

Example 1
●
All branches have been pruned, we have solved the original 
problem.
𝑥2 =
x
x
x

![Page 70](../course.material/figs/T2-5%20Discrete/page_070.png)

---

## Page 71

●
The solution from a relaxed problem provides a lower bound 
- the best that could be achieved if continued on that branch.
●
This is because adding constraints (i.e. branching) always 
leads to a solution that is either the same or worse, never 
better.
●
One common strategy is to branch on the variable with the 
largest fractional component.
●
For example, if 𝑥 = [1.0, 0.4, 0.9, 0.0], we could branch on 𝑥2 
or 𝑥3 because both are fractional. But we are more likely to 
force the algorithm to make faster progress by branching on 
variables that are furthest away from integers. In this case, 
that value would be 𝑥2 = 0.4.
What just happened

![Page 71](../course.material/figs/T2-5%20Discrete/page_071.png)

---

## Page 72

Depth-first vs Breadth-first
●
Depth-first strategy continues as far down as possible (e.g., 
by always branching left) until it cannot go further, and then it 
follows right branches.
●
Breadth-first strategy explores all nodes on a given level 
before increasing depth.

![Page 72](../course.material/figs/T2-5%20Discrete/page_072.png)

---

## Page 73

Depth-first vs Breadth-first
●
Depth-first is a common strategy because, in the absence of 
more information about a problem, it is most likely to be the 
fastest way to find a solution - reaching the bottom of the tree 
generally forces a solution. 
●
Finding a solution quickly is desirable because this solution 
can then be used as a lower bound on other branches - so 
they can be pruned.
●
The depth-first strategy requires less memory storage 
because breadth-first must maintain a longer history as the 
number of branches increases. In contrast, depth-first only 
requires node storage equal to the number of branch levels.

![Page 73](../course.material/figs/T2-5%20Discrete/page_073.png)

---

## Page 74

Mixed-Integer Programming
●
We can use the same B&B procedure with integer variables.
●
Instead of branching with two equality constraints 
(𝑥𝑖 = 0 and 𝑥𝑖 = 1), we branch with two inequality 
constraints.
●
Example, if the variable we branched on is 𝑥1 = 3.4, we 
would branch with two new problems with the following 
constraints: 𝑥1 ≤ 3   and   𝑥1 ≥ 4.

![Page 74](../course.material/figs/T2-5%20Discrete/page_074.png)

---

## Page 75

Example 2
●
Solve the relaxed problem, replacing the integer constraints 
with a continuous constraint: 𝑥𝑖 ≥ 0

![Page 75](../course.material/figs/T2-5%20Discrete/page_075.png)

---

## Page 76

=
[0, 1.1818,4.4091,0],
f*
=
-15.59
Example 2
t*

![Page 76](../course.material/figs/T2-5%20Discrete/page_076.png)

---

## Page 77

Example 2

![Page 77](../course.material/figs/T2-5%20Discrete/page_077.png)

---

## Page 78

=
[0, 1.1818,4.4091,0],
f*
=
-15.59
Example 2
X3
X3
X
=
[0, 1.4,4,0.3]
f*
=
-15.25
infeasible
t*
<4
2 5

![Page 78](../course.material/figs/T2-5%20Discrete/page_078.png)

---

## Page 79

=
[0, 1.1818,4.4091,0],
f*
=
-15.59
Example 2
X3 < 4
X3
X
=
[0, 1.4,4,0.3]
f*
=
-15.25
infeasible
X2 < 1
X2 2 2
t*
2 5

![Page 79](../course.material/figs/T2-5%20Discrete/page_079.png)

---

## Page 80

=
[0, 1.1818,4.4091,0],
f*
=
-15.59
Example 2
X3 < 4
X3
X
=
[0, 1.4,4,0.3]
f*
=
-15.25
infeasible
X2 < 1
X2 2 2
X1 < 0
X1 2 1
X3
X3 > 3
X"
=
[0,2,3,0.5]
infeasible
bounded
f*
=
-13.75
f*
=
-13.75.
X2 < 0
X2 2 1
bounded
X1 < 1
X1 2 2
infeasible
bounded
t*
2 5
<2

![Page 80](../course.material/figs/T2-5%20Discrete/page_080.png)

---

## Page 81

Greedy Algorithms

![Page 81](../course.material/figs/T2-5%20Discrete/page_081.png)

---

## Page 82

Greedy Algorithms
●
Reduce the problem to a subset of smaller problems (often 
down to a single choice) and then make a locally optimal 
decision.
●
That decision is locked in, and then the next small decision is 
made in the same way.
●
A greedy algorithm does not revisit past decisions and thus 
ignores much of the coupling between design variables.

![Page 82](../course.material/figs/T2-5%20Discrete/page_082.png)

---

## Page 83

Greedy Algorithms Example
●
Which path to take to achieve the lowest possible total cost?

![Page 83](../course.material/figs/T2-5%20Discrete/page_083.png)

---

## Page 84

Greedy Algorithms More Examples
●
Traveling salesperson problem - always select the nearest 
city as the next step.
●
Optimising a propeller design (number of blades, type of 
material, number of shear webs etc.) - optimise the variables 
one at a time, with the others fixed, i.e., optimise the number 
of blades first, fix that number, then optimise material, and so 
on.
●
Grocery store shopping problem - always pick the cheapest 
food item next, or always pick the most nutritious food item 
next, or always pick the food item with the most nutrition per 
unit cost.

![Page 84](../course.material/figs/T2-5%20Discrete/page_084.png)

---

## Page 85

Greedy Algorithms
●
Advantages:
■
Algorithms are easy to construct
■
Scalable 
■
Can sometimes quickly find solutions reasonably close to 
an optimal solution.
■
Bound the computational expense of the problem.
●
Disadvantages:
■
It usually does not find an optimal solution (and in some 
cases finds the worst solution! (Gutin et al., 2002)).
■
The solution may also not be feasible.
Gutin et al., “Traveling salesman should not be greedy: 
domination analysis of greedy-type heuristics for the TSP”, 2002.

![Page 85](../course.material/figs/T2-5%20Discrete/page_085.png)

---

## Page 86

Exercises
●
Think of an assignment problem that might be useful for 
you in real life. Solve it using the Hungarian Algorithm.
●
Think of an optimisation problem and apply the greedy 
algorithm to it. How would it proceed?
●
Look up the terms that are new to you in this lecture and 
understand them.
Thanks!

![Page 86](../course.material/figs/T2-5%20Discrete/page_086.png)

---

