#!/usr/bin/env python
import sys
sys.path.append('../../py')

import pylab as plt 
from gsim import *

g=gSim('311_circ.sch')
g.netlist()

for i in arange(10e-6, 1e-7, -1e-6):
    g.setPAR('IB',i)
    data, param = g.sim()
    ic = -data['i(v1)']*1e3
    vc = data['v(c)']
    plt.plot(vc,ic,'o-',markevery=40, 
             label=r'$'+str('%3.0f' %(i*1e6) )+'\, \mu A$')

plt.grid(True)
leg = plt.legend(loc='center right')
leg.get_frame().set_alpha(0.5)

plt.ylim(ymin=0.0)
plt.xlim(0, 6.5)
plt.xlabel(r'$V_c\,[V]$',fontsize=14)
plt.ylabel(r'$I_c\,[mA]$',fontsize=14)
plt.title(r'$I_c=f(I_b, V_c)$',fontsize=14)
plt.savefig('param_cb.png')
plt.show()
