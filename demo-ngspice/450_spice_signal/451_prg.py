#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('451_circ.sch')

vname = desc['varnames']
vunit = desc['varunits']

t = data['time']*1e3
vout = data['v(out)']

plot(t,vout, 'r', label='DT')
xlabel('Time [ms]')
ylabel('Voltage [V]')
xlim(0, t[-1])
grid()
savefig('451_img.png')
#show()

