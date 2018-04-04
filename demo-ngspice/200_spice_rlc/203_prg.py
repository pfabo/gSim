#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('203_circ.sch')
# print(desc['varnames'])


t = data['time']*1e3
v1 = data['v(q1)']
v2 = data['v(q2)']
v3 = data['v(q3)']
v4 = data['v(q4)']

plot(t,v1, label='Q1')
plot(t,v2, label='Q2')
plot(t,v3, label='Q3')
plot(t,v4, label='Q4')
legend(loc=3)
xlabel('Time [ms]')
ylabel('VQx [V]')
grid()
savefig('203_img.png')
#show()


