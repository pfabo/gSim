import sys
import os
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('500_circ.sch')
'''
vname = desc['varnames']
vunit = desc['varunits']
print('name', ' \t', desc[b'plotname'])
print('vars', ' \t', int(desc[b'no. variables']))
print('points', ' \t', int(desc[b'no. points']))
print('var', '\t|', 'unit')
print('---------------------------------------')
for i in range(len(vname)):
    print(vname[i], '\t|', vunit[i])
'''

t = data['time']*1e3
v1 = data['v(y1)']
v2 = data['v(y2)']

plot(t,v1, label='Y1')
plot(t,v2, label='Y2')
legend(loc='upper right')
xlim(0, t[-1])
xlabel('Time [ms]')
grid()
savefig('500_img.png')
#show()


