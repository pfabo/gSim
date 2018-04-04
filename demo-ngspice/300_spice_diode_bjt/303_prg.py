#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('303_circ.sch')
#print(desc['varnames'])

t = data['time']*1e6
v1 = data['v(out)']
v2 = data['v(nb2)']


graph=[subplot(211),subplot(212)]

graph[0].plot(t,v1, 'b', label='VOUT')
graph[0].grid()
graph[0].legend()
graph[0].set_ylabel('V [V]')

graph[1].plot(t,v2, 'r', label='VC1')
graph[1].grid()
graph[1].legend()
graph[1].set_xlabel('t [us]')
graph[1].set_ylabel('V [V]')
savefig('303_img.png')
#show()


