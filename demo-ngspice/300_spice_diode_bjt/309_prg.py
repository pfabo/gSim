#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('309_circ.sch')
#print(desc['varnames'])

t = data['time']*1e6
v1 = data['v(out)']
v2 = data['v(in)']

plot(t,v1, 'b', label='VOUT')
plot(t,v2, 'r', label='VIN')
xlim(0, t[-1])
grid()
legend()
ylabel('Vout [V]')
xlabel('Time [uS]')
savefig('309_img.png')
#show()


