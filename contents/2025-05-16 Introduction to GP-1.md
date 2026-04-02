# 2025-05-16 Introduction to GP-1

*Converted from PDF: 2025-05-16 Introduction to GP-1.pdf*

---

## Page 1

An Introduction to Gaussian 
Processes (GP)
Le Yang, Joe Chen and Jeremy Waston
Department of ECE, University of Canterbury

![Page 1](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_001.png)

---

## Page 2

Outline
• Supervised learning and regression
• Fundamentals of Gaussian Processes (GP) 
• Mean function, covariance function and hyperparameters in GP
• GP for nonlinear regression
• GP in spatiotemporal modeling
• References

![Page 2](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_002.png)

---

## Page 3

Supervised Learning
• Supervised learning
• Establish (generally non-linear) curve(s) to 
• Build decision boundaries (classification)
• Fit through labeled data (regression) 
Classification Problem
Regression Problem

![Page 3](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_003.png)

---

## Page 4

Supervised Regression
• Formulation of a regression problem
• Given a set of 𝑁 input-output pairs (labeled training data) {𝒙𝑛, 𝑦𝑛}𝑛=1
𝑁
• 𝒙𝑛: input
• 𝑦𝑛: output
• Find a nonlinear (multivariate) function 𝑦= 𝑓(𝒙) that can 
• Describe the training data well (no underfitting)
• Generalize to inputs other than 𝑥𝑛 well (no overfitting)
• Predictive/generative modeling

![Page 4](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_004.png)

---

## Page 5

Fundamentals of Gaussian Processes (1)
• Definition
• A Gaussian Processes (GP) is a collection of random variables with the joint 
distribution of any subset being Gaussian
• To specify a (multivariate) Gaussian distribution, we only need to provide
• Mean and covariance
• Similarly, to specify a GP, we need
• Mean function
• Covariance function

![Page 5](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_005.png)

---

## Page 6

Fundamentals of Gaussian Processes (2)
• Impose GP prior on the function 𝑦= 𝑓(𝒙) to be estimated
• Any subset of function values 𝑦𝑖= 𝑓(𝒙𝑖) is Gaussian
• 𝑝(𝑦1, 𝑦2, … , 𝑦𝑀) is Gaussian
• 𝑀= 1,2,3, … is an arbitrary positive integer
• What are the mean and covariance for 𝑝(𝑦1, 𝑦2, … , 𝑦𝑀)?
• Note that the inputs for 𝑦𝑖 are different
• Cannot use fixed mean and covariance
• Mean and covariance should depend on the input 𝒙1, 𝒙2, … , 𝒙𝑀

![Page 6](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_006.png)

---

## Page 7

Fundamentals of Gaussian Processes (3)
• Mean function 𝑚(𝒙)
• Specify the mean vector for 𝑝(𝑦1, 𝑦2, … , 𝑦𝑀)
• 𝝁𝑀×1 =
𝑚(𝒙1)
⋮
𝑚(𝒙𝑀)
• Covariance function 𝑘𝒙, 𝒙′
• Specify the covariance matrix for 𝑝(𝑦1, 𝑦2, … , 𝑦𝑀)
• 𝜮𝑀×𝑀=
𝑘(𝒙1, 𝒙1)
⋯
𝑘(𝒙1, 𝒙𝑀)
⋮
⋱
⋮
𝑘(𝒙𝑀, 𝒙1)
⋯
𝑘(𝒙𝑀, 𝒙𝑀)

![Page 7](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_007.png)

---

## Page 8

Mean Function and Covariance Function in GP (1)
• Mean function 𝑚(𝒙) captures the trend in the function 𝑓(𝒙)
•  𝑚𝒙= 0 is commonly used and in many cases, a good choice
• 𝑚𝒙= σ𝑗=1
𝐽
𝑎𝑗𝜑𝑗(𝒙), 𝜑𝑗(𝒙) is a linear/nonlinear function of 𝒙 (surrogate ☺)
• Covariance function 𝑘𝒙, 𝒙′  
• Specifies the variance of the function value when 𝒙= 𝒙′
• Specifies the correlation between function values 𝑓(𝒙) and 𝑓(𝒙′)
• 𝑓𝒙~𝒢𝒫𝑚𝒙, 𝑘𝒙, 𝒙′
: 𝑓(𝒙) has a GP prior with mean function 
𝑚𝒙 and covariance function 𝑘𝒙, 𝒙′

