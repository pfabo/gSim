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
Example 00301
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
value=DC 0 AC 1mV
}
C 47250 46450 1 180 0 res.sym
{
T 47100 45850 5 10 0 0 180 0 1
device=RESISTOR
T 46700 46500 5 10 1 1 0 0 1
refdes=R1
T 46600 46050 5 10 1 1 0 0 1
value=500
T 47100 45450 5 10 0 0 180 0 1
footprint=1206.fp
}
C 47550 44300 1 0 0 pwr-gnd.sym
{
T 47840 44960 5 10 0 0 0 0 1
value=GND
T 47830 45350 5 10 0 0 0 0 1
device=SYMBOL
}
C 48650 44650 1 90 0 res.sym
{
T 48050 44800 5 10 0 0 90 0 1
device=RESISTOR
T 48800 45100 5 10 1 1 0 0 1
refdes=R5
T 48800 44900 5 10 1 1 0 0 1
value=500
T 47650 44800 5 10 0 0 90 0 1
footprint=1206.fp
}
C 48650 47350 1 90 0 res.sym
{
T 48050 47500 5 10 0 0 90 0 1
device=RESISTOR
T 48800 47800 5 10 1 1 0 0 1
refdes=R4
T 48800 47600 5 10 1 1 0 0 1
value=100k
T 47650 47500 5 10 0 0 90 0 1
footprint=1206.fp
}
C 47650 47350 1 90 0 res.sym
{
T 47050 47500 5 10 0 0 90 0 1
device=RESISTOR
T 47100 47800 5 10 1 1 0 0 1
refdes=R2
T 47050 47600 5 10 1 1 0 0 1
value=100k
T 46650 47500 5 10 0 0 90 0 1
footprint=1206.fp
}
C 47650 44650 1 90 0 res.sym
{
T 47050 44800 5 10 0 0 90 0 1
device=RESISTOR
T 47750 45100 5 10 1 1 0 0 1
refdes=R3
T 47750 44900 5 10 1 1 0 0 1
value=10k
T 46650 44800 5 10 0 0 90 0 1
footprint=1206.fp
}
N 48550 46750 48550 47350 4
N 47250 46350 47950 46350 4
{
T 47650 46400 5 10 1 1 0 0 1
netname=NB
}
N 47550 46350 47550 47350 4
N 47550 44650 47550 44500 4
C 48550 44300 1 0 0 pwr-gnd.sym
{
T 48840 44960 5 10 0 0 0 0 1
value=GND
T 48830 45350 5 10 0 0 0 0 1
device=SYMBOL
}
N 48550 44500 48550 44650 4
C 49850 47350 1 90 0 cap.sym
{
T 48150 47550 5 10 0 0 90 0 1
device=CAPACITOR
T 49900 47850 5 10 1 1 0 0 1
refdes=C2
T 48950 47550 5 10 0 0 90 0 1
symversion=0.1
T 49900 47650 5 10 1 1 0 0 1
value=1uF
T 48350 47550 5 10 0 0 90 0 1
footprint=1206.fp
}
N 48550 47050 51150 47050 4
{
T 48650 47100 5 10 1 1 0 0 1
netname=NC
}
N 45000 48650 50450 48650 4
C 45300 46150 1 0 0 cap.sym
{
T 45500 47850 5 10 0 0 0 0 1
device=CAPACITOR
T 45650 46650 5 10 1 1 0 0 1
refdes=C1
T 45500 47050 5 10 0 0 0 0 1
symversion=0.1
T 45550 45950 5 10 1 1 0 0 1
value=1uF
T 45500 47650 5 10 0 0 0 0 1
footprint=1206.fp
}
N 46000 46350 46350 46350 4
N 45500 46350 45000 46350 4
{
T 45050 46400 5 10 1 1 0 0 1
netname=IN
}
N 45000 46350 45000 46150 4
C 44700 47250 1 0 0 spice-vdc.sym
{
T 45400 47900 5 10 1 1 0 0 1
refdes=V2
T 45400 48100 5 10 0 0 0 0 1
device=spice
T 45400 48300 5 10 0 0 0 0 1
footprint=none
T 45400 47700 5 10 1 1 0 0 1
value=DC 15V
}
C 45000 46950 1 0 0 pwr-gnd.sym
{
T 45290 47610 5 10 0 0 0 0 1
value=GND
T 45280 48000 5 10 0 0 0 0 1
device=SYMBOL
}
N 45000 47150 45000 47250 4
N 45000 48450 45000 48650 4
N 48550 48250 48550 48650 4
C 49500 44600 1 90 0 cap.sym
{
T 47800 44800 5 10 0 0 90 0 1
device=CAPACITOR
T 49600 45100 5 10 1 1 0 0 1
refdes=C3
T 48600 44800 5 10 0 0 90 0 1
symversion=0.1
T 49600 44900 5 10 1 1 0 0 1
value=100k
T 48000 44800 5 10 0 0 90 0 1
footprint=1206.fp
}
C 49300 44300 1 0 0 pwr-gnd.sym
{
T 49590 44960 5 10 0 0 0 0 1
value=GND
T 49580 45350 5 10 0 0 0 0 1
device=SYMBOL
}
N 49300 44500 49300 44800 4
N 47550 45550 47550 46350 4
N 47550 48250 47550 48650 4
N 48550 45950 48550 45550 4
N 48550 45800 49300 45800 4
{
T 48600 45850 5 10 1 1 0 0 1
netname=NE
}
N 49300 45800 49300 45300 4
C 51150 46950 1 0 0 port-out.sym
{
T 51400 47050 5 10 1 1 0 1 1
net=OUT:1
T 51350 47700 5 10 0 0 0 0 1
device=none
T 51400 46850 5 10 0 1 0 1 1
value=OUTPUT
}
N 49650 48050 49650 48650 4
N 49650 47050 49650 47550 4
N 50450 48350 50450 48650 4
N 50450 47250 50450 47050 4
C 52900 44800 1 0 0 spice-directive.sym
{
T 52900 45500 5 10 0 0 0 0 1
device=directive
T 53000 45200 5 10 1 1 0 0 1
refdes=A1
T 52600 44900 5 10 1 1 0 0 1
value=.AC DEC 10000 17400Hz 18200Hz
}
C 50450 48350 1 270 0 inductor.sym
{
T 50650 47850 5 10 1 1 0 0 1
refdes=L1
T 51800 48200 5 10 0 0 270 0 1
device=INDUCTOR
T 51300 48200 5 10 0 0 270 0 1
footprint=acy500.fp
T 50650 47600 5 10 1 1 0 0 1
value=80uH
}
C 47950 45950 1 0 0 npn.sym
{
T 48050 47700 5 10 0 0 0 0 1
device=NPN
T 48050 46550 5 8 1 1 0 0 1
refdes=Q1
T 48550 46350 5 8 1 1 0 0 1
value=BC546
}
