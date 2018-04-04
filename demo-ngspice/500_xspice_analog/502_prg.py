import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('502_circ.sch')
'''
vname = desc['varnames']
vunit = desc['varunits']
print('name', ' \t', desc[b'plotname'])
print('vars', ' \t', int(desc[b'no. variables']))
print('no.', ' \t', int(desc[b'no. points']))
print('var', '\t|', 'unit')
print('---------------------------------------')
for i in range(len(vname)):
    print(vname[i], '\t|', vunit[i])
'''

t = data['time']
vz = data['v(z)']
vy = data['v(y)']
vx = data['v(x)']

graph=[subplot(211),subplot(212)]

graph[0].plot(t,vz, label='Z')
graph[0].plot(t,vy, label='Y')
graph[0].plot(t,vx, label='X')
graph[0].set_xlim(0, t[-1])
graph[0].grid()
graph[0].legend(loc='upper right')

graph[1].plot(vy,vx, 'r-', label='X-Z')
graph[1].grid()
graph[1].legend(loc='upper right')
savefig('502_img.png')
#show()
