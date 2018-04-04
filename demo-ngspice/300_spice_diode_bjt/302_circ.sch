v 20130925 2
C 40000 40000 0 0 0 title-bordered-A3.sym
C 42150 44150 1 0 0 pwr-gnd.sym
{
T 42440 44810 5 10 0 0 0 0 1
value=GND
T 42430 45200 5 10 0 0 0 0 1
device=SYMBOL
}
N 42150 44350 42150 44500 4
T 49300 40900 9 14 1 0 0 0 2
Example 302
Two-stage BJT amplifier with shunt-series feedback 
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / A
T 53300 40300 9 8 1 0 0 0 1
090919 PF
C 41850 44500 1 0 0 spice-vsin.sym
{
T 42550 45050 5 10 1 1 0 0 1
refdes=V1
T 42550 45350 5 10 0 0 0 0 1
device=spice
T 42550 45550 5 10 0 0 0 0 1
footprint=none
T 42300 44600 5 10 1 1 0 0 1
value=DC 0 AC 10mV
}
C 43800 46000 1 180 0 res.sym
{
T 43650 45400 5 10 0 0 180 0 1
device=RESISTOR
T 43250 46050 5 10 1 1 0 0 1
refdes=RS
T 43150 45600 5 10 1 1 0 0 1
value=150
T 43650 45000 5 10 0 0 180 0 1
footprint=1206.fp
}
C 45650 44400 1 0 0 pwr-gnd.sym
{
T 45940 45060 5 10 0 0 0 0 1
value=GND
T 45930 45450 5 10 0 0 0 0 1
device=SYMBOL
}
C 46750 44650 1 90 0 res.sym
{
T 46150 44800 5 10 0 0 90 0 1
device=RESISTOR
T 46800 45100 5 10 1 1 0 0 1
refdes=Re1
T 46800 44900 5 10 1 1 0 0 1
value=3.6k
T 45750 44800 5 10 0 0 90 0 1
footprint=1206.fp
}
C 46750 46900 1 90 0 res.sym
{
T 46150 47050 5 10 0 0 90 0 1
device=RESISTOR
T 46900 47350 5 10 1 1 0 0 1
refdes=Rc1
T 46900 47150 5 10 1 1 0 0 1
value=12k
T 45750 47050 5 10 0 0 90 0 1
footprint=1206.fp
}
C 45750 46900 1 90 0 res.sym
{
T 45150 47050 5 10 0 0 90 0 1
device=RESISTOR
T 45050 47350 5 10 1 1 0 0 1
refdes=R1
T 45050 47150 5 10 1 1 0 0 1
value=200k
T 44750 47050 5 10 0 0 90 0 1
footprint=1206.fp
}
C 45750 44650 1 90 0 res.sym
{
T 45150 44800 5 10 0 0 90 0 1
device=RESISTOR
T 45850 45100 5 10 1 1 0 0 1
refdes=R2
T 45850 44900 5 10 1 1 0 0 1
value=50k
T 44750 44800 5 10 0 0 90 0 1
footprint=1206.fp
}
N 46650 46650 46650 46900 4
N 45650 46250 46050 46250 4
{
T 45700 46300 5 6 1 1 0 0 1
netname=NB1
}
N 45650 45550 45650 46900 4
N 45650 44650 45650 44600 4
C 46650 44400 1 0 0 pwr-gnd.sym
{
T 46940 45060 5 10 0 0 0 0 1
value=GND
T 46930 45450 5 10 0 0 0 0 1
device=SYMBOL
}
N 46650 44600 46650 44650 4
C 47300 46600 1 0 0 cap.sym
{
T 47500 48300 5 10 0 0 0 0 1
device=CAPACITOR
T 47650 47100 5 10 1 1 0 0 1
refdes=C2
T 47500 47500 5 10 0 0 0 0 1
symversion=0.1
T 47650 46400 5 10 1 1 0 0 1
value=10uF
T 47500 48100 5 10 0 0 0 0 1
footprint=1206.fp
}
N 47500 46800 46650 46800 4
{
T 46400 46750 5 6 1 1 0 0 1
netname=NC1
}
C 44200 45700 1 0 0 cap.sym
{
T 44400 47400 5 10 0 0 0 0 1
device=CAPACITOR
T 44550 46200 5 10 1 1 0 0 1
refdes=C1
T 44400 46600 5 10 0 0 0 0 1
symversion=0.1
T 44450 45500 5 10 1 1 0 0 1
value=1uF
T 44400 47200 5 10 0 0 0 0 1
footprint=1206.fp
}
N 42150 45900 42150 45700 4
C 51950 45550 1 90 0 res.sym
{
T 51350 45700 5 10 0 0 90 0 1
device=RESISTOR
T 52100 46000 5 10 1 1 0 0 1
refdes=RL
T 52100 45800 5 10 1 1 0 0 1
value=10k
T 50950 45700 5 10 0 0 90 0 1
footprint=1206.fp
}
C 51850 45200 1 0 0 pwr-gnd.sym
{
T 52140 45860 5 10 0 0 0 0 1
value=GND
T 52130 46250 5 10 0 0 0 0 1
device=SYMBOL
}
N 51850 46450 51850 46750 4
N 51850 45550 51850 45400 4
C 43700 46750 1 0 0 spice-vdc.sym
{
T 43350 47450 5 10 1 1 0 0 1
refdes=V2
T 44400 47600 5 10 0 0 0 0 1
device=spice
T 44400 47800 5 10 0 0 0 0 1
footprint=none
T 42950 47200 5 10 1 1 0 0 1
value=DC 15V
}
C 44000 46500 1 0 0 pwr-gnd.sym
{
T 44290 47160 5 10 0 0 0 0 1
value=GND
T 44280 47550 5 10 0 0 0 0 1
device=SYMBOL
}
N 44000 46700 44000 46750 4
N 46650 47800 46650 48000 4
C 47600 44650 1 90 0 cap.sym
{
T 45900 44850 5 10 0 0 90 0 1
device=CAPACITOR
T 47700 45150 5 10 1 1 0 0 1
refdes=CE1
T 46700 44850 5 10 0 0 90 0 1
symversion=0.1
T 47700 44950 5 10 1 1 0 0 1
value=15uF
T 46100 44850 5 10 0 0 90 0 1
footprint=1206.fp
}
C 47400 44400 1 0 0 pwr-gnd.sym
{
T 47690 45060 5 10 0 0 0 0 1
value=GND
T 47680 45450 5 10 0 0 0 0 1
device=SYMBOL
}
N 45650 47800 45650 48000 4
N 46650 45850 46650 45550 4
N 46650 45700 47400 45700 4
{
T 46400 45650 5 6 1 1 0 0 1
netname=NE1
}
N 47400 45700 47400 45350 4
C 49150 44400 1 0 0 pwr-gnd.sym
{
T 49440 45060 5 10 0 0 0 0 1
value=GND
T 49430 45450 5 10 0 0 0 0 1
device=SYMBOL
}
C 50250 44700 1 90 0 res.sym
{
T 49650 44850 5 10 0 0 90 0 1
device=RESISTOR
T 50400 45150 5 10 1 1 0 0 1
refdes=Re2
T 50400 44950 5 10 1 1 0 0 1
value=3.6k
T 49250 44850 5 10 0 0 90 0 1
footprint=1206.fp
}
C 50250 46900 1 90 0 res.sym
{
T 49650 47050 5 10 0 0 90 0 1
device=RESISTOR
T 50400 47350 5 10 1 1 0 0 1
refdes=Rc2
T 50400 47150 5 10 1 1 0 0 1
value=6.8k
T 49250 47050 5 10 0 0 90 0 1
footprint=1206.fp
}
C 49250 46900 1 90 0 res.sym
{
T 48650 47050 5 10 0 0 90 0 1
device=RESISTOR
T 48600 47350 5 10 1 1 0 0 1
refdes=R3
T 48600 47150 5 10 1 1 0 0 1
value=120k
T 48250 47050 5 10 0 0 90 0 1
footprint=1206.fp
}
C 49250 44700 1 90 0 res.sym
{
T 48650 44850 5 10 0 0 90 0 1
device=RESISTOR
T 48700 45150 5 10 1 1 0 0 1
refdes=R4
T 48700 44950 5 10 1 1 0 0 1
value=30k
T 48250 44850 5 10 0 0 90 0 1
footprint=1206.fp
}
N 50150 46550 50150 46900 4
{
T 49850 46700 5 6 1 1 0 0 1
netname=NC2
}
N 49150 45600 49150 46900 4
N 49150 44700 49150 44600 4
C 50150 44400 1 0 0 pwr-gnd.sym
{
T 50440 45060 5 10 0 0 0 0 1
value=GND
T 50430 45450 5 10 0 0 0 0 1
device=SYMBOL
}
N 50150 44600 50150 44700 4
N 50150 47800 50150 48000 4
N 49150 47800 49150 48000 4
N 50150 45750 50150 45600 4
{
T 50250 45650 5 6 1 1 0 0 1
netname=NE2
}
N 48000 46800 48600 46800 4
N 49150 46150 49550 46150 4
{
T 49200 46200 5 6 1 1 0 0 1
netname=NB2
}
C 45700 43750 1 0 0 cap.sym
{
T 45900 45450 5 10 0 0 0 0 1
device=CAPACITOR
T 46050 44200 5 10 1 1 0 0 1
refdes=Cf
T 45900 44650 5 10 0 0 0 0 1
symversion=0.1
T 45950 43550 5 10 1 1 0 0 1
value=10uF
T 45900 45250 5 10 0 0 0 0 1
footprint=1206.fp
}
C 48150 44050 1 180 0 res.sym
{
T 48000 43450 5 10 0 0 180 0 1
device=RESISTOR
T 47600 44100 5 10 1 1 0 0 1
refdes=Rf
T 47500 43650 5 10 1 1 0 0 1
value=25k
T 48000 43050 5 10 0 0 180 0 1
footprint=1206.fp
}
C 50650 46550 1 0 0 cap.sym
{
T 50850 48250 5 10 0 0 0 0 1
device=CAPACITOR
T 51000 47050 5 10 1 1 0 0 1
refdes=C3
T 50850 47450 5 10 0 0 0 0 1
symversion=0.1
T 50900 46350 5 10 1 1 0 0 1
value=10uF
T 50850 48050 5 10 0 0 0 0 1
footprint=1206.fp
}
N 44400 45900 43800 45900 4
N 42150 45900 42900 45900 4
{
T 42200 45950 5 10 1 1 0 0 1
netname=IN
}
N 45900 43950 44000 43950 4
N 44000 43950 44000 45900 4
N 46400 43950 47250 43950 4
N 50150 45700 49650 45700 4
N 49650 45700 49650 43950 4
N 49650 43950 48150 43950 4
N 44000 48000 50150 48000 4
N 50850 46750 50150 46750 4
N 52150 46750 51350 46750 4
N 44000 48000 44000 47950 4
N 49150 46150 48600 46150 4
N 48600 46150 48600 46800 4
N 44900 45900 45650 45900 4
C 44050 42250 1 0 0 spice-directive.sym
{
T 44050 42950 5 10 0 0 0 0 1
device=directive
T 44150 42650 5 10 1 1 0 0 1
refdes=A1
T 44150 42350 5 10 1 1 0 0 1
value=.AC DEC 100 10 100MEG
}
C 52150 46650 1 0 0 port-out.sym
{
T 52400 46750 5 10 1 1 0 1 1
net=OUT:1
T 52350 47400 5 10 0 0 0 0 1
device=none
T 52400 46550 5 10 0 1 0 1 1
value=OUTPUT
}
N 47400 44850 47400 44600 4
C 46050 45850 1 0 0 npn.sym
{
T 46150 47600 5 10 0 0 0 0 1
device=NPN
T 46150 46450 5 8 1 1 0 0 1
refdes=Q1
T 46650 46250 5 8 1 1 0 0 1
value=BC546
}
C 49550 45750 1 0 0 npn.sym
{
T 49650 47500 5 10 0 0 0 0 1
device=NPN
T 49650 46350 5 8 1 1 0 0 1
refdes=Q2
T 50150 46150 5 8 1 1 0 0 1
value=BC546
}
