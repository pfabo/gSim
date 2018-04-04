v 20130925 2
C 40000 40000 0 0 0 title-bordered-A3.sym
T 49300 40900 9 14 1 0 0 0 2
Example 351
Transient Analysis 
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / A
T 53300 40300 9 8 1 0 0 0 1
090908 PF
C 50850 43950 1 0 0 spice-directive.sym
{
T 50850 44650 5 10 0 0 0 0 1
device=directive
T 50950 44350 5 10 1 1 0 0 1
refdes=A1
T 50950 44050 5 10 1 1 0 0 1
value=.TRAN 0.1ns 400ns
}
C 44850 44100 1 0 0 pwr-gnd.sym
{
T 45140 44760 5 10 0 0 0 0 1
value=GND
T 45130 45150 5 10 0 0 0 0 1
device=SYMBOL
}
N 44850 44300 44850 44450 4
C 44550 44450 1 0 0 spice-vpulse.sym
{
T 45250 45100 5 10 1 1 0 0 1
refdes=V1
T 45250 45500 5 10 0 0 0 0 1
device=SPICE
T 43350 43800 5 10 1 1 0 0 1
value=DC 0 PULSE 0 10V 1ns 1ns 1ns 38ns 80ns
}
C 49000 45900 1 0 0 port-sout.sym
{
T 49250 46000 5 10 1 1 0 1 1
net=OUT:1
T 49200 46200 5 10 0 0 0 0 1
device=SYMBOL
T 50150 47250 5 10 0 0 0 7 1
value=NET
}
N 47200 46000 49000 46000 4
N 46300 46000 44850 46000 4
{
T 44850 46050 5 10 1 1 0 0 1
netname=IN
}
N 44850 46000 44850 45650 4
C 48400 44400 1 90 0 cap.sym
{
T 47700 44600 5 10 0 0 90 0 1
device=CAPACITOR
T 48500 44850 5 10 1 1 0 0 1
refdes=C1
T 47500 44600 5 10 0 0 90 0 1
symversion=0.1
T 48500 44650 5 10 1 1 0 0 1
value=10pF
T 46900 44600 5 10 0 0 90 0 1
footprint=NONE
}
C 48200 44100 1 0 0 pwr-gnd.sym
{
T 48490 44760 5 10 0 0 0 0 1
value=GND
T 48480 45150 5 10 0 0 0 0 1
device=SYMBOL
}
N 48200 44300 48200 44600 4
N 48200 45100 48200 46000 4
C 46300 45900 1 0 0 res.sym
{
T 46400 46500 5 10 0 0 0 0 1
device=RESISTOR
T 46650 46200 5 10 1 1 0 0 1
refdes=R1
T 46650 45650 5 10 1 1 0 0 1
value=5k
}