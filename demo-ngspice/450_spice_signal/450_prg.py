#!/usr/bin/env python

import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('450_circ.sch')

t = data['time']*1e9
vin = data['v(am)']
vout = data['v(s2)']

plot(t,vin, label='AM', alpha=0.3)
plot(t,vout, 'r', label='DT')
xlabel('Time [ns]')
ylabel('Voltage [V]')
xlim(0, t[-1])
grid()
legend(loc=4)
savefig('450_img.png')
#show()

