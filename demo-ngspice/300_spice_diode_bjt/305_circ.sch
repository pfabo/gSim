v 20130925 2
C 40000 40000 0 0 0 title-bordered-A3.sym
T 49300 40900 9 14 1 0 0 0 2
Example 00305
Low frequency oscillator
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / A
T 53300 40300 9 8 1 0 0 0 1
090919 PF
C 50950 46950 1 90 0 res.sym
{
T 50350 47100 5 10 0 0 90 0 1
device=RESISTOR
T 51050 47400 5 10 1 1 0 0 1
refdes=Rc1
T 51050 47200 5 10 1 1 0 0 1
value=640k
T 49950 47100 5 10 0 0 90 0 1
footprint=1206.fp
}
C 52300 47350 1 0 0 spice-vdc.sym
{
T 51950 48050 5 10 1 1 0 0 1
refdes=V1
T 53000 48200 5 10 0 0 0 0 1
device=spice
T 53000 48400 5 10 0 0 0 0 1
footprint=none
T 51550 47800 5 10 1 1 0 0 1
value=DC 12V
}
C 52600 47000 1 0 0 pwr-gnd.sym
{
T 52890 47660 5 10 0 0 0 0 1
value=GND
T 52880 48050 5 10 0 0 0 0 1
device=SYMBOL
}
N 52600 47200 52600 47350 4
C 49950 44700 1 90 0 cap.sym
{
T 48250 44900 5 10 0 0 90 0 1
device=CAPACITOR
T 50000 45200 5 10 1 1 0 0 1
refdes=C3
T 49050 44900 5 10 0 0 90 0 1
symversion=0.1
T 50000 45000 5 10 1 1 0 0 1
value=30nF
T 48450 44900 5 10 0 0 90 0 1
footprint=1206.fp
}
C 52050 44650 1 0 0 spice-directive.sym
{
T 52050 45350 5 10 0 0 0 0 1
device=directive
T 52150 45050 5 10 1 1 0 0 1
refdes=A2
T 51950 44650 5 10 1 1 0 0 1
value=.TRAN 0.01ms 60ms UIC
}
C 48600 45650 1 0 0 res.sym
{
T 48750 46250 5 10 0 0 0 0 1
device=RESISTOR
T 48900 45900 5 10 1 1 0 0 1
refdes=R3
T 48900 45450 5 10 1 1 0 0 1
value=20k
T 48750 46650 5 10 0 0 0 0 1
footprint=1206.fp
}
C 50850 44350 1 0 0 pwr-gnd.sym
{
T 51140 45010 5 10 0 0 0 0 1
value=GND
T 51130 45400 5 10 0 0 0 0 1
device=SYMBOL
}
N 50850 44550 50850 45350 4
N 50850 46150 50850 46950 4
N 50850 48600 50850 47850 4
N 52600 48600 50850 48600 4
N 52600 48600 52600 48550 4
C 49750 44350 1 0 0 pwr-gnd.sym
{
T 50040 45010 5 10 0 0 0 0 1
value=GND
T 50030 45400 5 10 0 0 0 0 1
device=SYMBOL
}
C 48600 44700 1 90 0 cap.sym
{
T 46900 44900 5 10 0 0 90 0 1
device=CAPACITOR
T 48650 45200 5 10 1 1 0 0 1
refdes=C2
T 47700 44900 5 10 0 0 90 0 1
symversion=0.1
T 48650 45000 5 10 1 1 0 0 1
value=30nF
T 47100 44900 5 10 0 0 90 0 1
footprint=1206.fp
}
C 47250 45650 1 0 0 res.sym
{
T 47400 46250 5 10 0 0 0 0 1
device=RESISTOR
T 47550 45900 5 10 1 1 0 0 1
refdes=R2
T 47550 45450 5 10 1 1 0 0 1
value=20k
T 47400 46650 5 10 0 0 0 0 1
footprint=1206.fp
}
C 48400 44350 1 0 0 pwr-gnd.sym
{
T 48690 45010 5 10 0 0 0 0 1
value=GND
T 48680 45400 5 10 0 0 0 0 1
device=SYMBOL
}
C 47250 44700 1 90 0 cap.sym
{
T 45550 44900 5 10 0 0 90 0 1
device=CAPACITOR
T 47300 45200 5 10 1 1 0 0 1
refdes=C1
T 46350 44900 5 10 0 0 90 0 1
symversion=0.1
T 47300 45000 5 10 1 1 0 0 1
value=30nF
T 45750 44900 5 10 0 0 90 0 1
footprint=1206.fp
}
C 45900 45650 1 0 0 res.sym
{
T 46050 46250 5 10 0 0 0 0 1
device=RESISTOR
T 46200 45900 5 10 1 1 0 0 1
refdes=R1
T 46200 45450 5 10 1 1 0 0 1
value=20k
T 46050 46650 5 10 0 0 0 0 1
footprint=1206.fp
}
C 47050 44350 1 0 0 pwr-gnd.sym
{
T 47340 45010 5 10 0 0 0 0 1
value=GND
T 47330 45400 5 10 0 0 0 0 1
device=SYMBOL
}
N 50250 45750 49500 45750 4
N 49750 45400 49750 45750 4
N 49750 44900 49750 44550 4
N 48600 45750 48150 45750 4
{
T 48300 45850 5 10 1 1 0 0 1
netname=VC
}
N 48400 45400 48400 45750 4
N 48400 44900 48400 44550 4
N 46800 45750 47250 45750 4
N 47050 45400 47050 45750 4
N 47050 44900 47050 44550 4
N 50850 46500 45800 46500 4
N 45800 46500 45800 45750 4
N 45800 45750 45900 45750 4
C 51750 46400 1 0 0 port-out.sym
{
T 52000 46500 5 10 1 1 0 1 1
net=OUT:1
T 51950 47150 5 10 0 0 0 0 1
device=none
T 52000 46300 5 10 0 1 0 1 1
value=OUTPUT
}
N 51750 46500 50850 46500 4
C 50250 45350 1 0 0 npn.sym
{
T 50350 47100 5 10 0 0 0 0 1
device=NPN
T 50350 45950 5 8 1 1 0 0 1
refdes=Q1
T 50850 45700 5 8 1 1 0 0 1
value=BC546
}
