#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('1205_circ.sch', 'XYCE')
t = data['time']*1e3
v1 = data['OUT']
v2 = data['IN']

plot(t,v1, label='OUT')
plot(t,v2, label='IN')

legend(loc=3)
xlim(0, t[-1])
xlabel('Time [ms]')
ylabel('Voltage [V]')
title('Ex. 205')
grid()
savefig('1205_img.png')
#show()


