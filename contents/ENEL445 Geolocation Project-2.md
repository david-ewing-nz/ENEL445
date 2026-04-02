# ENEL445 Geolocation Project-2

*Converted from PDF: ENEL445 Geolocation Project-2.pdf*

---

## Page 1

Source Geolocation using 
Frequency Measurements
ENEL445 - 26S1 Project

![Page 1](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_001.png)

---

## Page 2

Problem Description (1)
• Source geolocation refers to estimating the 
geodesic location of a signal emitter on the Earth 
surface from signal measurements 
• A large variety of civil and military applications
• Navigation, search and rescue, survillance, jammer 
localization ...  
• Source geolocation using frequency measurements
• Time measurements such as ranging are inaccurate for 
narrow-band sources
Figure from https://www.pocketgpsworld.com/howgpsworks.php

![Page 2](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_002.png)

---

## Page 3

Problem Description (2)
• Source geolocation using frequency difference of arrival 
(FDOA) measurements from four satellites
• The satellites are moving, causing relative motion 
between the satellites and the ground source
• The source signal received at each satellite is then subject 
to Doppler shift, which depends on the source location
• The source signal frequency is unknown, necessitating 
using FDOA rather than frequency measurements for 
geolocation
Figure from https://www.pocketgpsworld.com/howgpsworks.php

![Page 3](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_003.png)

---

## Page 4

Mathematical Preliminary
• Source position in Earth Centered Earth Fixed coordinate system:
• Source geodetic position (latitude, longitude, altitude):
• Coordinate conversion:

![Page 4](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_004.png)

---

## Page 5

Doppler and FDOA
• Satellite ECEF positions and velocities:
• Received frequency at satellite   :
• FDOA measurements (j = 2,3,4):

![Page 5](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_005.png)

---

## Page 6

Vector Form Representation
=                                                                              + 
True FDOAs
Noise
Measured FDOAs

![Page 6](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_006.png)

---

## Page 7

Phase-1 of the Project (1)
• Assume the noise in the frequency measurements      is Gaussian with 
zero mean and variance 𝜎𝑓
2
• The FDOA measurements are subject to zero-mean Gaussian noise too
• Derive the covariance of the FDOA noise vector

![Page 7](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_007.png)

---

## Page 8

Phase-1 of the Project (2)
Formulate the source geolocation problem as a maximum-likelihood 
estimation problem (see reference [1]) and transforms it into a non-
linear least-square (NLS) problem
• Grid search-based solution
• Perform a grid search over [0, 40o]×[0, 40o], output the one with the osmallest 
cost function value

![Page 8](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_008.png)

---

## Page 9

Phase-1 of the Project (3)
• Monte Carlo simulation-based performance evaluation
• For each setup, perform L = 10,000 ensemble run
• In each run, generate new random Gaussian noise and add to the true FDOA
• Perform the grid search-based method to find the geolocation result
• Compute the estimation root mean square error (RMSE) using
• Conside four scenarios, each with different frequency noise levels
• Plot the results

![Page 9](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_009.png)

---

## Page 10

Phase-2 of the Project (1)
• Solve the non-linear least square problem formulated in Phase-1 using a 
gradient-based approach
• Q1: With FDOA, the knowledge on the signal wavelength is still required：
• Find a way to estimate it and justify your method through an accuracy 
analysis

![Page 10](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_010.png)

---

## Page 11

Phase-2 of the Project (2)
• Bonus Question (5%): we use three FDOAs in this project
• Can the use of e.g., f23, f43 etc together with                              
improve performance?
• Q2:Derive analytically the Jacobian of the FDOA measurement 
function using the chain rule

![Page 11](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_011.png)

---

## Page 12

Phase-2 of the Project (3)
• Q3: Verify your analytical results using the finite difference method 
for computing the gradient/derivatives numerically
• Bonus Question (10%): verify your gradient results using the complex 
step method
• Q4: Develop (design + implement + test) a gradient-based approach 
for source geolocation 
• Conjugate gradient, Newton’s method, Gauss Newton method, Levenberg-
Marquardt, BFGS ... 
• With line search, stopping criteria, multi-start strategy
• Make sure your iterations always stay in the area of interest [0, 40o]×[0, 40o]

![Page 12](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_012.png)

---

## Page 13

Phase-2 of the Project (4)
• Q5: Compare the RMSE performance of your gradient-based 
approach with the grid search-based solution in Phase-1 using Monte 
Carlo simulation
• Bonus question (15%): implement a gradient-free technique such as 
the particle swarm optimization (PSO) algorithm for source 
geolocation and compare its performance with the gradient-based 
method and grid search-based solution.

![Page 13](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_013.png)

---

## Page 14

References
[1]. Source geolocation project description
[2]. Y. Pei et al. “A closed-form solution for source localization using 
FDOA measurements only,” IEEE Communications Letters, 2022.

![Page 14](../course.material/figs/ENEL445%20Geolocation%20Project-2/page_014.png)

---

