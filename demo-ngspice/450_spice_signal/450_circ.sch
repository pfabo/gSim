v 20130925 2
C 40000 40000 0 0 0 title-bordered-A3.sym
C 46500 45950 1 0 0 pwr-gnd.sym
{
T 46790 46610 5 10 0 0 0 0 1
value=GND
T 46780 47000 5 10 0 0 0 0 1
device=SYMBOL
}
N 46500 46150 46500 46250 4
N 46500 47450 46500 47550 4
N 46500 47550 46950 47550 4
T 49300 40900 9 14 1 0 0 0 2
Example 00450
AM Modulation and detection
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / A
T 53300 40300 9 8 1 0 0 0 1
PF
C 46200 46250 1 0 0 spice-vsin.sym
{
T 46850 46850 5 10 1 1 0 0 1
refdes=V3
T 46900 47100 5 10 0 0 0 0 1
device=spice
T 46900 47300 5 10 0 0 0 0 1
footprint=none
T 46000 45650 5 10 1 1 0 0 1
value=DC 0V SIN (0 1 10k)
}
T 49450 40600 9 8 1 0 0 0 1
circuit_0010.sch
C 47900 46250 1 0 0 spice-directive.sym
{
T 47900 46950 5 10 0 0 0 0 1
device=directive
T 48000 46650 5 10 1 1 0 0 1
refdes=A5
T 48000 46350 5 10 1 1 0 0 1
value=.TRAN 1uS 20mS
}
N 47650 47750 48100 47750 4
C 44000 45950 1 0 0 pwr-gnd.sym
{
T 44290 46610 5 10 0 0 0 0 1
value=GND
T 44280 47000 5 10 0 0 0 0 1
device=SYMBOL
}
N 44000 46150 44000 46250 4
C 43700 46250 1 0 0 spice-vsin.sym
{
T 44350 46850 5 10 1 1 0 0 1
refdes=V1
T 44400 47100 5 10 0 0 0 0 1
device=spice
T 44400 47300 5 10 0 0 0 0 1
footprint=none
T 43000 45650 5 10 1 1 0 0 1
value=DC 0V SIN (0 0.5 250)
}
C 46950 47550 1 0 0 mult_2.sym
{
T 47175 48950 5 8 0 0 0 0 1
device=SPICE
T 47300 47950 5 10 1 1 0 0 1
refdes=A3
T 47150 49950 5 8 0 0 0 0 1
value=MULT_2
T 46945 48000 5 6 1 1 0 0 1
in_gain_1=1.0
T 46945 47600 5 6 1 1 0 0 1
in_gain_2=1.0
T 47545 47800 5 6 1 1 0 0 1
out_gain=1.0
}
C 44300 47750 1 0 0 gain.sym
{
T 44525 49300 5 8 0 0 0 0 1
device=SPICE
T 44800 48450 5 10 1 1 0 0 1
refdes=A1
T 44500 50350 5 8 0 0 0 0 1
value=GAIN
T 44595 48150 5 10 1 1 0 1 1
gain=0.5
}
C 46050 47750 1 0 0 summer_2.sym
{
T 46275 49150 5 8 0 0 0 0 1
device=SPICE
T 46400 48150 5 10 1 1 0 0 1
refdes=A2
T 46250 50150 5 8 0 0 0 0 1
value=SUMMER_2
T 46045 48200 5 6 1 1 0 0 1
in_gain_1=1.0
T 46045 47800 5 6 1 1 0 0 1
in_gain_2=1.0
T 46645 48000 5 6 1 1 0 0 1
out_gain=1.0
}
C 44950 46250 1 0 0 spice-vdc.sym
{
T 45600 46850 5 10 1 1 0 0 1
refdes=V2
T 45650 47300 5 10 0 0 0 0 1
device=SPICE
T 45000 45650 5 10 1 1 0 0 1
value=DC 0.5V
}
C 45250 45950 1 0 0 pwr-gnd.sym
{
T 45540 46610 5 10 0 0 0 0 1
value=GND
T 45530 47000 5 10 0 0 0 0 1
device=SYMBOL
}
N 46750 47950 46950 47950 4
N 46050 47750 45250 47750 4
N 45250 47750 45250 47450 4
N 46050 48150 45300 48150 4
{
T 45550 48200 5 10 1 1 0 0 1
netname=IN
}
N 44300 48150 44000 48150 4
N 44000 48150 44000 47450 4
N 45250 46250 45250 46150 4
C 48100 47650 1 0 0 port.sym
{
T 48350 47750 5 10 1 1 0 1 1
net=AM:1
T 48300 48250 5 10 0 0 0 0 1
device=none
T 48450 47500 5 10 0 1 0 1 1
value=IO
}
C 44100 44350 1 0 1 port.sym
{
T 43850 44450 5 10 1 1 0 7 1
net=AM:1
T 43900 44950 5 10 0 0 0 6 1
device=none
T 43750 44200 5 10 0 1 0 7 1
value=IO
}
C 45750 43300 1 90 0 cap.sym
{
T 45050 43500 5 10 0 0 90 0 1
device=CAPACITOR
T 45850 43800 5 10 1 1 0 0 1
refdes=C1
T 44850 43500 5 10 0 0 90 0 1
symversion=0.1
T 45850 43600 5 10 1 1 0 0 1
value=100nF
T 44250 43500 5 10 0 0 90 0 1
footprint=NONE
}
C 45550 43000 1 0 0 pwr-gnd.sym
{
T 45840 43660 5 10 0 0 0 0 1
value=GND
T 45830 44050 5 10 0 0 0 0 1
device=SYMBOL
}
C 47400 44350 1 0 0 port.sym
{
T 47650 44450 5 10 1 1 0 1 1
net=S2:1
T 47600 44950 5 10 0 0 0 0 1
device=none
T 47750 44200 5 10 0 1 0 1 1
value=IO
}
N 44100 44450 44500 44450 4
N 45200 44450 47400 44450 4
N 45550 44000 45550 44450 4
N 45550 43500 45550 43200 4
C 44500 44350 1 0 0 diode.sym
{
T 44550 45600 5 10 0 0 0 0 1
device=DIODE
T 44700 44650 5 10 1 1 0 0 1
refdes=D1
T 44700 44850 5 10 0 1 0 0 1
value=DIODE
}
C 46600 43250 1 90 0 res.sym
{
T 46000 43350 5 10 0 0 90 0 1
device=RESISTOR
T 46700 43750 5 10 1 1 0 0 1
refdes=R1
T 46650 43550 5 10 1 1 0 0 1
value=10k
}
C 46500 42950 1 0 0 pwr-gnd.sym
{
T 46790 43610 5 10 0 0 0 0 1
value=GND
T 46780 44000 5 10 0 0 0 0 1
device=SYMBOL
}
N 46500 43150 46500 43250 4
N 46500 44150 46500 44450 4
T 46600 48500 2 10 1 0 0 0 1
AM Modulator
T 43450 43950 2 10 1 0 0 0 1
AM Envelope Detector
T 46300 45400 2 10 1 0 0 0 1
Carrier
T 43500 45400 2 10 1 0 0 0 1
Modulation
T 44050 48700 2 10 1 0 0 0 1
Modulation index
