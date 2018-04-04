import sys
import os
sys.path.append('../../py')

from pylab import *
from gsim import *

fileName='1501'
gx = gSim(fileName+'_circ.sch','XYCE')
gx.netlist()
data, desc = gx.sim()

t = data['time']
vz = data['Z']
vy = data['Y']
vx = data['X']

graph=[subplot(211),subplot(212)]

graph[0].plot(t,vz, label='Z')
graph[0].plot(t,vy, label='Y')
graph[0].plot(t,vx, label='X')
graph[0].set_xlim(0, t[-1])
graph[0].grid()
graph[0].legend(loc='upper right')

graph[1].plot(vx,vz, 'r-', label='X-Z')
graph[1].grid()
graph[1].legend(loc='upper right')
savefig(fileName+'_img.png')
#show()
