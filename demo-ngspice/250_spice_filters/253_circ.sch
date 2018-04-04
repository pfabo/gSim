v 20130925 2
C 40000 40000 0 0 0 title-bordered-A3.sym
C 47550 46000 1 0 0 spice-directive-1.sym
{
T 47650 46300 5 10 0 1 0 0 1
device=directive
T 47650 46400 5 10 1 1 0 0 1
refdes=A1
T 47550 46100 5 10 1 1 0 0 1
value=.AC DEC 1000 10Hz 10kHz
}
T 49300 40900 9 14 1 0 0 0 2
Example 00811
50Hz notch filter
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / B
T 53300 40300 9 8 1 0 0 0 1
100104 PF
C 41700 45250 1 0 0 pwr-gnd.sym
{
T 41990 45910 5 10 0 0 0 0 1
value=GND
T 41980 46300 5 10 0 0 0 0 1
device=SYMBOL
}
N 41700 47150 42350 47150 4
{
T 41800 47200 5 10 1 1 0 0 1
netname=IN
}
N 41700 47150 41700 46850 4
N 41700 45450 41700 45650 4
C 41400 45650 1 0 0 spice-vac.sym
{
T 42100 46300 5 10 1 1 0 0 1
refdes=V1
T 42100 46500 5 10 0 0 0 0 1
device=spice
T 42100 46700 5 10 0 0 0 0 1
footprint=none
T 42100 46100 5 10 1 1 0 0 1
value=dc 0 ac 0.1
}
C 42350 47050 1 0 0 res.sym
{
T 42500 47650 5 10 0 0 0 0 1
device=RESISTOR
T 42750 47300 5 10 1 1 0 0 1
refdes=R1
T 42550 46850 5 10 1 1 0 0 1
value=6516
T 42500 48050 5 10 0 0 0 0 1
footprint=1206.fp
}
C 47550 48850 1 180 1 opamp.sym
{
T 47650 46200 5 10 0 0 180 6 1
device=OPAMP
T 48150 48200 5 10 1 1 180 6 1
refdes=X1
T 47645 45775 5 10 0 0 180 6 1
value=OPAMP
}
C 46150 45850 1 90 0 res.sym
{
T 45550 46000 5 10 0 0 90 0 1
device=RESISTOR
T 45550 46300 5 10 1 1 0 0 1
refdes=R2
T 45550 46100 5 10 1 1 0 0 1
value=342
T 45150 46000 5 10 0 0 90 0 1
footprint=1206.fp
}
C 46050 45250 1 0 0 pwr-gnd.sym
{
T 46340 45910 5 10 0 0 0 0 1
value=GND
T 46330 46300 5 10 0 0 0 0 1
device=SYMBOL
}
N 46050 45450 46050 45850 4
C 46250 47450 1 90 0 cap.sym
{
T 44550 47650 5 10 0 0 90 0 1
device=CAPACITOR
T 46300 47900 5 10 1 1 0 0 1
refdes=C2
T 45350 47650 5 10 0 0 90 0 1
symversion=0.1
T 46300 47700 5 10 1 1 0 0 1
value=97.67nF
T 44750 47650 5 10 0 0 90 0 1
footprint=1206.fp
}
C 49300 48350 1 0 0 port-out.sym
{
T 49550 48450 5 10 1 1 0 1 1
net=OUT:1
T 49500 49100 5 10 0 0 0 0 1
device=none
T 49550 48250 5 10 0 1 0 1 1
value=OUTPUT
}
C 43900 47450 1 90 0 cap.sym
{
T 42200 47650 5 10 0 0 90 0 1
device=CAPACITOR
T 43950 47900 5 10 1 1 0 0 1
refdes=C1
T 43000 47650 5 10 0 0 90 0 1
symversion=0.1
T 43950 47700 5 10 1 1 0 0 1
value=97.72nF
T 42400 47650 5 10 0 0 90 0 1
footprint=1206.fp
}
C 43800 48550 1 0 0 res.sym
{
T 43950 49150 5 10 0 0 0 0 1
device=RESISTOR
T 44200 48800 5 10 1 1 0 0 1
refdes=R3
T 43900 48350 5 10 1 1 0 0 1
value=123805
T 43950 49550 5 10 0 0 0 0 1
footprint=1206.fp
}
C 44950 48550 1 0 0 res.sym
{
T 45100 49150 5 10 0 0 0 0 1
device=RESISTOR
T 45350 48800 5 10 1 1 0 0 1
refdes=R4
T 45200 48350 5 10 1 1 0 0 1
value=6516
T 45100 49550 5 10 0 0 0 0 1
footprint=1206.fp
}
N 43250 47150 46050 47150 4
N 46050 46750 46050 47650 4
N 46050 48150 46050 48650 4
N 45850 48650 47550 48650 4
N 44950 48650 44700 48650 4
N 43800 48650 43700 48650 4
N 43700 48150 43700 49650 4
N 43700 47650 43700 47150 4
C 47450 47700 1 0 0 pwr-gnd.sym
{
T 47740 48360 5 10 0 0 0 0 1
value=GND
T 47730 48750 5 10 0 0 0 0 1
device=SYMBOL
}
N 47550 48250 47450 48250 4
N 47450 48250 47450 47900 4
N 49300 48450 48550 48450 4
N 43700 49650 49000 49650 4
N 49000 49650 49000 48450 4