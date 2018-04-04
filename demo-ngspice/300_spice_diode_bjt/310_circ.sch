v 20130925 2
C 40000 40000 0 0 0 title-bordered-A3.sym
T 49300 40900 9 14 1 0 0 0 2
Example 310
Sawtooh Waveform Generator
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / A
T 53300 40300 9 8 1 0 0 0 1
100214 PF
C 50950 45800 1 0 0 spice-vdc.sym
{
T 51700 46550 5 10 1 1 0 0 1
refdes=V1
T 51650 46650 5 10 0 0 0 0 1
device=spice
T 51650 46850 5 10 0 0 0 0 1
footprint=none
T 51700 46250 5 10 1 1 0 0 1
value=DC 15V
}
C 51250 45350 1 0 0 pwr-gnd.sym
{
T 51540 46010 5 10 0 0 0 0 1
value=GND
T 51530 46400 5 10 0 0 0 0 1
device=SYMBOL
}
N 51250 47000 51250 47050 4
N 51250 45800 51250 45550 4
C 51250 47050 1 0 0 pwr-15v-plus.sym
{
T 51050 47350 5 10 1 1 0 0 1
value=+15V
T 51350 48150 5 10 0 0 0 0 1
device=SYMBOL
}
C 50250 44000 1 0 0 spice-directive.sym
{
T 50250 44700 5 10 0 0 0 0 1
device=directive
T 50350 44400 5 10 1 1 0 0 1
refdes=A1
T 50200 44100 5 10 1 1 0 0 1
value=.TRAN 1us 20ms UIC
}
C 44950 45650 1 0 1 port-sout.sym
{
T 44700 45750 5 10 1 1 0 7 1
net=OUT:1
T 44750 45950 5 10 0 0 0 6 1
device=SYMBOL
T 43800 47000 5 10 0 0 0 1 1
value=NET
}
C 47100 43500 1 90 0 res.sym
{
T 46500 43600 5 10 0 0 90 0 1
device=RESISTOR
T 47150 44000 5 10 1 1 0 0 1
refdes=R4
T 47150 43750 5 10 1 1 0 0 1
value=100
}
C 45700 44800 1 90 0 cap.sym
{
T 45000 45000 5 10 0 0 90 0 1
device=CAPACITOR
T 44850 45250 5 10 1 1 0 0 1
refdes=C1
T 44800 45000 5 10 0 0 90 0 1
symversion=0.1
T 44850 45000 5 10 1 1 0 0 1
value=22nF
T 44200 45000 5 10 0 0 90 0 1
footprint=NONE
T 44850 44750 5 10 1 0 0 0 1
ic=0
}
C 46400 44700 1 0 0 npn.sym
{
T 46500 46450 5 10 0 0 0 0 1
device=NPN
T 46450 44800 5 8 1 1 0 0 1
refdes=Q2
T 47000 45100 5 8 1 1 0 0 1
value=NPN
}
C 46750 46650 1 180 0 pnp.sym
{
T 46650 44900 5 10 0 0 180 0 1
device=PNP
T 46600 46600 5 8 1 1 180 0 1
refdes=Q1
T 46150 46250 5 8 1 1 180 0 1
value=PNP
}
N 47000 46250 47000 45500 4
N 46150 44400 46150 45850 4
C 49050 45100 1 90 0 res.sym
{
T 48450 45200 5 10 0 0 90 0 1
device=RESISTOR
T 49100 45600 5 10 1 1 0 0 1
refdes=R2
T 49100 45350 5 10 1 1 0 0 1
value=3k3
}
C 49050 46650 1 90 0 res.sym
{
T 48450 46750 5 10 0 0 90 0 1
device=RESISTOR
T 49100 47150 5 10 1 1 0 0 1
refdes=R1
T 49100 46900 5 10 1 1 0 0 1
value=1k5
}
C 45600 46650 1 90 0 res.sym
{
T 45000 46750 5 10 0 0 90 0 1
device=RESISTOR
T 45650 47150 5 10 1 1 0 0 1
refdes=R5
T 45650 46900 5 10 1 1 0 0 1
value=100k
}
C 46250 43500 1 90 0 res.sym
{
T 45650 43600 5 10 0 0 90 0 1
device=RESISTOR
T 45700 44000 5 10 1 1 0 0 1
refdes=R3
T 45700 43750 5 10 1 1 0 0 1
value=39k
}
N 46750 46250 48950 46250 4
N 48950 46000 48950 46650 4
N 47000 44400 47000 44700 4
N 46150 46650 45500 46650 4
N 45500 46650 45500 45500 4
N 45500 47550 45500 47750 4
N 45500 47750 48950 47750 4
N 48950 47750 48950 47550 4
N 45500 45000 45500 44750 4
N 48950 44900 48950 45100 4
N 46150 43500 46150 43250 4
N 47000 43250 47000 43500 4
C 47000 43050 1 0 0 pwr-gnd.sym
{
T 47290 43710 5 10 0 0 0 0 1
value=GND
T 47280 44100 5 10 0 0 0 0 1
device=SYMBOL
}
C 46750 48000 1 0 0 pwr-15v-plus.sym
{
T 46550 48300 5 10 1 1 0 0 1
value=+15V
T 46850 49100 5 10 0 0 0 0 1
device=SYMBOL
}
N 46750 48000 46750 47750 4
N 44950 45750 45500 45750 4
C 47450 44400 1 0 0 port-sout.sym
{
T 47700 44500 5 10 1 1 0 1 1
net=VE:1
T 47650 44700 5 10 0 0 0 0 1
device=SYMBOL
T 48600 45750 5 10 0 0 0 7 1
value=NET
}
N 47450 44500 47000 44500 4
N 46400 45100 46150 45100 4
C 45500 44550 1 0 0 pwr-gnd.sym
{
T 45790 45210 5 10 0 0 0 0 1
value=GND
T 45780 45600 5 10 0 0 0 0 1
device=SYMBOL
}
C 46150 43050 1 0 0 pwr-gnd.sym
{
T 46440 43710 5 10 0 0 0 0 1
value=GND
T 46430 44100 5 10 0 0 0 0 1
device=SYMBOL
}
C 48950 44700 1 0 0 pwr-gnd.sym
{
T 49240 45360 5 10 0 0 0 0 1
value=GND
T 49230 45750 5 10 0 0 0 0 1
device=SYMBOL
}
