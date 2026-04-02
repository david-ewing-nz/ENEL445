# ENEL445_optimisation_2024_test (2)

*Converted from PDF: ENEL445_optimisation_2024_test (2).pdf*

---

## Page 1

Q1
Q2
Q3
Q4
Q5
Tot
University of Canterbury
Term Test 2024
Prescription Number(s): ENEL445
Paper Title:
Applied Engineering Optimisation
Time allowed: 1 hour 30 minutes
Number of pages: 19
Calculators ARE permitted.
ALL Questions ARE COMPULSORY.
(There are 5 questions in total.
The maximum total score is 100 marks.)
Family name (in block letters): ..........................................................................
Given name: .......................................................................................................
Student number: .................................................................................................

![Page 1](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_001.png)

---

## Page 2

2
ENEL445
INSTRUCTIONS
This is an closed-book test (apart from the A4 cheat sheet). Please write you answers in the
space provided. There is extra space at the end of the test should you need it. Show your
working as you complete the test, so that you can more easily receive partial credit. Make a
note indicating when your work is continued on an extra page.

![Page 2](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_002.png)

---

## Page 3

3
ENEL445
Q1.
Basics
(a)
[6 marks]
Let b and x be column vectors of size n × 1. Show that the vector derivative of
f(x) = bTx with respect to x is b.
(b)
[2 marks]
Write down the Frobenious norm of a matrix A in terms of A, AT, and the trace
operator.
TURN OVER

![Page 3](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_003.png)

---

## Page 4

4
ENEL445
(c)
[4 marks]
Write down the Taylor series expansion around the point c for a multivariate func-
tion, f(x), up to and including the second order term.
(d)
[8 marks]
Write down the definition of the Hessian and discuss the role of the Hessian in the
context of optimisation, include the term “positive semi-definite” in your answer.
Feel free to draw pictures!

![Page 4](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_004.png)

---

## Page 5

5
ENEL445
Q2.
Unconstrained Optimization (1)
(a)
[2 marks]
Put x = c + µp into your answer to Q1 (c), and keep the first-order term only to
derive the first-order Taylor-Series approximation of f(x) along the direction p.
(b)
[4 marks]
Assume that the direction vector p has unit length (i.e., ||p||2 = 1).
Use your answer to Q2 (a) to show that at the point c, the negated gradient −▽f(c)
gives the direction of the fastest function decrease.
(c)
[4 marks]
Explain why we must have ▽f(c)Tp = 0 for any direction p, if c is a local mini-
mum of f(x).
TURN OVER

![Page 5](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_005.png)

---

## Page 6

6
ENEL445
(d)
[5 marks]
Calculate, using the Chain Rule, the partial derivative of f(c−µ▽f(c)) with respect
to the step size µ. That is, find ∂f(c−µ▽f(c))
∂µ
.
(e)
[5 marks]
Suppose when µ = µ∗, we have ∂f(c−µ∗▽f(c))
∂µ
= 0.
Use your result in Q2 (d) to show that the gradient of f(x) at the point c−µ∗▽f(c)
is orthogonal to the gradient of f(x) at the point c.
That is, prove that ▽f(c −µ∗▽f(c))T▽f(c) = 0.

![Page 6](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_006.png)

---

## Page 7

7
ENEL445
Q3.
Unconstrained Optimization (2)
(a)
[8 marks]
In unconstrained optimization, the generic form for updating the design variable
x of the objective function f(x) is xk = xk−1 + αkpk. Here, xk is the solution
obtained in iteration k, αk is the step size and pk is the search direction.
Show that this generic update form can actually be derived by solving another un-
constrained optimization problem:
min
xk
h(xk) =
1
2αk
(xk −xk−1)T(xk −xk−1) −(xk −xk−1)Tpk.
Hint: First find the partial derivative of h(xk) with respect to xk. Then, setting the
result to zero would yield the desired answer.
(b)
[4 marks]
What insights can you obtain from examining h(xk)? Explain your answer.
TURN OVER

![Page 7](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_007.png)

---

## Page 8

8
ENEL445
(c)
[8 marks]
We are trying to solve a weighted nonlinear least squares (NLS) problem, whose
objective function is
f(x) = 1
2(b −g(x))TW(b −g(x)).
Here, W is a positive definite weighting matrix. b is the measurement vector and
g(x) is a nonlinear vector function of x.
We are going to update the solution iteratively. At iteration k, we first approximate
g(x) using g(x) ≈g(xk−1) + Jk−1(x −xk−1), where Jk−1 is the Jacobian matrix.
Derive the desired update rule by putting the above approximation into f(x) and
finding xk that minimizes the approximated objective function.

![Page 8](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_008.png)

---

## Page 9

9
ENEL445
Q4.
Constrained optimisation & algorithms
(a)
[16 marks]
Consider the problem:
min
x1,x2 x2
1 −x2
subject to x2 ≤−1
x1 −x2 ≤0
i) State the Lagrangian function, including slack variables [2 marks].
ii) Derive the KKT conditions associated with this problem and find the optimal so-
lution [8 marks].
TURN OVER

![Page 9](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_009.png)

---

## Page 10

10
ENEL445

![Page 10](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_010.png)

---

## Page 11

11
ENEL445
iii) State the Lagrangian dual problem, identifying the dual function (note: you are
NOT required to work out the dual function - although you would not be penalised
for doing so) [2 marks].
iv) Explain what duality gap is. What is the duality gap in this case? Prove your
answer mathematically or otherwise [4 marks].
TURN OVER

![Page 11](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_011.png)

---

## Page 12

12
ENEL445

![Page 12](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_012.png)

---

## Page 13

13
ENEL445
(b)
[4 marks]
In a few sentences, explain the concept of interior penalty.
TURN OVER

![Page 13](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_013.png)

---

## Page 14

14
ENEL445
Q5.
Optimisation-based Control
(a)
[10 marks]
Consider the system:
xk+1 = f(xk, uk)
with
f(xk, uk) =
u = 1
u = 2
u = 3
x = 1
1
2
3
x = 2
1
3
1
x = 3
2
1
2
and cost function:
c(xk, uk) =
u = 1
u = 2
u = 3
x = 1
1
3
4
x = 2
1
2
3
x = 3
0
1
2
and terminal cost Jh(xh) = 3 −xh. Find the optimal solution for two steps (i.e. the
optimal uh−1 and uh−2) for any initial value of xh−2 ∈{1, 2, 3} recursively using
dynamic programming. (Hint: a graphical illustration might be helpful).

![Page 14](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_014.png)

---

## Page 15

15
ENEL445
TURN OVER

![Page 15](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_015.png)

---

## Page 16

16
ENEL445
(b)
[10 marks]
What is Q Learning? Illustrate your answer with pseudo-code describing a Q -
Learning algorithm using ϵ-greedy exploration. Explain the main parameters, what
they are, and how they work and/or why they are needed.
(Hint: the parameters should include ϵ, a learning rate, and the discount factor.)

![Page 16](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_016.png)

---

## Page 17

17
ENEL445
TURN OVER

![Page 17](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_017.png)

---

## Page 18

18
ENEL445
Extra Answer Space (Optional)

![Page 18](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_018.png)

---

## Page 19

19
ENEL445
Extra Answer Space (Optional)
END OF PAPER

![Page 19](../course.material/figs/ENEL445_optimisation_2024_test%20%282%29/page_019.png)

---

