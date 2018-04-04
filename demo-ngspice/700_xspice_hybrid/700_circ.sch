v 20130925 2
C 40000 40000 0 0 0 title-bordered-A3.sym
C 44550 44900 1 0 0 pwr-gnd.sym
{
T 44840 45560 5 10 0 0 0 0 1
value=GND
T 44830 45950 5 10 0 0 0 0 1
device=SYMBOL
}
C 55700 46400 1 0 1 port-in.sym
{
T 55650 46500 5 10 1 1 0 7 1
net=OUT:1
T 55600 47100 5 10 0 0 0 6 1
device=none
T 54900 46300 5 10 0 1 0 1 1
value=INPUT
}
N 44550 45100 44550 45500 4
T 49300 40900 9 14 1 0 0 0 2
Example 700
TIMER_555 - Macro Model
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / A
T 53300 40300 9 8 1 0 0 0 1
100104 PF
C 44350 46200 1 270 0 cap.sym
{
T 46050 46000 5 10 0 0 270 0 1
device=CAPACITOR
T 44000 45800 5 10 1 1 0 0 1
refdes=C1
T 45250 46000 5 10 0 0 270 0 1
symversion=0.1
T 44000 45500 5 10 1 1 0 0 1
value=15nF
T 45850 46000 5 10 0 0 270 0 1
footprint=1206.fp
T 43950 45150 5 10 1 0 0 0 1
ic=1V
}
C 42400 40950 1 0 0 spice-directive.sym
{
T 42400 41650 5 10 0 0 0 0 1
device=directive
T 42500 41350 5 10 1 1 0 0 1
refdes=A1
T 42500 41050 5 10 1 1 0 0 1
value=.TRAN 0.01us 1ms UIC
}
C 47550 44150 1 0 1 aswitch.sym
{
T 47140 46400 5 10 0 0 180 2 1
device=SPICE
T 46910 44800 5 10 1 1 0 0 1
refdes=A6
T 47140 46850 5 10 0 0 180 2 1
value=ASWITCH
}
C 47850 47700 1 0 0 diff_2.sym
{
T 48075 49100 5 8 0 0 0 0 1
device=SPICE
T 48200 48100 5 10 1 1 0 0 1
refdes=A2
T 48050 50100 5 8 0 0 0 0 1
value=DIFF_2
}
C 47850 46100 1 0 0 diff_2.sym
{
T 48075 47500 5 8 0 0 0 0 1
device=SPICE
T 48200 46500 5 10 1 1 0 0 1
refdes=A4
T 48050 48500 5 8 0 0 0 0 1
value=DIFF_2
}
C 48750 47500 1 0 0 hyst.sym
{
T 48975 48650 5 8 0 0 0 0 1
device=SPICE
T 49450 48100 5 10 1 1 0 0 1
refdes=A3
T 48950 50100 5 10 0 0 0 0 1
value=HYST
T 48950 48600 5 6 1 0 0 0 1
in_low=-0.001
T 48950 48500 5 6 1 0 0 0 1
in_high=0.001
T 48950 48400 5 6 1 0 0 0 1
hyst=0.01
T 48950 48700 5 6 1 0 0 0 1
out_upper_limit=1
T 48950 48800 5 6 1 0 0 0 1
out_lower_limit=0
}
C 48750 45900 1 0 0 hyst.sym
{
T 48975 47050 5 8 0 0 0 0 1
device=SPICE
T 49450 46500 5 10 1 1 0 0 1
refdes=A7
T 48950 48500 5 10 0 0 0 0 1
value=HYST
T 48950 45500 5 6 1 0 0 0 1
in_low=-0.001
T 48950 45600 5 6 1 0 0 0 1
in_high=0.001
T 48950 45700 5 6 1 0 0 0 1
hyst=0.01
T 48950 45400 5 6 1 0 0 0 1
out_upper_limit=1
T 48950 45300 5 6 1 0 0 0 1
out_lower_limit=0
}
C 49950 47800 1 0 0 adc_bridge.sym
{
T 50050 49900 5 10 0 0 0 0 1
device=SPICE
T 50050 48050 5 10 1 1 0 0 1
refdes=A5
T 50036 49700 5 10 0 0 0 0 1
value=ADC_BRIDGE
T 49850 47550 5 6 1 0 0 0 1
rise_delay=1e-6
T 49850 47650 5 6 1 0 0 0 1
fall_delay=1e-6
}
C 49950 46200 1 0 0 adc_bridge.sym
{
T 50050 48300 5 10 0 0 0 0 1
device=SPICE
T 50050 46450 5 10 1 1 0 0 1
refdes=A9
T 50036 48100 5 10 0 0 0 0 1
value=ADC_BRIDGE
T 49900 46050 5 6 1 0 0 0 1
rise_delay=1e-6
T 49900 45950 5 6 1 0 0 0 1
fall_delay=1e-6
}
C 52150 46400 1 0 0 dac_bridge.sym
{
T 52250 49100 5 10 0 0 0 0 1
device=SPICE
T 52250 46650 5 10 1 1 0 0 1
refdes=A12
T 52236 48900 5 10 0 0 0 0 1
value=DAC_BRIDGE
T 52250 46100 5 6 1 0 0 0 1
out_low=0
T 52250 46200 5 6 1 0 0 0 1
out_high=4.8
T 52250 46300 5 6 1 0 0 0 1
out_undef=2.5
}
C 50550 47400 1 0 0 d_nand_2.sym
{
T 50850 49700 5 10 0 0 0 0 1
device=SPICE
T 51050 48050 5 10 1 1 0 0 1
refdes=A8
T 50836 49500 5 10 0 0 0 0 1
value=D_NAND_2
}
C 50550 46200 1 0 0 d_nand_2.sym
{
T 50850 48500 5 10 0 0 0 0 1
device=SPICE
T 51000 46000 5 10 1 1 0 0 1
refdes=A11
T 50836 48300 5 10 0 0 0 0 1
value=D_NAND_2
}
N 50550 47500 50450 47500 4
N 50450 47300 50450 47500 4
N 50800 47300 51200 46900 4
N 50550 46700 50450 46700 4
N 50800 46900 51200 47300 4
N 51200 47300 51950 47300 4
N 51950 47300 51950 47700 4
N 51200 46900 51950 46900 4
N 51950 46900 51950 46500 4
N 50450 47300 50800 47300 4
N 50800 46900 50450 46900 4
N 51850 46500 52150 46500 4
N 50550 46300 50350 46300 4
N 49950 46300 49750 46300 4
N 50550 47900 50350 47900 4
N 49950 47900 49750 47900 4
N 54500 46500 52550 46500 4
C 41800 47850 1 0 0 pwr-gnd.sym
{
T 42090 48510 5 10 0 0 0 0 1
value=GND
T 42080 48900 5 10 0 0 0 0 1
device=SYMBOL
}
C 52150 47600 1 0 0 dac_bridge.sym
{
T 52250 50300 5 10 0 0 0 0 1
device=SPICE
T 52250 47850 5 10 1 1 0 0 1
refdes=A10
T 52236 50100 5 10 0 0 0 0 1
value=DAC_BRIDGE
}
N 51850 47700 52150 47700 4
N 47050 44750 53200 44750 4
N 53200 44750 53200 47700 4
N 53200 47700 52550 47700 4
N 41800 48250 41800 48050 4
N 48750 47900 48550 47900 4
C 47550 49100 1 270 0 res.sym
{
T 48150 48950 5 10 0 0 270 0 1
device=RESISTOR
T 47850 48700 5 10 1 1 0 0 1
refdes=R3
T 47850 48500 5 10 1 1 0 0 1
value=100k
T 48550 48950 5 10 0 0 270 0 1
footprint=1206.fp
}
C 47550 47550 1 270 0 res.sym
{
T 48150 47400 5 10 0 0 270 0 1
device=RESISTOR
T 47850 47150 5 10 1 1 0 0 1
refdes=R4
T 47850 46950 5 10 1 1 0 0 1
value=100k
T 48550 47400 5 10 0 0 270 0 1
footprint=1206.fp
}
C 47550 46000 1 270 0 res.sym
{
T 48150 45850 5 10 0 0 270 0 1
device=RESISTOR
T 47850 45500 5 10 1 1 0 0 1
refdes=R5
T 47850 45300 5 10 1 1 0 0 1
value=100k
T 48550 45850 5 10 0 0 270 0 1
footprint=1206.fp
}
N 47850 48100 47650 48100 4
N 47650 47550 47650 48200 4
N 47850 47700 45350 47700 4
N 47650 46100 47850 46100 4
C 47650 43450 1 0 0 pwr-gnd.sym
{
T 47940 44110 5 10 0 0 0 0 1
value=GND
T 47930 44500 5 10 0 0 0 0 1
device=SYMBOL
}
N 47650 45100 47650 43650 4
N 47650 46000 47650 46650 4
C 41500 48250 1 0 0 spice-vdc.sym
{
T 42200 48900 5 10 1 1 0 0 1
refdes=V1
T 42200 49300 5 10 0 0 0 0 1
device=SPICE
T 42200 48700 5 10 1 1 0 0 1
value=DC 5V
}
C 44450 48800 1 270 0 res.sym
{
T 45050 48650 5 10 0 0 270 0 1
device=RESISTOR
T 44100 48400 5 10 1 1 0 0 1
refdes=R1
T 44100 48200 5 10 1 1 0 0 1
value=10k
T 45450 48650 5 10 0 0 270 0 1
footprint=1206.fp
}
C 44450 47500 1 270 0 res.sym
{
T 45050 47350 5 10 0 0 270 0 1
device=RESISTOR
T 44150 47100 5 10 1 1 0 0 1
refdes=R2
T 44100 46900 5 10 1 1 0 0 1
value=10k
T 45450 47350 5 10 0 0 270 0 1
footprint=1206.fp
}
N 45350 47700 45350 46500 4
N 44550 46000 44550 46600 4
N 44550 46500 47850 46500 4
{
T 44100 46450 5 10 1 1 0 0 1
netname=CAP
}
N 47650 49100 47650 49600 4
N 47650 49600 41800 49600 4
N 41800 49600 41800 49450 4
N 44550 48800 44550 49600 4
N 44550 47500 44550 47900 4
N 43400 47650 44550 47650 4
{
T 44600 47600 5 10 1 1 0 0 1
netname=DISCH
}
N 47550 44250 47650 44250 4
N 46550 44250 43400 44250 4
N 43400 44250 43400 47650 4
N 50450 46700 50450 46900 4
N 48550 46300 48750 46300 4
T 45550 44300 9 8 1 0 0 0 1
DISCH (7)
T 45500 46550 9 8 1 0 0 0 1
TRIG (2)
T 45450 47800 9 8 1 0 0 0 1
THRES (6)
T 46850 48050 9 8 1 0 0 0 1
CONT (5)
T 53600 46550 9 8 1 0 0 0 1
OUT (3)
T 45650 49650 9 8 1 0 0 0 1
VDD (8)
B 46400 44100 7100 5850 3 0 0 0 -1 -1 0 -1 -1 -1 -1 -1
T 47750 43800 9 8 1 0 0 0 1
GND (1)
T 50250 49700 9 10 1 0 0 0 1
Internal structure of TIMER_555 Model