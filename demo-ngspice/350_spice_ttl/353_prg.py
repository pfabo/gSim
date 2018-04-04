import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('353_circ.sch')
#print(desc['varnames'])

vin = data['v(in)']
vout = data['v(out)']
plot(vin,vout, label='Vin')
xlabel('Vin')
ylabel('Vout')
ylim(0,10)
grid()
savefig('353_cmos.png')
#show()

