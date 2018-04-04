#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *


gx = gSim('1253_circ.sch','XYCE')
gx.netlist()
data, desc = gx.sim()

t = data['time']*1e3
v1 = data['Q1']
v2 = data['Q2']
v3 = data['Q3']
v4 = data['Q4']

plot(t,v1, label='Q1')
plot(t,v2, label='Q2')
plot(t,v3, label='Q3')
plot(t,v4, label='Q4')
legend(loc=3)
xlabel('Time [ms]')
ylabel('Qx [V]')
grid()
savefig('1253_img.png')
#show()


