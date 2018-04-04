import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('700_circ.sch')
print(desc['varnames'])

t = data['time']*1000
vout = data['v(out)']
vcap = data['v(cap)']

plot(t,vout, label='OUT')
plot(t,vcap, label='CAP')
xlim(0, t[-1])
grid()
legend(loc='upper right')
savefig('700_img.png')
#show()



