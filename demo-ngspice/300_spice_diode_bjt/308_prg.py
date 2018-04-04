#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('308_circ.sch')
#print(desc['varnames'])

t = data['time']*1e3
v1 = data['v(out)']
v2 = data['v(in)']

plot(t,v1, 'b', label='VOUT')
plot(t,v2, 'r', label='VIN')
grid()
legend()
ylabel('Vout [V]')
savefig('308_img.png')
#show()


