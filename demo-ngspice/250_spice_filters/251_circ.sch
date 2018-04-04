v 20130925 2
C 40000 40000 0 0 0 title-bordered-A3.sym
C 43950 43100 1 0 0 spice-directive-1.sym
{
T 44050 43400 5 10 0 1 0 0 1
device=directive
T 44050 43500 5 10 1 1 0 0 1
refdes=A1
T 43950 43200 5 10 1 1 0 0 1
value=.AC DEC 1000 1Hz 10kHz
}
T 49300 40900 9 14 1 0 0 0 2
Example 00810
6th order Chebyshev Low-pass filter
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / A
T 53300 40300 9 8 1 0 0 0 1
090919 PF
T 49450 40600 9 8 1 0 0 0 1
circuit_080.sch
C 41800 45200 1 0 0 pwr-gnd.sym
{
T 42090 45860 5 10 0 0 0 0 1
value=GND
T 42080 46250 5 10 0 0 0 0 1
device=SYMBOL
}
N 41800 47100 42050 47100 4
{
T 41500 46950 5 10 1 1 0 0 1
netname=IN
}
N 41800 47100 41800 46800 4
N 41800 45400 41800 45600 4
C 41500 45600 1 0 0 spice-vac.sym
{
T 42200 46250 5 10 1 1 0 0 1
refdes=V1
T 42200 46450 5 10 0 0 0 0 1
device=spice
T 42200 46650 5 10 0 0 0 0 1
footprint=none
T 42200 46050 5 10 1 1 0 0 1
value=dc 0 ac 1
}
C 43250 47000 1 0 0 res.sym
{
T 43400 47600 5 10 0 0 0 0 1
device=RESISTOR
T 43650 47250 5 10 1 1 0 0 1
refdes=R2
T 43600 46800 5 10 1 1 0 0 1
value=10k
T 43400 48000 5 10 0 0 0 0 1
footprint=1206.fp
}
C 42050 47000 1 0 0 res.sym
{
T 42200 47600 5 10 0 0 0 0 1
device=RESISTOR
T 42450 47250 5 10 1 1 0 0 1
refdes=R1
T 42400 46800 5 10 1 1 0 0 1
value=10k
T 42200 48000 5 10 0 0 0 0 1
footprint=1206.fp
}
N 45550 47300 45800 47300 4
N 43250 47100 42950 47100 4
N 45650 47300 45650 48350 4
N 44550 47500 44450 47500 4
N 44450 47500 44450 48350 4
N 44150 47100 44550 47100 4
C 53200 47600 1 0 0 port-out.sym
{
T 53450 47700 5 10 1 1 0 1 1
net=OUT:1
T 53400 48350 5 10 0 0 0 0 1
device=none
T 53450 47500 5 10 0 1 0 1 1
value=OUTPUT
}
C 43450 48150 1 0 0 cap.sym
{
T 43650 49850 5 10 0 0 0 0 1
device=CAPACITOR
T 44050 48700 5 10 1 1 0 0 1
refdes=C1
T 43650 49050 5 10 0 0 0 0 1
symversion=0.1
T 44050 48500 5 10 1 1 0 0 1
value=68.6nF
T 43650 49650 5 10 0 0 0 0 1
footprint=1206.fp
}
C 44650 46050 1 90 0 cap.sym
{
T 42950 46250 5 10 0 0 90 0 1
device=CAPACITOR
T 44700 46500 5 10 1 1 0 0 1
refdes=C2
T 43750 46250 5 10 0 0 90 0 1
symversion=0.1
T 44700 46300 5 10 1 1 0 0 1
value=29.62nF
T 43150 46250 5 10 0 0 90 0 1
footprint=1206.fp
}
C 44450 45750 1 0 0 pwr-gnd.sym
{
T 44740 46410 5 10 0 0 0 0 1
value=GND
T 44730 46800 5 10 0 0 0 0 1
device=SYMBOL
}
N 44150 48350 45650 48350 4
N 44450 46750 44450 47100 4
N 44450 45950 44450 46250 4
N 43650 48350 43100 48350 4
N 43100 48350 43100 47100 4
C 47000 47200 1 0 0 res.sym
{
T 47150 47800 5 10 0 0 0 0 1
device=RESISTOR
T 47400 47450 5 10 1 1 0 0 1
refdes=R4
T 47350 47000 5 10 1 1 0 0 1
value=10k
T 47150 48200 5 10 0 0 0 0 1
footprint=1206.fp
}
C 45800 47200 1 0 0 res.sym
{
T 45950 47800 5 10 0 0 0 0 1
device=RESISTOR
T 46200 47450 5 10 1 1 0 0 1
refdes=R3
T 46150 47000 5 10 1 1 0 0 1
value=10k
T 45950 48200 5 10 0 0 0 0 1
footprint=1206.fp
}
N 49300 47500 49450 47500 4
N 47000 47300 46700 47300 4
N 49400 47500 49400 48550 4
N 48300 47700 48200 47700 4
N 48200 47700 48200 48550 4
N 47900 47300 48300 47300 4
C 47200 48350 1 0 0 cap.sym
{
T 47400 50050 5 10 0 0 0 0 1
device=CAPACITOR
T 47800 48900 5 10 1 1 0 0 1
refdes=C3
T 47400 49250 5 10 0 0 0 0 1
symversion=0.1
T 47800 48700 5 10 1 1 0 0 1
value=93.7nF
T 47400 49850 5 10 0 0 0 0 1
footprint=1206.fp
}
C 48400 46250 1 90 0 cap.sym
{
T 46700 46450 5 10 0 0 90 0 1
device=CAPACITOR
T 48450 46700 5 10 1 1 0 0 1
refdes=C4
T 47500 46450 5 10 0 0 90 0 1
symversion=0.1
T 48450 46500 5 10 1 1 0 0 1
value=4.85nF
T 46900 46450 5 10 0 0 90 0 1
footprint=1206.fp
}
C 48200 45950 1 0 0 pwr-gnd.sym
{
T 48490 46610 5 10 0 0 0 0 1
value=GND
T 48480 47000 5 10 0 0 0 0 1
device=SYMBOL
}
N 47900 48550 49400 48550 4
N 48200 46950 48200 47300 4
N 48200 46150 48200 46450 4
N 47400 48550 46850 48550 4
N 46850 48550 46850 47300 4
C 50650 47400 1 0 0 res.sym
{
T 50800 48000 5 10 0 0 0 0 1
device=RESISTOR
T 51050 47650 5 10 1 1 0 0 1
refdes=R6
T 51000 47200 5 10 1 1 0 0 1
value=10k
T 50800 48400 5 10 0 0 0 0 1
footprint=1206.fp
}
C 49450 47400 1 0 0 res.sym
{
T 49600 48000 5 10 0 0 0 0 1
device=RESISTOR
T 49850 47650 5 10 1 1 0 0 1
refdes=R5
T 49800 47200 5 10 1 1 0 0 1
value=10k
T 49600 48400 5 10 0 0 0 0 1
footprint=1206.fp
}
N 52950 47700 53200 47700 4
N 50650 47500 50350 47500 4
N 53050 47700 53050 48750 4
N 51950 47900 51850 47900 4
N 51850 47900 51850 48750 4
N 51550 47500 51950 47500 4
C 50850 48550 1 0 0 cap.sym
{
T 51050 50250 5 10 0 0 0 0 1
device=CAPACITOR
T 51450 49100 5 10 1 1 0 0 1
refdes=C5
T 51050 49450 5 10 0 0 0 0 1
symversion=0.1
T 51450 48900 5 10 1 1 0 0 1
value=256nF
T 51050 50050 5 10 0 0 0 0 1
footprint=1206.fp
}
C 52050 46450 1 90 0 cap.sym
{
T 50350 46650 5 10 0 0 90 0 1
device=CAPACITOR
T 52100 46900 5 10 1 1 0 0 1
refdes=C6
T 51150 46650 5 10 0 0 90 0 1
symversion=0.1
T 52100 46700 5 10 1 1 0 0 1
value=1nF
T 50550 46650 5 10 0 0 90 0 1
footprint=1206.fp
}
C 51850 46150 1 0 0 pwr-gnd.sym
{
T 52140 46810 5 10 0 0 0 0 1
value=GND
T 52130 47200 5 10 0 0 0 0 1
device=SYMBOL
}
N 51550 48750 53050 48750 4
N 51850 47150 51850 47500 4
N 51850 46350 51850 46650 4
N 51050 48750 50500 48750 4
N 50500 48750 50500 47500 4
C 44550 47700 1 180 1 opamp.sym
{
T 44650 45050 5 10 0 0 180 6 1
device=OPAMP
T 45150 47050 5 10 1 1 180 6 1
refdes=X1
T 44645 44625 5 10 0 0 180 6 1
value=OPAMP
}
C 48300 47900 1 180 1 opamp.sym
{
T 48400 45250 5 10 0 0 180 6 1
device=OPAMP
T 48900 47250 5 10 1 1 180 6 1
refdes=X2
T 48395 44825 5 10 0 0 180 6 1
value=OPAMP
}
C 51950 48100 1 180 1 opamp.sym
{
T 52050 45450 5 10 0 0 180 6 1
device=OPAMP
T 52550 47450 5 10 1 1 180 6 1
refdes=X3
T 52045 45025 5 10 0 0 180 6 1
value=OPAMP
}
T 43300 44600 9 14 1 0 0 0 2
6th order Chebyshev Low-pass filter
1kHz band stop frequency, 1dB ripple