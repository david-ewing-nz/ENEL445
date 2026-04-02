# Applied Engineering Optimisation - Mathematics and background-1

*Converted from PDF: Applied Engineering Optimisation - Mathematics and background-1.pdf*

---

## Page 1

Classification: In-Confidence
Nau mai, welcome to
Applied Engineering 
Optimisation
ENEL445

![Page 1](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_001.png)

---

## Page 2

Classification: In-Confidence
Week 1 Lecture 2
• How to formulate optimisation problems
• Design variables
• Objective (cost) function
• Constraints
• Optimisation problem classification
• Mathematical background

![Page 2](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_002.png)

---

## Page 3

Classification: In-Confidence
Design (decision) variables
• These are the variables that we can change to 
achieve our desired result:
• We usually denote them as follows:
• When setting up an optimization problem, a good
starting point is to think “what variables do I have 
control over”?

![Page 3](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_003.png)

---

## Page 4

Classification: In-Confidence
Design variables
• Design variables can be continuous or discrete, or a 
mixture. 
• Design variables should be independent, otherwise 
there may be an infinite number of equivalent 
solutions. 
• Don’t forget to add physically meaningful bounds. 
• Tip: when starting to solve a problem, try to use as few 
design variables as possible.

![Page 4](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_004.png)

---

## Page 5

Classification: In-Confidence
Objective function
• These is the objective by which we measure the 
quality of a solution.
• In this course, we will usually have a closed-form
function f(x) which serves as the objective to be 
minimised or maximised.
• However, in many applications, the objective
function could be the output of a simulation or 
physical system/experiment.

![Page 5](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_005.png)

---

## Page 6

Classification: In-Confidence
Objective function
• We will look at minimisation problems in this course. If 
you have a maximization problem, you can always 
simply reverse the sign of the objective function!
• The choice of objective function is crucial for successful 
design optimization. If this is done poorly, the 
mathematical optimum will be non-optimal from the 
engineering point of view. 
• A bad choice for the objective function is a common 
mistake in design optimization.

![Page 6](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_006.png)

---

## Page 7

Classification: In-Confidence
Choosing an objective function
• Example: designing a car for Toyota
• What should your objective function be?.
a.
The weight of the car in kg (lower is better).
b. The manufacturing cost of the car in $.
c.
The performance (speed, acceleration, handling, 
torque, etc.) of the car.
d. The capacity (people and baggage) of the car.
e.
Some weighted combination of some of the above.

![Page 7](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_007.png)

---

## Page 8

Classification: In-Confidence
Choosing an objective function
• Example: going shopping at the supermarket
• What should your objective function be?
a.
The total cost of your groceries. 
b. Meeting your nutritional requirements as closely as 
possible. 
c.
Required preparation time (minimise). 
d. How much you like the food (maximise)
e.
Some weighted combination of some of the above.

![Page 8](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_008.png)

---

## Page 9

Classification: In-Confidence
Objective functions
• As we can see, many real-life problems are 
complicated, and the objective function is a 
weighted combination of various considerations.
• Alternatively, multi-objective optimisation can be
performed directly.

![Page 9](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_009.png)

---

## Page 10

Classification: In-Confidence
Constraints
• Many optimisation problems involve constraints:
• E.g. when designing a car you are limited by the 
available parts, by road rules governing size, by safety 
requirements etc.
• When grocery shopping you are limited by stock 
availability, budget limits, item limits, etc.
• There are two types of constraints:
• Inequality constraints
• Equality constraints (equivalent to two inequality 
constraints)

![Page 10](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_010.png)

---

## Page 11

Classification: In-Confidence
Constraints
• Inequality constraints can be active or inactive at 
the optimum point. An active inequality constraint 
means that 𝑔(𝑥∗) = 0, whereas for an inactive one, 
𝑔(𝑥∗) < 0.

![Page 11](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_011.png)

---

## Page 12

Classification: In-Confidence
Constraints
• The region in which all constraints are satisfied is 
called the feasible region. 
• If there are too many constraints, there may be no 
feasible region and this makes the problem also 
infeasible.
• Example: if there are more independent equality 
constraints than design variables, the problem is 
infeasible.

![Page 12](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_012.png)

---

## Page 13

Classification: In-Confidence
Constraints vs Objective function 
terms
• Example: going shopping at the supermarket
• Which ones could be constraints?
a. The total cost of your groceries (e.g. total cost 
less than $100)
b. Meeting your nutritional requirements (e.g.
calories >= X, fat <= Y, etc.)
c. Required preparation time (e.g. time/day <= 1 hr)
d. How much you like the food (e.g. all foods below 
a threshold of liability are out)

![Page 13](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_013.png)

---

## Page 14

Classification: In-Confidence
Putting it all together (+notation)

![Page 14](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_014.png)

---

## Page 15

Classification: In-Confidence
Optimization classification

![Page 15](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_015.png)

---

## Page 16

Classification: In-Confidence
Mathematical concepts
• Smooth / continuous functions
• Linearity
• Multimodal vs unimodal

![Page 16](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_016.png)

---

## Page 17

Classification: In-Confidence
Optimisation algorithms
• No optimization 
algorithm is good 
for every 
problem!
• Gradient vs 
gradient-free 
optimisation

![Page 17](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_017.png)

---

## Page 18

Classification: In-Confidence
Which optimiser should I use?

![Page 18](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_018.png)

---

## Page 19

Classification: In-Confidence
Notation
• Vectors
• Matrices and elements of matrices
• Optimum point 𝑥∗

![Page 19](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_019.png)

---

## Page 20

Classification: In-Confidence
Vector and matrix norms

![Page 20](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_020.png)

---

## Page 21

Classification: In-Confidence
Vector and matrix math concepts
trace
symmetric matrices
positive (negative) (semi-)definiteness
gradient
Hessian
Vector derivatives
Taylor-series expansion

![Page 21](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Mathematics%20and%20background-1/page_021.png)

---

