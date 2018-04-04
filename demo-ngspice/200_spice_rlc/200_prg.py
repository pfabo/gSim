#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('200_circ.sch')
#print(desc['varnames'])

f = data['frequency'].real
v1 = abs(data['v(q1)'])
v2 = abs(data['v(q2)'])
v3 = abs(data['v(q3)'])
v4 = abs(data['v(q4)'])

semilogx(f,v1, label='Q1')
semilogx(f,v2, label='Q2')
semilogx(f,v3, label='Q3')
semilogx(f,v4, label='Q4')
legend()
xlabel('f [Hz]')
ylabel('Vq [V]')
grid()
savefig('200_img.png')
#show()


