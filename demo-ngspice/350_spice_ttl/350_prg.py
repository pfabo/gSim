import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('350_circ.sch')
#print(desc['varnames'])

vin = data['v(in)']
vout = data['v(out)']
xlim(0,5.1)
ylim(0,5.1)
xlabel('Vin [V]')
ylabel('Vout [V]')
title('TTL Gate')
plot(vin,vout)
grid()
savefig('350_ttl.png')
#show()


