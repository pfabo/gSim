v 20130925 2
C 40000 40000 0 0 0 title-bordered-A3.sym
T 49300 40900 9 14 1 0 0 0 2
Example 502
The Rossler Attractor
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / A
T 53300 40300 9 8 1 0 0 0 1
100401 PF
C 41900 46500 1 0 0 spice-directive.sym
{
T 41900 47200 5 10 0 0 0 0 1
device=directive
T 42000 46900 5 10 1 1 0 0 1
refdes=A12
T 42000 46600 5 10 1 1 0 0 1
value=.TRAN 1e-3 300
}
C 44900 42800 1 0 0 spice-vdc.sym
{
T 45600 43550 5 10 1 1 0 0 1
refdes=V1
T 45600 43850 5 10 0 0 0 0 1
device=SPICE
T 45600 43300 5 10 1 1 0 0 1
value=DC 0.2
}
C 45200 42500 1 0 0 pwr-gnd.sym
{
T 45490 43160 5 10 0 0 0 0 1
value=GND
T 45480 43550 5 10 0 0 0 0 1
device=SYMBOL
}
N 45200 42800 45200 42700 4
N 45300 44100 45200 44100 4
N 45200 44100 45200 44000 4
C 43400 42500 1 0 0 pwr-gnd.sym
{
T 43690 43160 5 10 0 0 0 0 1
value=GND
T 43680 43550 5 10 0 0 0 0 1
device=SYMBOL
}
N 43400 42800 43400 42700 4
C 43100 42800 1 0 0 spice-vdc.sym
{
T 43800 43550 5 10 1 1 0 0 1
refdes=V2
T 43800 43300 5 10 1 1 0 0 1
value=DC 0.2
T 43800 43850 5 10 0 0 0 0 1
device=SPICE
}
C 41600 42500 1 0 0 pwr-gnd.sym
{
T 41890 43160 5 10 0 0 0 0 1
value=GND
T 41880 43550 5 10 0 0 0 0 1
device=SYMBOL
}
N 41600 42800 41600 42700 4
C 41300 42800 1 0 0 spice-vdc.sym
{
T 42000 43550 5 10 1 1 0 0 1
refdes=V3
T 42000 43300 5 10 1 1 0 0 1
value=DC 5.7
T 42000 43850 5 10 0 0 0 0 1
device=SPICE
}
N 41700 44100 41600 44100 4
N 41600 44100 41600 44000 4
N 43400 44100 43500 44100 4
N 43400 44100 43400 44000 4
T 45000 42200 9 10 1 0 0 0 1
Parameter A
T 43200 42200 9 10 1 0 0 0 1
Parameter B
T 41400 42200 9 10 1 0 0 0 1
Parameter C
C 45300 44000 1 0 0 port.sym
{
T 45550 44100 5 10 1 1 0 1 1
net=A:1
T 45500 44600 5 10 0 0 0 0 1
device=none
T 45650 43850 5 10 0 1 0 1 1
value=IO
}
C 43500 44000 1 0 0 port.sym
{
T 43750 44100 5 10 1 1 0 1 1
net=B:1
T 43700 44600 5 10 0 0 0 0 1
device=none
T 43850 43850 5 10 0 1 0 1 1
value=IO
}
C 41700 44000 1 0 0 port.sym
{
T 41950 44100 5 10 1 1 0 1 1
net=C:1
T 41900 44600 5 10 0 0 0 0 1
device=none
T 42050 43850 5 10 0 1 0 1 1
value=IO
}
C 47500 45600 1 0 1 port.sym
{
T 47250 45700 5 10 1 1 0 7 1
net=X:1
T 47300 46200 5 10 0 0 0 6 1
device=none
T 47150 45450 5 10 0 1 0 7 1
value=IO
}
C 47500 46600 1 0 1 port.sym
{
T 47250 46700 5 10 1 1 0 7 1
net=Y:1
T 47300 47200 5 10 0 0 0 6 1
device=none
T 47150 46450 5 10 0 1 0 7 1
value=IO
}
C 47500 47000 1 0 1 port.sym
{
T 47250 47100 5 10 1 1 0 7 1
net=Z:1
T 47300 47600 5 10 0 0 0 6 1
device=none
T 47150 46850 5 10 0 1 0 7 1
value=IO
}
C 47900 46700 1 0 0 summer_2.sym
{
T 48125 48100 5 8 0 0 0 0 1
device=SPICE
T 48250 47100 5 10 1 1 0 0 1
refdes=A1
T 48100 49100 5 8 0 0 0 0 1
value=SUMMER_2
T 47895 47150 5 6 1 1 0 0 1
in_gain_1=1.0
T 47895 46750 5 6 1 1 0 0 1
in_gain_2=1.0
T 48495 46950 5 6 1 1 0 0 1
out_gain=-1.0
}
C 49100 46500 1 0 0 int.sym
{
T 49325 47850 5 10 0 0 0 0 1
device=SPICE
T 49600 47200 5 10 1 1 0 0 1
refdes=A2
T 49300 49300 5 10 0 0 0 0 1
value=INT
T 49570 46900 5 6 1 1 0 1 1
gain=1.0
}
N 49100 46900 48600 46900 4
N 47500 47100 47900 47100 4
N 47500 46700 47900 46700 4
C 51200 46800 1 0 0 port.sym
{
T 51450 46900 5 10 1 1 0 1 1
net=X:1
T 51400 47400 5 10 0 0 0 0 1
device=none
T 51550 46650 5 10 0 1 0 1 1
value=IO
}
N 51200 46900 50100 46900 4
C 48900 45000 1 0 0 summer_2.sym
{
T 49125 46400 5 8 0 0 0 0 1
device=SPICE
T 49250 45400 5 10 1 1 0 0 1
refdes=A4
T 49100 47400 5 8 0 0 0 0 1
value=SUMMER_2
T 48895 45450 5 6 1 1 0 0 1
in_gain_1=1.0
T 48895 45050 5 6 1 1 0 0 1
in_gain_2=1.0
T 49495 45250 5 6 1 1 0 0 1
out_gain=1.0
}
C 47700 44800 1 0 0 mult_2.sym
{
T 47925 46200 5 8 0 0 0 0 1
device=SPICE
T 48050 45200 5 10 1 1 0 0 1
refdes=A3
T 47900 47200 5 8 0 0 0 0 1
value=MULT_2
T 47695 45250 5 6 1 1 0 0 1
in_gain_1=1.0
T 47695 44850 5 6 1 1 0 0 1
in_gain_2=1.0
T 48295 45050 5 6 1 1 0 0 1
out_gain=1.0
}
C 47500 45100 1 0 1 port.sym
{
T 47250 45200 5 10 1 1 0 7 1
net=A:1
T 47300 45700 5 10 0 0 0 6 1
device=none
T 47150 44950 5 10 0 1 0 7 1
value=IO
}
C 47500 44700 1 0 1 port.sym
{
T 47250 44800 5 10 1 1 0 7 1
net=Y:1
T 47300 45300 5 10 0 0 0 6 1
device=none
T 47150 44550 5 10 0 1 0 7 1
value=IO
}
N 47500 44800 47700 44800 4
N 47500 45200 47700 45200 4
N 48400 45000 48900 45000 4
N 48900 45400 48400 45400 4
N 48400 45400 48400 45700 4
C 50000 44800 1 0 0 int.sym
{
T 50225 46150 5 10 0 0 0 0 1
device=SPICE
T 50500 45500 5 10 1 1 0 0 1
refdes=A6
T 50200 47600 5 10 0 0 0 0 1
value=INT
T 50470 45200 5 6 1 1 0 1 1
gain=1.0
}
N 50000 45200 49600 45200 4
C 51200 45100 1 0 0 port.sym
{
T 51450 45200 5 10 1 1 0 1 1
net=Y:1
T 51400 45700 5 10 0 0 0 0 1
device=none
T 51550 44950 5 10 0 1 0 1 1
value=IO
}
N 51200 45200 51000 45200 4
N 47500 45700 48400 45700 4
C 47700 43400 1 0 0 summer_2.sym
{
T 47925 44800 5 8 0 0 0 0 1
device=SPICE
T 48050 43800 5 10 1 1 0 0 1
refdes=A5
T 47900 45800 5 8 0 0 0 0 1
value=SUMMER_2
T 47695 43850 5 6 1 1 0 0 1
in_gain_1=1.0
T 47695 43450 5 6 1 1 0 0 1
in_gain_2=-1.0
T 48295 43650 5 6 1 1 0 0 1
out_gain=1.0
}
C 47500 43300 1 0 1 port.sym
{
T 47250 43400 5 10 1 1 0 7 1
net=C:1
T 47300 43900 5 10 0 0 0 6 1
device=none
T 47150 43150 5 10 0 1 0 7 1
value=IO
}
C 47500 43700 1 0 1 port.sym
{
T 47250 43800 5 10 1 1 0 7 1
net=X:1
T 47300 44300 5 10 0 0 0 6 1
device=none
T 47150 43550 5 10 0 1 0 7 1
value=IO
}
C 48700 43200 1 0 0 mult_2.sym
{
T 48925 44600 5 8 0 0 0 0 1
device=SPICE
T 49050 43600 5 10 1 1 0 0 1
refdes=A7
T 48900 45600 5 8 0 0 0 0 1
value=MULT_2
T 48695 43650 5 6 1 1 0 0 1
in_gain_1=1.0
T 48695 43250 5 6 1 1 0 0 1
in_gain_2=1.0
T 49295 43450 5 6 1 1 0 0 1
out_gain=1.0
}
C 47500 42900 1 0 1 port.sym
{
T 47250 43000 5 10 1 1 0 7 1
net=Z:1
T 47300 43500 5 10 0 0 0 6 1
device=none
T 47150 42750 5 10 0 1 0 7 1
value=IO
}
C 48700 42500 1 0 1 port.sym
{
T 48450 42600 5 10 1 1 0 7 1
net=B:1
T 48500 43100 5 10 0 0 0 6 1
device=none
T 48350 42350 5 10 0 1 0 7 1
value=IO
}
N 47500 43800 47700 43800 4
N 47500 43400 47700 43400 4
N 47500 43000 48300 43000 4
N 48300 43000 48300 43200 4
N 48300 43200 48700 43200 4
N 48400 43600 48700 43600 4
C 49900 43000 1 0 0 summer_2.sym
{
T 50125 44400 5 8 0 0 0 0 1
device=SPICE
T 50250 43400 5 10 1 1 0 0 1
refdes=A8
T 50100 45400 5 8 0 0 0 0 1
value=SUMMER_2
T 49895 43450 5 6 1 1 0 0 1
in_gain_1=1.0
T 49895 43050 5 6 1 1 0 0 1
in_gain_2=1.0
T 50495 43250 5 6 1 1 0 0 1
out_gain=1.0
}
N 49400 43400 49900 43400 4
N 48700 42600 49400 42600 4
N 49400 42600 49400 43000 4
N 49400 43000 49900 43000 4
C 50800 42800 1 0 0 int.sym
{
T 51025 44150 5 10 0 0 0 0 1
device=SPICE
T 51300 43500 5 10 1 1 0 0 1
refdes=A9
T 51000 45600 5 10 0 0 0 0 1
value=INT
T 51270 43200 5 6 1 1 0 1 1
gain=1.0
}
C 52000 43100 1 0 0 port.sym
{
T 52250 43200 5 10 1 1 0 1 1
net=Z:1
T 52200 43700 5 10 0 0 0 0 1
device=none
T 52350 42950 5 10 0 1 0 1 1
value=IO
}
N 50600 43200 50800 43200 4
N 51800 43200 52000 43200 4
