v 20110115 2
C 40000 40000 0 0 0 title-bordered-A3.sym
T 49350 40950 9 14 1 0 0 0 2
Comparator
XSPICE MAcromodel
T 49450 40300 9 8 1 0 0 0 1
1
T 50950 40300 9 8 1 0 0 0 1
1
T 53300 40600 9 8 1 0 0 0 1
1.00 / A
T 53300 40300 9 8 1 0 0 0 1
090908 PF
N 45750 46250 46500 46250 4
N 45750 44750 46500 44750 4
N 48350 45500 48150 45500 4
C 46400 45200 1 0 0 summer_2_1.sym
{
T 46325 46700 5 8 0 0 0 0 1
device=SPICE
T 46600 45900 5 10 1 1 0 0 1
refdes=A1
T 46300 47700 5 8 0 0 0 0 1
value=SUMMER_2
T 46545 45700 5 6 1 1 0 0 1
in_gain_1=1.0
T 46545 45200 5 6 1 1 0 0 1
in_gain_2=-1.0
T 46695 45550 5 6 1 1 0 0 1
out_gain=1.0
}
N 46500 45800 46500 46250 4
N 46500 45200 46500 44750 4
N 47150 45500 46800 45500 4
C 47150 45100 1 0 0 hyst.sym
{
T 47375 46250 5 8 0 0 0 0 1
device=SPICE
T 47850 45700 5 10 1 1 0 0 1
refdes=A2
T 47350 47700 5 10 0 0 0 0 1
value=HYST
T 47295 46450 5 10 1 0 0 0 1
in_low=0.0
T 47295 46250 5 10 1 0 0 0 1
in_high=0.0
T 47295 46050 5 10 1 0 0 0 1
hyst=1e-6
}
C 44850 46150 1 0 0 port-sin.sym
{
T 44900 46250 5 10 1 1 0 1 1
net=IN+:1
T 44850 46450 5 10 0 0 0 0 1
device=SYMBOL
T 45850 47550 5 10 0 0 0 7 1
value=NET
}
C 44850 44650 1 0 0 port-sin.sym
{
T 44900 44750 5 10 1 1 0 1 1
net=IN-:1
T 44850 44950 5 10 0 0 0 0 1
device=SYMBOL
T 45850 46050 5 10 0 0 0 7 1
value=NET
}
C 48350 45400 1 0 0 port-sout.sym
{
T 48600 45500 5 10 1 1 0 1 1
net=OUT:1
T 48550 45700 5 10 0 0 0 0 1
device=SYMBOL
T 49500 46750 5 10 0 0 0 7 1
value=NET
}
L 56000 51100 50500 51100 3 0 0 0 -1 -1
L 50500 51100 50500 47100 3 0 0 0 -1 -1
L 56000 47100 56000 51100 3 0 0 0 -1 -1
L 50500 47100 56000 47100 3 0 0 0 -1 -1
L 50500 50700 56000 50700 3 0 0 0 -1 -1
L 56000 50300 50500 50300 3 0 0 0 -1 -1
L 52000 51100 52000 50300 3 0 0 0 -1 -1
T 52200 50800 9 10 1 0 0 0 1
\\sym\\xspice_model\\xcomp.sym
T 52200 50400 9 10 1 0 0 0 1
\\model\\xspice\\xcomp.spm
T 50700 50800 9 10 1 0 0 0 1
Symbol 
T 50700 50400 9 10 1 0 0 0 1
Macromodel
C 52600 48600 1 0 0 xcomp.sym
{
T 52825 50850 5 8 0 0 0 0 1
device=SPICE
T 53300 49200 5 10 1 1 0 0 1
refdes=X?
T 52800 51200 5 10 0 0 0 0 1
value=XCOMP
}
