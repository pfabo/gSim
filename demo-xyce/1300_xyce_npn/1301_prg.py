#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

fileName='1301'

gx = gSim(fileName+'_circ.sch', 'XYCE')
gx.netlist()
data, desc = gx.sim()

t = data['frequency'].real
v = abs(data['OUT'])
p = angle(data['OUT'])

graph=[subplot(211),subplot(212)]

graph[0].plot(t,v, 'b', label='Ampl')
graph[0].grid()
graph[0].legend()
graph[0].set_ylabel('|K|')

graph[1].plot(t,p, 'r', label='Phase')
graph[1].grid()
graph[1].legend()
graph[1].set_xlabel('f [Hz]')
graph[1].set_ylabel('phi [rad]')
savefig(fileName+'_img.png')
#show()

