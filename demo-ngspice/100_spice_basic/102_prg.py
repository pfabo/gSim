#!/usr/bin/env python

import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('102_circ.sch')

t = data['time']*1e3
v1 = data['v(out1)']
v2 = data['v(out2)']
v3 = data['v(out3)']

plot(t,v1, label='OUT1 RC')
plot(t,v2, label='OUT2 CR')
plot(t,v3, label='OUT3 CRL')
xlabel('Time [ms]') 
ylabel('Voltage [V]') 
grid()
legend()
savefig('102_img.png')
#show()

