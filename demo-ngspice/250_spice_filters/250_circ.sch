v 20130925 2
C 40000 40000 0 0 0 title-bordered-A3.sym
C 41750 43800 1 0 0 spice-directive-1.sym
{
T 41850 44100 5 10 0 1 0 0 1
device=directive
T 41850 44200 5 10 1 1 0 0 1
refdes=A1
T 41750 43900 5 10 1 1 0 0 1
value=.AC DEC 1000 10Hz 50kHz
}
T 49300 40900 9 14 1 0 0 0 2
Example 00800
LQLF filter
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / A
T 53300 40300 9 8 1 0 0 0 1
100104 PF
C 41850 45000 1 0 0 pwr-gnd.sym
{
T 42140 45660 5 10 0 0 0 0 1
value=GND
T 42130 46050 5 10 0 0 0 0 1
device=SYMBOL
}
N 41850 46900 41850 46600 4
N 41850 45200 41850 45400 4
C 41550 45400 1 0 0 spice-vac.sym
{
T 42250 46050 5 10 1 1 0 0 1
refdes=V1
T 42250 46250 5 10 0 0 0 0 1
device=spice
T 42250 46450 5 10 0 0 0 0 1
footprint=none
T 42250 45850 5 10 1 1 0 0 1
value=DC 0 AC 1
}
C 43600 46800 1 0 0 res.sym
{
T 43750 47400 5 10 0 0 0 0 1
device=RESISTOR
T 44000 47050 5 10 1 1 0 0 1
refdes=R3
T 43950 46600 5 10 1 1 0 0 1
value=13.5k
T 43750 47800 5 10 0 0 0 0 1
footprint=1206.fp
}
C 42400 46800 1 0 0 res.sym
{
T 42550 47400 5 10 0 0 0 0 1
device=RESISTOR
T 42800 47050 5 10 1 1 0 0 1
refdes=R11
T 42750 46600 5 10 1 1 0 0 1
value=6.6k
T 42550 47800 5 10 0 0 0 0 1
footprint=1206.fp
}
N 45900 47100 47000 47100 4
N 43600 46900 43300 46900 4
N 46000 47100 46000 48150 4
N 44900 47300 44800 47300 4
N 44800 47300 44800 48150 4
N 44500 46900 44900 46900 4
C 43800 47950 1 0 0 cap.sym
{
T 44000 49650 5 10 0 0 0 0 1
device=CAPACITOR
T 44400 48500 5 10 1 1 0 0 1
refdes=C2
T 44000 48850 5 10 0 0 0 0 1
symversion=0.1
T 44400 48300 5 10 1 1 0 0 1
value=27nF
T 44000 49450 5 10 0 0 0 0 1
footprint=1206.fp
}
C 45000 45850 1 90 0 cap.sym
{
T 43300 46050 5 10 0 0 90 0 1
device=CAPACITOR
T 45050 46300 5 10 1 1 0 0 1
refdes=C4
T 44100 46050 5 10 0 0 90 0 1
symversion=0.1
T 45050 46100 5 10 1 1 0 0 1
value=3.3nF
T 43500 46050 5 10 0 0 90 0 1
footprint=1206.fp
}
C 44800 45550 1 0 0 pwr-gnd.sym
{
T 45090 46210 5 10 0 0 0 0 1
value=GND
T 45080 46600 5 10 0 0 0 0 1
device=SYMBOL
}
N 44500 48150 46000 48150 4
N 44800 46550 44800 46900 4
N 44800 45750 44800 46050 4
N 44000 48150 43450 48150 4
N 43450 48150 43450 46900 4
C 44900 47500 1 180 1 opamp.sym
{
T 45000 44850 5 10 0 0 180 6 1
device=OPAMP
T 45500 46850 5 10 1 1 180 6 1
refdes=X1
T 44995 44425 5 10 0 0 180 6 1
value=OPAMP
}
C 43550 45850 1 90 0 res.sym
{
T 42950 46000 5 10 0 0 90 0 1
device=RESISTOR
T 43650 46400 5 10 1 1 0 0 1
refdes=R12
T 43650 46200 5 10 1 1 0 0 1
value=10k
T 42550 46000 5 10 0 0 90 0 1
footprint=1206.fp
}
C 43450 45550 1 0 0 pwr-gnd.sym
{
T 43740 46210 5 10 0 0 0 0 1
value=GND
T 43730 46600 5 10 0 0 0 0 1
device=SYMBOL
}
N 43450 46750 43450 46900 4
N 43450 45750 43450 45850 4
N 41850 46900 42400 46900 4
{
T 41950 46950 5 10 1 1 0 0 1
netname=IN
}
C 47000 47000 1 0 0 port-out.sym
{
T 47250 47100 5 10 1 1 0 1 1
net=OUT:1
T 47200 47750 5 10 0 0 0 0 1
device=none
T 47250 46900 5 10 0 1 0 1 1
value=OUTPUT
}
