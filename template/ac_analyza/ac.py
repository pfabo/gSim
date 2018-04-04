#!/usr/bin/env python

# Template pre AC analyzu

import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('ac.sch')               # Ngspice
#data, desc = gs('ac.sch', 'XYCE')      # Xyce

vname = desc['varnames']
vunit = desc['varunits']
print('name', ' \t', desc[b'plotname'])
print('vars', ' \t', int(desc[b'no. variables']))
print('no.', ' \t', int(desc[b'no. points']))
print('var', '\t|', 'unit')
print('---------------------------------------')
for i in range(len(vname)):
    print(vname[i], '\t|', vunit[i])

f = data['frequency'].real

v = abs(data['v(out)'])                 # Ngspice
p = angle(data['v(out)'])*180/pi        

#v = abs(data['OUT'])                   # Xyce
#p = angle(data['OUT'])*180/pi        

graph=[subplot(211),subplot(212)]

graph[0].semilogx(f,v, 'b', label='Ampl')
graph[0].grid()
graph[0].legend()
graph[0].set_ylabel('|K|')

graph[1].semilogx(f,p, 'r', label='Phase')
graph[1].grid()
graph[1].legend()
graph[1].set_xlabel('f [Hz]')
graph[1].set_ylabel('phi [deg]')

show()

