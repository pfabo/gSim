#!/usr/bin/env python
import os
import sys
print(os.getcwd())
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('100_circ.sch')

t = data['time']
vp = data['v(pulse)']
vs = data['v(sin)']
vf = data['v(sffm)']
ve = data['v(exp)']

plot(t,vp, label='PULSE')
plot(t,vs, label='SIN')
plot(t,vf, label='SFFM')
plot(t,ve, label='EXP')
xlabel('Time [ms]') 
ylabel('Voltage [V]') 
grid()
legend()
savefig('100_img.png')
#show()