![Page 8](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_008.png)

---

## Page 9

Mean Function and Covariance Function in GP (2)
• Squared exponential (SE): a commonly used covariance function 
• 𝑘𝒙, 𝒙′ = 𝜎𝑓
2exp −
||𝒙−𝒙′||2
2𝑙2
• 𝑘𝒙, 𝒙= 𝜎𝑓
2
• 𝜎𝑓
2: a priori variance of function values 𝑓(𝒙)
• 𝑙   : characteristic length
• Smoothness of the function 𝑓(𝑥) to be modeled
• What if the training data has noise in 𝑦𝑛?
• 𝑘𝒙, 𝒙′ = 𝜎𝑓
2 exp −
𝒙−𝒙′
2
2𝑙2
+ 𝜎𝑣2𝛿(𝒙−𝒙′)  
• 𝜎𝑣2    : noise variance
• 𝛿(∙) :  Dirac delta function

![Page 9](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_009.png)

---

## Page 10

Mean Function and Covariance Function in GP (3)
• Sampling from 𝑧~𝑁𝜇, Σ  v.s. sampling from 𝑓𝑥~𝒢𝒫𝑚𝑥, 𝑘𝑥, 𝑥′
𝜇= 0
0 , Σ =
1
0.9
0.9
1                                𝑚𝑥= 0, 𝑘𝑥, 𝑥′ =exp −𝑥−𝑥′
2 + 𝛿(𝑥−𝑥′)

![Page 10](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_010.png)

---

## Page 11

Hyperparameters in GP (1)
• Hyperparameters in GP
• Unknown parameters in the mean function 𝑚𝒙 and covariance function 𝑘𝒙, 𝒙′
• Example
• 𝑚𝒙= σ𝑗=1
𝐽
𝑎𝑗𝜑𝑗(𝒙)
• 𝑘𝒙, 𝒙′ = 𝜎𝑓
2 exp −
𝒙−𝒙′
2
2𝑙2
+ 𝜎𝑣2𝛿(𝒙−𝒙′)  
• 𝐽+ 3 hyperparameters: {𝑎1, 𝑎2, … , 𝑎𝐽, 𝑙, 𝜎𝑓
2, 𝜎𝑣2}

![Page 11](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_011.png)

---

## Page 12

Hyperparameters in GP (2)
• Sampling from 𝑓𝑥~𝒢𝒫𝑚𝑥, 𝑘𝑥, 𝑥′
• 𝑚𝑥= 0
• 𝑘𝑥, 𝑥′ = 𝜎𝑓
2 exp −
𝑥−𝑥′
2
2𝑙2
+ 𝜎𝑣2𝛿(𝑥−𝑥′)
•  𝑙= 1
• 𝜎𝑣= 0 : no measurement noise
• (a) 𝜎𝑓= 1
• (b) 𝜎𝑓= 2
• (c) 𝜎𝑓= 3
• (d) 𝜎𝑓= 0.5
• 𝜎𝑓 specifies the ‘signal’ energy

![Page 12](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_012.png)

---

## Page 13

Hyperparameters in GP (3)
• Sampling from 𝑓𝑥~𝒢𝒫𝑚𝑥, 𝑘𝑥, 𝑥′
• 𝑚𝑥= 0
• 𝑘𝑥, 𝑥′ = 𝜎𝑓
2 exp −
𝑥−𝑥′
2
2𝑙2
+ 𝜎𝑣2𝛿(𝑥−𝑥′)
• 𝜎𝑣= 0 : no measurement noise
• 𝜎𝑓= 1
• (a) 𝑙= 1
• (b) 𝑙= 3
• (c) 𝑙= 5
• (d) 𝑙= 0.5
• 𝑙 specifies the smoothness of the function

![Page 13](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_013.png)

---

## Page 14

Hyperparameters in GP (4)
• Sampling from 𝑓𝑥~𝒢𝒫𝑚𝑥, 𝑘𝑥, 𝑥′
• 𝑚𝑥= 0
• 𝑘𝑥, 𝑥′ = 𝜎𝑓
2 exp −
𝑥−𝑥′
2
2𝑙2
+ 𝜎𝑣2𝛿(𝑥−𝑥′)
•  𝑙= 1
• 𝜎𝑓=1 
• (a) 𝜎𝑣= 0
• (b) 𝜎𝑣= 0.01
• (c) 𝜎𝑣= 0.05
• (d) 𝜎𝑣= 0.1
• 𝜎𝑣 specifies the SNR

