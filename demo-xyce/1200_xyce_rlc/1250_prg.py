#!/usr/bin/env python
import sys
sys.path.append('../../py')
from pylab import *
from gsim import *

gx = gSim('1250_circ.sch', 'XYCE')
gx.netlist()
data, desc = gx.sim()

f = data['frequency'].real
v1 = abs(data['Q1'])
v2 = abs(data['Q2'])
v3 = abs(data['Q3'])
v4 = abs(data['Q4'])

semilogx(f,v1, label='Q1')
semilogx(f,v2, label='Q2')
semilogx(f,v3, label='Q3')
semilogx(f,v4, label='Q4')
legend()
xlabel('f [Hz]')
ylabel('Vq [V]')
grid()
savefig('1250_img.png')
#show()


