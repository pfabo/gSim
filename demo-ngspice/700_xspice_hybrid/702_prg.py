import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('702_circ.sch')
print(desc['varnames'])

t = data['time']*1000
vout = data['v(out)']
vc = data['v(in-)']
plot(t,vout, label='OUT')
plot(t,vc, label='Vc')
xlim(0, t[-1])
grid()
legend(loc='upper right')
savefig('702_img.png')
#show()



