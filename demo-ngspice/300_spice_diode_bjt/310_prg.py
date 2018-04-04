#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('310_circ.sch')
#print(desc['varnames'])

t = data['time']*1e3
v1 = data['v(out)']
v2 = data['v(ve)']

plot(t,v1, 'b', label='VOUT')
plot(t,v2, 'r', label='VE')

xlim(0, t[-1])
grid()
legend()
ylabel('Vout [V]')
xlabel('Time [ms]')
savefig('310_img.png')
#show()