![Page 14](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_014.png)

---

## Page 15

Hyperparameters in GP (5)
• Maximum likelihood (ML) estimation of GP hyperparameters
• 𝑓𝒙~𝒢𝒫𝑚𝒙, 𝑘𝒙, 𝒙′
• The training data satisfy 
𝑝(𝑦1, 𝑦2, … , 𝑦𝑁) = 𝑁
𝑚(𝒙1)
⋮
𝑚(𝒙𝑁)
,
𝑘(𝒙1, 𝒙1)
⋯
𝑘(𝒙1, 𝒙𝑁)
⋮
⋱
⋮
𝑘(𝒙𝑁, 𝒙1)
⋯
𝑘(𝒙𝑁, 𝒙𝑁)
• Find the hyperparameters through solving via conjugate gradient
𝑚𝑎𝑥log(𝑝(𝑦1, 𝑦2, … , 𝑦𝑁))

![Page 15](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_015.png)

---

## Page 16

GP for Nonlinear Regression (1)
• Problem setup
• Given a set of 𝑁 training data points {𝒙𝑛, 𝑦𝑛}𝑛=1
𝑁
• The function to be modeled, 𝑓𝒙, has a GP prior 𝑓𝒙~𝒢𝒫𝑚𝒙, 𝑘𝒙, 𝒙′
• GP hyperparameters have been found through e.g., ML estimation
• Data-driven approach
• We are interested to find the posterior
𝑝(𝑦∗|𝒙∗, {𝒙𝑛, 𝑦𝑛}𝑛=1
𝑁
)
• 𝑦∗= 𝑓(𝒙∗): the function value at an input 𝒙∗
• ‘Predictive’ probability of 𝑦∗ 
• Modeling of mapping from 𝒙∗ to 𝑦∗

![Page 16](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_016.png)

---

## Page 17

GP for Nonlinear Regression (2)
• By Bayes theorem
𝑝(𝑦∗|𝒙∗, {𝒙𝑛, 𝑦𝑛}𝑛=1
𝑁
) = 𝑝( 𝒙∗, 𝑦∗, {𝒙𝑛, 𝑦𝑛}𝑛=1
𝑁
)
𝑝({𝒙𝑛, 𝑦𝑛}𝑛=1
𝑁
)
• Note that because 𝑓𝒙~𝒢𝒫𝑚𝒙, 𝑘𝒙, 𝒙′
, 
𝑝
𝒙𝑛, 𝑦𝑛𝑛=1
𝑁
= 𝑝(𝑦1, 𝑦2, … , 𝑦𝑁) = 𝑁
𝑚(𝒙1)
⋮
𝑚(𝒙𝑁)
,
𝑘(𝒙1, 𝒙1)
⋯
𝑘(𝒙1, 𝒙𝑁)
⋮
⋱
⋮
𝑘(𝒙𝑁, 𝒙1)
⋯
𝑘(𝒙𝑁, 𝒙𝑁)
𝑝
𝒙∗, 𝑦∗, 𝒙𝑛, 𝑦𝑛𝑛=1
𝑁
= 𝑝(𝑦∗, 𝑦1, 𝑦2, … , 𝑦𝑁) = 𝑁
𝑚(𝒙∗)
𝑚(𝒙1)
⋮
𝑚(𝒙𝑁)
,
𝑘(𝒙∗, 𝒙∗)
𝑘(𝒙∗, 𝒙1)
⋯
𝑘(𝒙∗, 𝒙1)
𝑘(𝒙1, 𝒙∗)
⋮
𝑘(𝒙𝑁, 𝒙∗)
𝑘(𝒙1, 𝒙1)
⋯
𝑘(𝒙1, 𝒙𝑁)
⋮
⋱
⋮
𝑘(𝒙𝑁, 𝒙1)
⋯
𝑘(𝒙𝑁, 𝒙𝑁)

![Page 17](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_017.png)

---

## Page 18

GP for Nonlinear Regression (3)
• 𝑝(𝑦∗|𝒙∗, {𝒙𝑛, 𝑦𝑛}𝑛=1
𝑁
) is Gaussian
• By Gaussian conditional, 
𝑝(𝑦∗|𝒙∗, {𝒙𝑛, 𝑦𝑛}𝑛=1
𝑁
) = 𝑁(𝜇∗, Σ∗) 
    where
