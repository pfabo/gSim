#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

gx = gSim('1251_circ.sch','XYCE')
gx.netlist()
data, desc = gx.sim()

f = data['frequency'].real
v1 = abs(data['OUT1'])
v2 = abs(data['OUT2'])
v3 = abs(data['OUT3'])
v4 = abs(data['OUT4'])

semilogx(f,v1, label='OUT1')
semilogx(f,v2, label='OUT2')
semilogx(f,v3, label='OUT3')
semilogx(f,v4, label='OUT4')
legend(loc=3)
xlabel('f [Hz]')
ylabel('Vq [V]')
title('Ex.201')
grid()
savefig('1251_img.png')
#show()


