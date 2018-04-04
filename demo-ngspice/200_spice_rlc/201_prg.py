#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('201_circ.sch')
#print(desc['varnames'])

f = data['frequency'].real
v1 = abs(data['v(out1)'])
v2 = abs(data['v(out2)'])
v3 = abs(data['v(out3)'])
v4 = abs(data['v(out4)'])

semilogx(f,v1, label='OUT1')
semilogx(f,v2, label='OUT2')
semilogx(f,v3, label='OUT3')
semilogx(f,v4, label='OUT4')
legend(loc=3)
xlabel('f [Hz]')
ylabel('Vq [V]')
title('Ex.201')
grid()
savefig('201_img.png')
#show()


