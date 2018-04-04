import sys
import os
sys.path.append('../../py')

from pylab import *
from gsim import *

fileName='1500'
gx = gSim(fileName+'_circ.sch','XYCE')
gx.netlist()
data, desc = gx.sim()

t = data['time']*1e3
v1 = data['Y1']
v2 = data['Y2']

plot(t,v1, 'r-', label='Y1')
plot(t,v2, 'b-', label='Y2')
legend(loc='upper right')
xlim(0, t[-1])
xlabel('Time [ms]')
title('Xyce Demo - Generator')
grid()
savefig(fileName+'_img.png')
#show()


