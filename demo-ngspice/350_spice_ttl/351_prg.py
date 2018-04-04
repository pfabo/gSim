import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('351_circ.sch')

t = data['time']*1e9
vin = data['v(in)']
vout = data['v(out)']

plot(t,vin, label='Vin')
plot(t,vout, label='Vout')
xlabel('Time [ns]')
ylabel('Vin, Vout [V]')
ylim(0, 5.5)
grid()
legend()
savefig('351_ttl.png')
#show()

