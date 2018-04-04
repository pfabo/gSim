#!/usr/bin/env python
import os
os.system("echo  'codemodel ../../model/scm/user.cm' > .spiceinit")
import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('551_circ.sch')
#print(desc['varnames'])

t = data['time']*1000
va = data['v(a)']/5.5
vb = data['v(b)']/5.5 + 1
vc = data['v(c)']/5.5 + 2
vd = data['v(d)']/5.5 + 3


plot(t,va, label='A')
plot(t,vb, label='B')
plot(t,vc, label='C')
plot(t,vd, label='D')
xlabel('t [ms]')
grid()
legend()
savefig('551_img.png')
#show()


