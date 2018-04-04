#!/usr/bin/env python
# Template pre transient analyzu

import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('tr.sch')       # Ngspice
#data, desc = gs('tr.sch', 'XYCE')       # Ngspice

vname = desc['varnames']
vunit = desc['varunits']
print('name', ' \t', desc[b'plotname'])
print('vars', ' \t', int(desc[b'no. variables']))
print('no.', ' \t', int(desc[b'no. points']))
print('var', '\t|', 'unit')
print('---------------------------------------')
for i in range(len(vname)):
    print(vname[i], '\t|', vunit[i])


t = data['time']*1e9

vin = data['v(in)']            # Ngspice
vout = data['v(out)']

#vin = data['IN']                # Xyce
#vout = data['OUT']

plot(t,vin, label='Vin')
plot(t,vout, label='Vout')
xlabel('Time [ns]')
ylabel('Vin, Vout [V]')
xlim(0, t[-1])
grid()
legend()
show()

