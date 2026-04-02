# ENEL445_optimisation_2025_test

*Converted from PDF: ENEL445_optimisation_2025_test.pdf*

---

## Page 1

Q1
Q2
Q3
Q4
Q5
Tot
University of Canterbury
Term Test 2025
Prescription Number(s): ENEL445
Paper Title:
Applied Engineering Optimisation
Time allowed: 1 hour 30 minutes
Number of pages: 20
Calculators ARE permitted.
ALL Questions ARE COMPULSORY.
(There are 5 questions in total.
The maximum total score is 100 marks.)
Family name (in block letters): ..........................................................................
Given name: .......................................................................................................
Student number: .................................................................................................

![Page 1](../course.material/figs/ENEL445_optimisation_2025_test/page_001.png)

---

## Page 2

2
ENEL445
INSTRUCTIONS
This is an closed-book test (apart from the A4 cheat sheet). Please write you answers in the
space provided. There is extra space at the end of the test should you need it. Show your
working as you complete the test, so that you can more easily receive partial credit. Make a
note indicating when your work is continued on an extra page.

![Page 2](../course.material/figs/ENEL445_optimisation_2025_test/page_002.png)

---

## Page 3

3
ENEL445
Q1.
Basics
(a)
[6 marks]
Let x be a column vector of size n × 1 and A be a matrix of size n × n.
Show that the vector derivative of f(x) = xTAx with respect to x is Ax + ATx.
TURN OVER

![Page 3](../course.material/figs/ENEL445_optimisation_2025_test/page_003.png)

---

## Page 4

4
ENEL445
(b)
[5 marks]
Show that the infinity norm of an n × 1 vector x is the maximum absolute value of
the entries in x.
(c)
[4 marks]
Write down the Taylor series expansion around the point c for a multivariate func-
tion, f(x), up to and including the second-order term.

![Page 4](../course.material/figs/ENEL445_optimisation_2025_test/page_004.png)

---

## Page 5

5
ENEL445
(d)
[5 marks]
Write down the definition of positive semi-definiteness and discuss the role of pos-
itive semi-definite matrices in the context of optimisation.
Include the term “Hessian” in your answer. Feel free to draw pictures!
TURN OVER

![Page 5](../course.material/figs/ENEL445_optimisation_2025_test/page_005.png)

---

## Page 6

6
ENEL445
Q2.
Unconstrained Optimization (1)
(a)
[3 marks]
Directional gradient: Substitute x = c + µp into your answer to Q1 (c), where µ
is the step size, and keep up to the first-order term to derive the directional gradient
of f(x) along the direction p.
(b)
[5 marks]
First-order necessary optimality condition: Show that if c is a local minimum of
f(x), we must have ▽f(c)Tp = 0.
Hint: use the fact that the direction vector p can be arbitrary.

![Page 6](../course.material/figs/ENEL445_optimisation_2025_test/page_006.png)

---

## Page 7

7
ENEL445
(c)
(i)
[2 marks]
Suppose the objective function is quadratic with respect to the design vari-
able. That is, f(x) = 1
2xTAx + bTx, where A is positive definite. Compute
its gradient at x = c (i.e., find ▽f(c)).
Hint: you may want to apply some of your answers to Q1 (a).
(ii)
[4 marks]
Line search: We would like to perform an exact line search at c along the
direction p. Formulate this exact line search problem as an unconstrained
optimization problem with the design variable being the step size µ.
(iii)
[6 marks]
Optimal step size: Solve the unconstrained optimization problem formulated
in the previous question for the optimal step size µ∗.
TURN OVER

![Page 7](../course.material/figs/ENEL445_optimisation_2025_test/page_007.png)

---

## Page 8

8
ENEL445
Q3.
Unconstrained Optimization (2)
Nonlinear least squares: Consider a range-based location system. We use three sensors
at s1 = [sx,1, sy,1]T, s2 = [sx,2, sy,2]T and s3 = [sx,3, sy,3]T to locate an object at unknown
location u = [ux, uy]T.
(a)
[5 marks]
Let ri(u) = ||u −si||2 be the true distance between sensor i and the object u,
where i = 1, 2, 3, and || · ||2 is the Euclidean norm (2-norm).
Derive the gradient of ri(u).
(b)
[5 marks]
Jacobian matrix: Derive the Jacobian J(u) of r(u) = [r1(u), r2(u), r3(u)]T.
Hint: use your result in Q3 (a).

![Page 8](../course.material/figs/ENEL445_optimisation_2025_test/page_008.png)

