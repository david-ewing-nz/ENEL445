# Project 2 FDOA-only Geolocation-2

*Converted from PDF: Project 2 FDOA-only Geolocation-2.pdf*

---

## Page 1

6.2.
SUGGESTED PROJECT 2: SOURCE GEOLOCATION USING FREQUENCY MEASUREMEN
6.2
Suggested Project
2:
Source
Geolocation using
Frequency Measurements
Project Summary
Formulate the source geolocation problem under Gaussian measurement noise a8 a
nonlinear least squares (NLS) problem:
Derive the analytical expression for the gradient of the cost function and validate
vour results using numerical methods for computing the derivatives
Design and realize your
OWI
gradient-based algorithm with line search that takes
into account the bound constraints O1 the design variables
Evaluate the geolocation accuracy of your method undler different noise levels and
compare it with at least one benchmark method at your choice.
Analyze the efficiency of Your method in terms of the number of iterations required
by YOur gradient-based algorithm and the number of objective function evaluations
required by your line search method.
6.2.1
Problem Description
Geolocation of radio sources on the Earth surface is
classic estimation problem,
which has found numerous civil and military applications in navigation, search and rescue,
and surveillance.
In this project ,
we shall consider the use of four satellites to locate
ground radio
source using the frequency
difference of arrival (FDOA) measurements only:
This is
known in some literature as FDOA-only localization; which is & recently exploited topic_
For
example. see the paper below and references there in:
[1]:
Y.
Pei_
X
Li; Le
and F.
A closed-form solution for source localization
using FDOA
measurements only;
IEEE Communications Letters, vol
27,
pp.
115-119,
Jan. 2022_
6.2.2
Mathematical Background
In FDOA-only geolocation, each satellite in the satellite group receives the signal ofthe
same radio source. The source is located at u?
[x' ,y" , 2'T in the Earth Centered Earth
Fixed (ECEF
coordinate system: Its geodetic position is denoted as p"
[B' , L' , He]T ,
where Bo
Lo and
IIo represents the latitude, longitude and altitude.
Since the radio
source is assumed to be on the ground,
we have Ho _ 0.
The Cartesian coordinates u'
are related to p" via
(RE(B') + H)cos( Bo)cos( L") ;
(6.1a)
y"
(RE(B') + H)cos( B')sin( L') ,
(6.1b)
= [(1 _ e2)Re(B') + HJsin(B');
(6.lc)
where
Ro
RE(Bo)
(6.2)
e2sin? ( Bo)
Guo.
Yang
V1 -

![Page 1](../course.material/figs/Project%202%20FDOA-only%20Geolocation-2/page_001.png)

---

## Page 2

56
CHAPTER 6.
DESIGN PROJECTS
0.081819198425 is the eccentricity;
and Ro
6378.137km is the Earth equatorial
radius_
MATLAB functions 0n coordinate conversion,
sCC
"hittps: ,
MV IV
nathworks com/help/map/ref/ geodeticZecef htil,
"littps:,
WWW.mathworks com /help/ map/rel/ ecel2geodetic html.
Let
uS denote the position and velocity of satellite
1,2,3,4,
in the ECEF
coordinate system
as S;
[Sw,i, Sy,i, 82,]T
and S;
[3r,i, Sy,i, 8_,]T .
Suppose the radio
source is
transmitting with an unknown frequency fo:  The signal frequency measured at
satellite i is thus subject to the Doppler effect and is equal to
(u?
Si)Ts;
fi = fo +
A
+ ni;
(6.3)
Iluo
Si|l
where A =
fo is the source signal wavelength; and n; is the Gaussian random noise with
zero mean and variance 0f (i.e,, n; ~ N(0,0})).
Since the source signal  frequency is not known, we subtract the received frequency
at satellite 1 (also called the reference satellite)
the received frequencies at other
satellites to obtain the FDOA
measurements
Specifically;
the
measured FDOA
fjl
between the satellite
j and 1,j = 2,3,4, is
(u?
s;)Ts;
(u" _
S1 )Ts,
fju = f; - fi =
1
n1 ) _
(6.4)
Iluo
s;ll
Iluo
S1
Collecting  f;u for
2,3,4 generates the
measurement vector f
[f21, fs1, f4]T .
Besides, define
L") as the true FDOA function
[g(B' , L' , 82,82) _
L" , 81,81)
g(B' , L")
g( Bo , L" , 83, 83 _
9(B' , L' , S1,51)
(6.5)
L" , 84, 84)
L' , S1, S1 _
where from
'6.4) .
(u"
S;)T s;
Lo , Si,S;) =
(6.6)
|lue
S;|l
The measurement noise in f is thus equal to nf, which is
n2
n1
nf
n3
n1
(6.7)
n4
n[
We
are interested in identifying the source position p
(with its altitude
Ho
0)
the measured FDOAs in f as well as the known satellite positions S; and velocities
Si, i = 1,2,3,4.
1This is how the
namc
FDOA
comes
from.
We
arc
indeed the difference of the Doppler
frequencies received at various satellites for
sOurCC
geolocation:
For
from
pair
(nj
g( B .
9( Bo .
9( Bo.
9( Bo .
9(Bo .
using
using

![Page 2](../course.material/figs/Project%202%20FDOA-only%20Geolocation-2/page_002.png)

---

## Page 3

6.2.
SUGGESTED PROJECT 2: SOURCE GEOLOCATION USING FREQUENCY MEASUREMEN
6.2.3
Guidelines for Progress Report
1) . (30) Show that the FDOA measurement vector f follows & multivariate Gaussian
distribution with mean
L') and covariance 0}Q, where Q takes the form
(6.8)
2
Then, formulate the FDOA-only geolocation problem using the maximum likelihood (VL)
estimation principle as
nonlinear least-squares problem:
Hint: Refer to Chapter
in this notes for an introduction to the multivariate Gaus-
sian density and ML estimation.
2) .
(40%)
Consider the following scenario.
The radio source has
a carrier
frequency
of fo
1GHz.
It is located at p"
[59,109 , 0jT
where 59 means the north latitude of
5 degrees and
109 means the east longitude of 10
degrees:
The satellite positions and
velocities are listed below:
S1
[7378.1,
0,
0]T km; $1
0.0001,4.4995, 5.3623]T km
82
[7377.5,
100 _
OJT km; $2
-0.0671,4.9493,4.9497]
km_
83
[7377.5,~100 ,
0]" km; 83
0.0610,4.4991,5.3623
km
54
[7377.5,
0
100JT km; s4
[-0.0777,4.0150,5.7335]T km/s
It is priorly known that the latitude and longitude of the radio source are  within
[0, 408] and [0, 402].
Implement the
search
method for accomplishing geolocation_
The
search process is as follows. First , the priorly known location area of the radio
source is covered with
uniform
We then evaluate the objective function at each
The
point with the minimum objective function value is output as the
geolocation result.
In the progress report. assume that the signal frequency of the radio source is known.
3).
(30%) Implement
a Monte Carlo simulation program to investigate the geoloca-
tion accuracy of yOur
search method in terms of estimation root mean square error
(RMSE) under different FDOA noise levels
1,2,4,8,16Hz)_
Suppose in the &-th Monte
Carlo run; the estimated
source position in the ECEF
coordinates is denoted by
U . The
geolocation RMSE is computed
RMSE
Ilu
uo l2
(6.9)
L
I-1
where L is the total number of Monte Carlo runs (normally set to be e.g; 104).
6.2.4
Guidelines for Final Report
1).
Re-use VOul' progress report that details the problem formulation and grid-based
search mnethod:
2) .
(107) In order to generate the true FDOAs using (6.5), the signal wavelength
needs to be provided:
But it is still not known; a8
c/ fo requires the knowledge on the
g( Bo.
grid
grid
grid.
grid
point .
grid
grid
(0f
using

![Page 3](../course.material/figs/Project%202%20FDOA-only%20Geolocation-2/page_003.png)

---

## Page 4

58
CHAPTER 6.
DESIGN PROJECTS
unknown signal frequency fo: Find
a way to obtain an estimate of the signal wavelength
Justify VOur design by carrying out
an
analysis on the approximation error_
Use this frequency estimate throughout the remaining experiments 
Bonus:
In the current setup;
we  consider exploiting the FDOAs   f21, f31
and  f41
only.
The other possible FDOAs such
as
f23 and f34 are not used_
Address the follow-
question in  Vour final report:
Does utilizing these FDOAs bring any performance
improvement?
Justify your
allswer
using theoretical analysis and you will receive 5% of
JOur' final report mark as bonus_
3). (30%,
Derive with the help of chain rule the analytical expression of the gradient
of the true FDOA g(B' , L',S;,8;-
9(Bo , L" , 81,S1 ) .
Verify your result using the finite
differences mnethod for computing the gradient_
derivatives
see
Chapter 4.4 of this note)_
Bonus: if you can also numerically verify your results
the complex step method
see also Chapter 4.4 of this note) , you will receive 10% of your final report mark as bonus 
4) .
(35%) Select_
modify and implement one of the following gradient-base methods
on your own:
Conjugate gradient
Newton's method
Gauss Newton method
Levenberg-Marquardt algorithm
BFGS algorithm
with line search
and stopping criteria.
See Chapter 4.3 for
a1 introduction
to these
gradient-based algorithms, line search and stopping criteria.
Make sure that in each iteration; the geolocation solution ALWAYS stays in the area
of interest (i.e , the arca with the latitude range [0, 408] and longitude range [0, 402]).
In your implementation, also include & routine to realize the multistart strategy (i.e.
generate multiple initial solutions such that multiple solution sequence
can be produced
using YOur gradient-based method.
You can output the solution with the smallest objec-
tive function value as the final geolocation result). See Chapter 4.3.6 for details_
5) . (25%) Compare, using Monte Carlo simulation; the geolocation accuracy; in terms
of estimation RMSE (see (6.9)). of vour gradient-based algorithm against that of vour
search algorithm (now with the estimated signal frequency) under different frequency
measurement noise levels_
Demonstrate the convergence behavior of your gradient-based algorithm in terms of
the number of iterations required before convergence and the number of objective func-
tion evaluations needed in each line search:
Bonus:  if yOu can implement another optimization algorithm: such
as the particle
swarm
optimization
PSO), for performance comparison;
yOu  will receive 15% of vour
final report mark as bonus_
ing
using
grid

![Page 4](../course.material/figs/Project%202%20FDOA-only%20Geolocation-2/page_004.png)

---

## Page 5

6.2.
SUGGESTED PROJECT 2: SOURCE GEOLOCATION USING FREQUENCY MEASUREMEN
6.2.5
Guidelines for Demo
In YOur presentation; YOu
to cover at least item 1) from the progress report, as
well as items 3), 4) and 5) from the final report _
In words_
we expect to see your problem formulation_
verification of gradient deriva-
tion, gradient-based algorithm design (i.e  the optimization strategy
and
performance
comparison with benchmark technique(s) .
We encourage You to illustrate your design with various types of plots_
As this project
is in fact a 2-D optimization problem, visualization
contours (to show the modality
of the objective function; satellite position, source position; etc), arrowed line segments
to show the gradient direction and line search strategy; and RMSE curves
function of
the FDOA measurement noise variance/standard deviation, can be used.
The marking scheme is similar to that of Project
put  emphasis on the pre-
sentation (209) and graphie illustration (30%).
The quality of your design (307) and
performance (20%) are also considered.
need
using
We

![Page 5](../course.material/figs/Project%202%20FDOA-only%20Geolocation-2/page_005.png)

---

## Page 6

Chapter 7
Mathematics Background:
Part II
7.1
Gaussian Distribution
Perhaps, the most widely used probability distribution is the multivariate Gaussian,
also called multivariate normal (MVN) in
some literature.
It is mathematically
COnve-
nient, and more importantly, Gaussianity is fairly reasonable in many applications
Suppose X € R"x1 follows
multivariate Gaussian distribution; i.e.,
~
N(x; p,2);
which is defined as
N(x; p,Z)
exp
(_
2"2 "6-4)
(7.1)
Vwz|
Here, u
[pt1, 02,
Vn]T
Elx] is the
mean vector and >
E[(x
p) (x ~ p)T] is
the covariance_
The notation | . | represents the matrix determinant_
In particular_
the
covariance matrix Z is
to
val'
(T1_
cov(T1, T2)
cov(T1,Tn_
COV
(82,81
var(T2_
COV
(12,Tn_
(7.2)
cov(Tn, T1 )
cov(Tn,T2
Var
(xn _
where
var(x;) = El(x;
p;)21,
i = 1,2,
n ,
(7.3)
and
cOV
(xi;*j) = El(zi
[)(xj
Vj)]; i,j =1,2,
n;
and i # j
(7.4)
It
can be shown
Exercise 3.4) that Z is symmetric and at least positive semidefinite
When n = 1, (7.1) reduces to the univariate Gaussian distribution
Exercise 3.5) ,
(x
Wl,
02) =
exp
(_6zp2
(7.5)
One application of the Gaussian distribution is a transformation method popular in
machine learning referred to as the re-parameterization trick:
In some cases, the objective
function is the expectation of another function f(y) with
respect
t0
e.g ,
Gaussian
density N(y; Ey, Zy), where the mean /y and covariance Zy are the design variables to
be optimized.
The re-parameterization trick replaces Y
y = py + Lye,
(7.6)
63
equal
8'
N(c;
(2to2
using

![Page 6](../course.material/figs/Project%202%20FDOA-only%20Geolocation-2/page_006.png)

---

## Page 7

64
CHAPTER
MATHEMATICS BACKGROUND: PART II
where Zy = LyLy is the Cholesky decomposition of the covariance Zy; and
e follows
Gaussian density N (e; 0,I).
As a result, the objective function becomes the expectation
of
+ Lye) with respect to the Gaussian dlensity N (e; 0,I) that is HOw independent
of the design variables /y and Zy:
7.2
Maximum Likelihood Estimation
We are interested in estimating the parameter vector 0
e Rrx1 from measurements
(also referred to as training data) in D.
The most commonly used approach for parameter
estimation is to locate the parameter values that assign the highest probability to the
measurements_
This is called the maximum likelihood estimation (MLE), which indeed
requires solving an optimization (maximization) problem.
Mathematically; the MLE is
defined as
= max
P(Dle) ,
(7.7)
where p(Dle) is the distribution function of D parameterized by 0_
Sometimes_
it is convenient t0 work with the logarithm of the objective function
which is
log(p(Dle)).
It can be shown
Exercise 3.6) that this transform does not change
the solution to (7.7).
When the measurements in D = {Y1,Y2,
Ym} are independent and identically dis-
tributed (i.i.d.), the logarithm of the original objective function becomes
log (p(Dle)) = log
p(y;|e)
(7.8)
i=1
To illustrate the concept of MLE, consider the following example where the measure-
ments are generated via
y
[y1; 92,
Ym]
G0 + e;
(7.9)
where G is a m Xr measurement matrix
€ is the additive zero-mean Gaussian
measure-
ment noise (i.e.
N (e; 0,2)).
It can be shown
Exercise 3.7) that the measurements
in y follows & Gaussian distribution given by
p(yle) = N(y; G0,2).
(7.10)
Note that in this case, the parameter vector 0 determines the mean of the measurements
GO, which according to (7.9) , is also the unknown true values of the measurements_
To find the MLE of 0
we first notice that the logarithm of the objective function
p(yl0) in
7.10 -
is, from (7.1)
log(p(yle)) x ~(y
Ge)tz-1(y
G0);
(7.11)
where all the terms uot  depending
OHl
0 have been   dropped:
The MLE of 0 for this
particular example is thus given by
= max
log(p(yle))
= min (y -
GO)Tz-1(y-
Ge):
(7.12)
If the covariance of the noise
Z, is
diagonal matrix with the diagonal elements
equal to one another (i.e._
X
62). the MLE problem in (7.12
reduces to
= max
log(p(y/0))
mnin (y
G0)T (y
Ge):
(7.13)
f(pu
being

![Page 7](../course.material/figs/Project%202%20FDOA-only%20Geolocation-2/page_007.png)

---

## Page 8

7.2.
MAXIMUM LIKELIHOOD ESTIMATION
65
This is in fact
a linear least squares (LLS) problem:
If 2
has non-identical diagonal
elements and/o it is not
diagonal matrix; the MLE problem in (7.12
is
weighted
least squares (WLS) problei in the sense that each measurement is not equally weighted
in the objective function_
Ideally; we can emphasize those measurements if we know
have better quality; to improve the estimation accuracy:
It can be shown by using the
results in Chapter 2.3 of the course notes
Exercise 3.8) that the MLE
(7.12) is
0 =
(GTx-'G)-'GTx-Iy:
(7.14)
An important extension
to the measurement
model in (7.9) is that the true
mea-
surements
are HOW
nonlincarly related to the unknown parameters   Mathematically;
we
have
y = g(0) + €
(7.15)
Here; the nonlinear measurement function g(0) is defined as
g(0) = [91(0) , 92(0), 
Im
(0)]" ,
(7.16)
where gi (0) produces the true value of the i-th measurement yi; i = 1,2,
m.
In this case, the MLE of 0 is found by solving
= max
log(p(yle))
= min
(y
g(0))Tz-'(y_
g(0)).
(7.17)
This is called the nonlinear least squares (NLS) problem_
This formulation will be
ex-
plored in the course project provide by Le
it is
an
unconstrained optimization
problem that
can be solved by methods that was presented in Chapter
4 of this notes_
they
from
Yang.

![Page 8](../course.material/figs/Project%202%20FDOA-only%20Geolocation-2/page_008.png)

---

## Page 9

66
CHAPTER
MATHEMATICS BACKGROUND: PART II

![Page 9](../course.material/figs/Project%202%20FDOA-only%20Geolocation-2/page_009.png)

---

