#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

fileName='1307'
gx = gSim(fileName+'_circ.sch','XYCE')
gx.netlist()
data, desc = gx.sim()

t = data['time']*1e3
v1 = data['VA']
v3 = data['VB']
v2 = data['VD']

graph=[subplot(211),subplot(212)]

graph[0].plot(t,v1, 'b', label='VA')
graph[0].plot(t,v3, 'g', label='VB')
graph[0].grid()
graph[0].legend()
graph[0].set_ylabel('Vout [V]')

graph[1].plot(t,v2, 'r', label='VA-VB')
graph[1].grid()
graph[1].legend()
graph[1].set_xlabel('t [ms]')
graph[1].set_ylabel('Vd [V]')
savefig(fileName+'_img.png')
#show()


