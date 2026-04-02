# Applied Engineering Optimisation - Power Systems Optimisation Lecture 1 NOTES

*Converted from PDF: Applied Engineering Optimisation - Power Systems Optimisation Lecture 1 NOTES.pdf*

---

## Page 1

Economic Dispatch Formulation
min
Ci
subject to:
PGin
PGax
=
PD
Classification:
Confidence
PGi
PGi
PGi

![Page 1](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20Lecture%201%20NOTES/page_001.png)

---

## Page 2

Economic Dispatch Example
D
1
2
2
1
1
1
1
2
2
2
2
2
1
1
1
What is economic dispatch for a two generator 
system P
500 MW  and
(
)
1000 20
0.01
$/
(
)
400 15
0.03
$/
Using the Largrange multiplier method we know
(
)
20
0
G
G
G
G
G
G
G
G
G
G
P
P
C P
P
P
hr
C
P
P
P
hr
dC P
dP

=
+
=
=
+
+
=
+
+
−
=
+
1
2
2
2
2
1
2
.02
0
(
)
15
0.06
0
500
0
G
G
G
G
G
G
P
dC
P
P
dP
P
P



−
=
−
=
+
−
=
−
−
=

![Page 2](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20Lecture%201%20NOTES/page_002.png)

---

## Page 3

Economic Dispatch Example, cont’d
1
2
1
2
1
2
1
2
We therefore need to solve three linear equations
20
0.02
0
15
0.06
0
500
0
0.02
0
1
20
0
0.06
1
15
1
1
500
312.5 MW
187.5 MW
26.2 $/MWh
G
G
G
G
G
G
G
G
P
P
P
P
P
P
P
P




+
−
=
+
−
=
−
−
=
−
−










−
=
−





−
−
−













=

















![Page 3](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20Lecture%201%20NOTES/page_003.png)

---

## Page 4

Two Bus Penalty Factor Example
2
2
2
(
)
(
)
0.37
0.0387
0.037
10
0.9627
0.9643
L
G
L
G
G
Gi
P P
P P
MW
P
P
MW
L
L


−
= −
=
= −


=


![Page 4](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20Lecture%201%20NOTES/page_004.png)

---

## Page 5

AC OPF Formulation
min
Cf (G)
geg
subject to
G
L
Pg
=
PD +
Pbb' +
GBvz
(2)
gegb
dedb
6'ebb
4G
Q8 +
qbb'
_
BBvz
(3)
gegb
dedb
6'ebb
L
pbb'
=
2} Gbb +ubut' (Gbb' cos(0b - 06'
+Bbb' sin(Ot ~ Ab' ))
L
4bb'
3
L
v& Bbb +UbUb' ( Gbb' sin(0b ~ 06' )
7
cos(06 ~ Ov' ) )
=0
"fB < Ub < vfB
;
9
<pg <
9
QGB < 9g < QYB
(9)
L
2
L
2
2
pbb'
(Sbbax
(10)
Bbb'
Hbo
pLB
PUB
+ 46b'

![Page 5](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20Lecture%201%20NOTES/page_005.png)

---

## Page 6

DC optimal power flow
•
As an example, let’s look at Transpower’s DC OPF (solved every 5 minutes for 
real-time dispatch) here

![Page 6](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20Lecture%201%20NOTES/page_006.png)

---