𝜇∗= 𝑚𝒙∗+ [𝑘(𝒙∗, 𝒙1)
⋯
𝑘(𝒙∗, 𝒙𝑁)] ∙
𝑘(𝒙1, 𝒙1)
⋯
𝑘(𝒙1, 𝒙𝑁)
⋮
⋱
⋮
𝑘(𝒙𝑁, 𝒙1)
⋯
𝑘(𝒙𝑁, 𝒙𝑀)
−1
𝑦1
⋮
𝑦𝑁
−
𝑚(𝒙1)
⋮
𝑚(𝒙𝑁)
Σ∗= 𝑘𝒙∗, 𝒙∗−[𝑘(𝒙∗, 𝒙1)
⋯
𝑘(𝒙∗, 𝒙𝑁)] ∙
𝑘(𝒙1, 𝒙1)
⋯
𝑘(𝒙1, 𝒙𝑁)
⋮
⋱
⋮
𝑘(𝒙𝑁, 𝒙1)
⋯
𝑘(𝒙𝑁, 𝒙𝑀)
−1 𝑘(𝒙1, 𝒙∗)
⋮
𝑘(𝒙𝑁, 𝒙∗)
• 𝜇∗: predictive function value at 𝒙∗
• Σ∗: prediction uncertainty

![Page 18](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_018.png)

---

## Page 19

GP for Nonlinear Regression (3)
• Example
• 𝑚𝑥= 0
• 𝑘𝑥, 𝑥′ = 𝜎𝑓
2 exp −
𝑥−𝑥′
2
2𝑙2
+ 𝜎𝑣2𝛿(𝑥−𝑥′)
•  𝑙= 1
• 𝜎𝑣= 0 : no measurement noise
• 𝜎𝑓= 1
• ‘Accurate’ prediction around training data points
• ‘Large’ uncertainty when away from training data

![Page 19](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_019.png)

---

## Page 20

GP for Nonlinear Regression (4)
• GP-based nonlinear regression is non-parametric
• Complexity proportional to 𝑂(𝑁3), scalable methods needed for large-scale dataset
• GP-based nonlinear regression explicitly quantifies prediction uncertainty 
• GP-based nonlinear regression is equivalent to a neural network with one 
hidden layer and infinitely large number of neurons
• Powerful function approximator
• A few mean functions and covariance functions are available for modeling
• Combinations of different mean functions and covariance functions possible

![Page 20](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_020.png)

---

## Page 21

GP for Spatiotemporal Modeling (1)
• Spatiotemporal phenomenon is an event relating to both time and space
• El Nino dataset: 178,080 meteorological measurements across the Pacific
• Air temperature
• Relative humidity
• Surface winds
• Sea surface temperature
• 25 sensors and span of 5 years (daily records)
• Air temperature at one particular location →

![Page 21](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_021.png)

---

## Page 22

GP for Spatiotemporal Modeling (2)
• Prediction at 40 uniformly spaced 
time points using 30 measurements
• Mean function 𝑚(𝑥) = 27
• SE covariance function with 𝑙= 100 
days, 𝜎𝑓= 1, 𝜎𝑣= 1
• Prediction at 200 uniformly spaced 
time points using 100 measurements
• Mean function 𝑚(𝑥) = 27
• SE covariance function with 𝑙= 100 
days, 𝜎𝑓= 1, 𝜎𝑣= 1

![Page 22](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_022.png)

---

## Page 23

References
Book Chapters
[1]. C. E. Rasmussen and C. K. I. Williams, Gaussian Processes for Machine Learning, The MIT Press, 2006.
[2]. K. Murphy, Probabilistic Machine Learning: An introduction, Chapter 17, Book Draft, 2021.
Scalable GP:
[3]. Liu et. al., When Gaussian Processes meets big data: A review with scalable GPs, IEEE Trans. Neural 
Networks and Learning Systems, 2020
Spatiotemporal Modeling:
[4]. C. Jidling, Tailoring Gaussian Processes for Tomographic Reconstruction, PhD Dissertation, Uppsala 
University, 2019.
[5]. Singh et. al., Efficient informative sensing using multiple robots, Journal of Artificial Intelligence 
Research, 2009.
[6]. Kopp et. al., Temperature-driven global sea-level variability in the common era, PNAS, 2016.
[7]. Guestrin et. al., Near-optimal sensor placements in Gaussian Processes. ICML, 2005.

![Page 23](../course.material/figs/2025-05-16%20Introduction%20to%20GP-1/page_023.png)

---

