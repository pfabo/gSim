import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('701_circ.sch')

#print(desc['varnames'])

t = data['time']*1000
vout = data['v(out)']
vcap = data['v(trig)']

plot(t,vout, label='OUT')
plot(t,vcap, label='CAP')
xlim(0, t[-1])
grid()
legend(loc='upper right')
savefig('701_img.png')
#show()



