import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('352_circ.sch')
#print(desc['varnames'])

t = data['time']*1e9
vin = data['v(in)']
vout = data['v(out)']

plot(t,vin, label='Vin')
plot(t,vout, label='Vout')
xlabel('Time [ns]')
ylabel('Vin, Vout [V]')
grid()
legend()
savefig('352_img.png')
#show()

