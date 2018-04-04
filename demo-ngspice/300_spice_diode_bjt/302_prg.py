#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('302_circ.sch')
#print(desc['varnames'])

t = data['frequency'].real
v = abs(data['v(out)'])
p = unwrap(angle(data['v(out)']))

graph=[subplot(211),subplot(212)]

graph[0].semilogx(t,v, 'b', label='Ampl')
graph[0].grid()
graph[0].legend()
graph[0].set_ylabel('|K|')

graph[1].semilogx(t,p, 'r', label='Phase')
graph[1].grid()
graph[1].legend()
graph[1].set_xlabel('f [Hz]')
graph[1].set_ylabel('phi [rad]')
savefig('302_img.png')
#show()

