import sys
sys.path.append('../../py')

from pylab import *
from gsim import *

data, desc = gs('503_circ.sch')
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
f = data['frequency'].real
d1 = abs(data['v(b1)'])
d2 = abs(data['v(b2)'])
d3 = abs(data['v(b3)'])
d5 = abs(data['v(b5)'])

c2 = abs(data['v(c2)'])
c3 = abs(data['v(c3)'])
c5 = abs(data['v(c5)'])
c6 = abs(data['v(c6)'])

graph=[subplot(211),subplot(212)]

graph[0].semilogx(f,d1, label='B1')
graph[0].semilogx(f,d2, label='B2')
graph[0].semilogx(f,d3, label='B3')
graph[0].semilogx(f,d5, label='B5')
graph[0].grid()
graph[0].legend(loc=3)

graph[1].semilogx(f,c2, label='C2')
graph[1].semilogx(f,c3, label='C3')
graph[1].semilogx(f,c5, label='C5')
graph[1].semilogx(f,c6, label='C6')
graph[1].grid()
graph[1].legend(loc=3)
graph[1].set_xlabel('Frequency [norm]')
savefig('503_img.png')
#show()
