#!/usr/bin/env python
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

gx = gSim('1254_circ.sch','XYCE')
gx.netlist()
data, desc = gx.sim()

#print(desc['varnames'])

f = data['frequency'].real
v1 = abs(data['UL'])
v2 = abs(data['UR'])
v3 = abs(data['UC'])

semilogx(f,v1, label='UL')
semilogx(f,v2, label='UR')
semilogx(f,v3, label='UC')
title('Ex.1254 Serial RLC')
legend()
xlabel('f [Hz]')
ylabel('Vq [V]')
grid()
savefig('254_img_1.png')
#show()

v1 = abs(data['V3#branch'])*1e3
v2 = abs(data['V2#branch'])*1e3
v3 = abs(data['V4#branch'])*1e3

semilogx(f,v1, label='IL')
semilogx(f,v2, label='IR')
semilogx(f,v3, label='IC')
title('Ex.1254 Parallel RLC')
legend()
xlabel('f [Hz]')
ylabel('I [mA]')
grid()
savefig('254_img_2.png')
#show()