---

## Page 9

9
ENEL445
(c)
[10 marks]
Let di be the measured distance between sensor i and the object u, where i =
1, 2, 3.
Formulate a nonlinear least squares problem with the design variable being u. This
is the problem to be solved for range-based location.
Hint: you can use the definitions d = [d1, d2, d3]T and r(u) = [r1(u), r2(u), r3(u)]T
to simplify your expression.
TURN OVER

![Page 9](../course.material/figs/ENEL445_optimisation_2025_test/page_009.png)

---

## Page 10

10
ENEL445
Q4.
Constrained optimisation & algorithms
(a)
[16 marks]
Consider the problem:
min
x1,x2 (x1 −x2)2
subject to x1 + 2x2 = 0
i) State the Lagrangian function [2 marks].
ii) Derive the KKT conditions associated with this problem and find the optimal so-
lution. [6 marks].

![Page 10](../course.material/figs/ENEL445_optimisation_2025_test/page_010.png)

---

## Page 11

11
ENEL445
TURN OVER

![Page 11](../course.material/figs/ENEL445_optimisation_2025_test/page_011.png)

---

## Page 12

12
ENEL445
iii) State the Lagrangian dual problem, identifying the dual function (note: you are
NOT required to work out the dual function - although you would not be penalised
for doing so) [2 marks].
iv) Explain what duality gap is. What is the duality gap in this case? Explain your
answer mathematically or otherwise [2 marks].

![Page 12](../course.material/figs/ENEL445_optimisation_2025_test/page_012.png)

---

## Page 13

13
ENEL445
(b)
[3 marks]
In a few sentences, explain the concept of slackness and slack variables.
(c)
[3 marks]
What is the "combinatorial problem" when trying to solve the KKT conditions of an
optimisation problem? How does the Sequential Quadratic Programming algorithm
(SQP) cope with this issue?
TURN OVER

![Page 13](../course.material/figs/ENEL445_optimisation_2025_test/page_013.png)

---

## Page 14

14
ENEL445

![Page 14](../course.material/figs/ENEL445_optimisation_2025_test/page_014.png)

---

## Page 15

15
ENEL445
Q5.
Optimisation-based Control
(a)
[8 marks]
Consider the system:
xk+1 = uk
with cost function:
c(xk, uk) =
u = 1
u = 2
u = 3
x = 1
2
3
4
x = 2
1
2
3
x = 3
2
1
1
and terminal cost Jh(xh) = 1. Find the optimal solution for two steps (i.e. the
optimal uh−1 and uh−2) for any initial value of xh−2 ∈{1, 2, 3} recursively using
dynamic programming. (Hint: a graphical illustration might be helpful).
TURN OVER

![Page 15](../course.material/figs/ENEL445_optimisation_2025_test/page_015.png)

---

## Page 16

16
ENEL445

![Page 16](../course.material/figs/ENEL445_optimisation_2025_test/page_016.png)

---

## Page 17

17
ENEL445
(b)
[8 marks]
Consider the discrete-time system:
xk+1 = 0.9xk + 0.1uk
yk = xk
If x0 = 0 and |u| <= 1, and the desired (reference) trajectory for y is r =
[r1, r2, r3, r4, r5]T = [0.2, 0.4, 0.6, 0.8, 1]T, and the cost function is ||y−r||2
2+||u||2
2,
i) Formulate (but do not solve) the model-predictive control problem [5 marks].
ii) What is the horizon length implied by the given reference trajectory [1 mark]?
iii) Is this (or can the problem be made) a quadratic optimisation problem [2 marks]?
Hint: you do not need to include terminal constraints / costs in your formulation
(although you would not be penalised for doing so). However, you do need to make
sure all the given information is represented in the problem.
TURN OVER

![Page 17](../course.material/figs/ENEL445_optimisation_2025_test/page_017.png)

---

## Page 18

18
ENEL445
(c)
[2 marks]
Explain briefly, ideally in two sentences or less, the trade-off when choosing ϵ in
ϵ-greedy exploration, as often used with Q Learning.

![Page 18](../course.material/figs/ENEL445_optimisation_2025_test/page_018.png)

---

## Page 19

19
ENEL445
Extra Answer Space (Optional)

![Page 19](../course.material/figs/ENEL445_optimisation_2025_test/page_019.png)

---

## Page 20

20
ENEL445
Extra Answer Space (Optional)
END OF PAPER

![Page 20](../course.material/figs/ENEL445_optimisation_2025_test/page_020.png)

---

