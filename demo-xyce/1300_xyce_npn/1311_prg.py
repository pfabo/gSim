#!/usr/bin/env python
import sys
sys.path.append('../../py')

import pylab as plt 
from gsim import *

fileName='1311'
gx = gSim(fileName+'_circ.sch', 'XYCE')
gx.netlist()

for i in arange(10e-6, 1e-7, -1e-6):
    gx.setPAR('IB',i)
    data, param = gx.sim()
    ic = -data['V1#branch']*1e3
    vc = data['C']
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
plt.savefig(fileName+'_img.png')
#plt.show()
