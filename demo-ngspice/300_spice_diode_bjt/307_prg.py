#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('307_circ.sch')
#print(desc['varnames'])

t = data['time']*1e3
v1 = data['v(va)']
v3 = data['v(vb)']
v2 = data['v(vd)']


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
savefig('307_img.png')
#show()


