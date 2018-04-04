#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('204_circ.sch')
# print(desc['varnames'])

f = data['frequency'].real
v1 = abs(data['v(ul)'])
v2 = abs(data['v(ur)'])
v3 = abs(data['v(uc)'])

semilogx(f,v1, label='UL')
semilogx(f,v2, label='UR')
semilogx(f,v3, label='UC')
title('Ex.204 Serial RLC')
legend()
xlabel('f [Hz]')
ylabel('Vq [V]')
grid()
savefig('204_img_1.png')
#show()

v1 = abs(data['v(il)'])*1e3
v2 = abs(data['v(ir)'])*1e3
v3 = abs(data['v(ic)'])*1e3

semilogx(f,v1, label='IL')
semilogx(f,v2, label='IR')
semilogx(f,v3, label='IC')
title('Ex.204 Parallel RLC')
legend()
xlabel('f [Hz]')
ylabel('I [mA]')
grid()
savefig('204_img_2.png')
#show()


