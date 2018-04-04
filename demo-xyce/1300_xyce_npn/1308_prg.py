#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

fileName='1308'
gx = gSim(fileName+'_circ.sch', 'XYCE')
gx.netlist()
data, desc = gx.sim()

t = data['time']*1e3
v1 = data['OUT']
v2 = data['IN']

plot(t,v1, 'b', label='VOUT')
plot(t,v2, 'r', label='VIN')
grid()
legend()
ylabel('Vout [V]')
savefig(fileName+'_img.png')
#show()


