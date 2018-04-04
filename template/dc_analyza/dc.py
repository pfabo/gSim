#!/usr/bin/env python

from pylab import *
import sys
sys.path.append('../../py')

from gsim import *

data, desc = gs('dc.sch')           # Ngspice
#data, desc = gs('dc.sch', 'XYCE')  # Xyce

vname = desc['varnames']
vunit = desc['varunits']
print('name', ' \t', desc[b'plotname'])
print('vars', ' \t', int(desc[b'no. variables']))
print('no.', ' \t', int(desc[b'no. points']))
print('var', '\t|', 'unit')
print('---------------------------------------')
for i in range(len(vname)):
    print(vname[i], '\t|', vunit[i])
