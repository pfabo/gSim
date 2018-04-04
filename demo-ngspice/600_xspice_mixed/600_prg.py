#!/usr/bin/env python
import sys
import os
os.system("echo  'codemodel ../../model/scm/user.cm' > .spiceinit")
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('600_circ.sch')
#print(desc['varnames'])



t = data['time']*1000
va = data['v(a)']/5.5
vb = data['v(b)']/5.5 + 1
vc = data['v(c)']/5.5 + 2
vd = data['v(d)']/5.5 + 3

vq = data['v(q)']

graph=[subplot(211),subplot(212)]

graph[0].plot(t,va, label='A')
graph[0].plot(t,vb, label='B')
graph[0].plot(t,vc, label='C')
graph[0].plot(t,vd, label='D')
graph[0].set_xlim(0, t[-1])
graph[0].grid()
graph[0].legend(loc='upper right')

graph[1].plot(t,vq, label='Analog')
graph[1].set_xlabel('t [ms]')
graph[1].set_xlim(0, t[-1])
graph[1].grid()
graph[1].legend(loc='upper right')
savefig('600_img.png')
#show()



