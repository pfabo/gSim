v 20130925 2
C 40000 40000 0 0 0 title-bordered-A3.sym
C 45000 44600 1 0 0 pwr-gnd.sym
{
T 45290 45260 5 10 0 0 0 0 1
value=GND
T 45280 45650 5 10 0 0 0 0 1
device=SYMBOL
}
N 45000 44800 45000 44950 4
T 49300 40900 9 14 1 0 0 0 2
Example 300
Bipolar transistor amplifier circuit
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / A
T 53300 40300 9 8 1 0 0 0 1
090919 PF
C 44700 44950 1 0 0 spice-vsin.sym
{
T 45400 45500 5 10 1 1 0 0 1
refdes=V1
T 45400 45800 5 10 0 0 0 0 1
device=spice
T 45400 46000 5 10 0 0 0 0 1
footprint=none
T 45150 45050 5 10 1 1 0 0 1
value=DC 0 AC 1V
}
N 47250 46350 49050 46350 4
N 45000 46350 46350 46350 4
{
T 45050 46400 5 10 1 1 0 0 1
netname=IN
}
N 45000 46350 45000 46150 4
C 48000 44800 1 0 0 pwr-gnd.sym
{
T 48290 45460 5 10 0 0 0 0 1
value=GND
T 48280 45850 5 10 0 0 0 0 1
device=SYMBOL
}
N 48000 45000 48000 45350 4
N 48000 45850 48000 46350 4
C 49050 46250 1 0 0 port-out.sym
{
T 49300 46350 5 10 1 1 0 1 1
net=OUT:1
T 49250 47000 5 10 0 0 0 0 1
device=none
T 49300 46150 5 10 0 1 0 1 1
value=OUTPUT
}
C 46700 43150 1 0 0 spice-directive.sym
{
T 46700 43850 5 10 0 0 0 0 1
device=directive
T 46800 43550 5 10 1 1 0 0 1
refdes=A1
T 46550 43250 5 10 1 1 0 0 1
value=.AC DEC 100 1Hz 1MEG
}
C 48200 45150 1 90 0 cap.sym
{
T 47500 45350 5 10 0 0 90 0 1
device=CAPACITOR
T 48300 45650 5 10 1 1 0 0 1
refdes=C1
T 47300 45350 5 10 0 0 90 0 1
symversion=0.1
T 48300 45450 5 10 1 1 0 0 1
value=10uF
T 46700 45350 5 10 0 0 90 0 1
footprint=NONE
}
C 46350 46250 1 0 0 res.sym
{
T 46450 46850 5 10 0 0 0 0 1
device=RESISTOR
T 46700 46500 5 10 1 1 0 0 1
refdes=R1
T 46700 46050 5 10 1 1 0 0 1
value=500
}