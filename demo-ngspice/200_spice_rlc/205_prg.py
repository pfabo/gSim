#!/usr/bin/env python

import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('205_circ.sch')
#print(desc['varnames'])

t = data['time']*1e3
v1 = data['v(out)']
v2 = data['v(in)']

plot(t,v1, label='OUT')
plot(t,v2, label='IN')

legend(loc=3)
xlim(0, t[-1])
xlabel('Time [ms]')
ylabel('Voltage [V]')
title('Ex. 205')
grid()
savefig('205_img.png')
#show()


