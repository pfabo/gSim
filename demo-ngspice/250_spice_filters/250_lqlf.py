#!/usr/bin/env python
from scipy import *
import sys

def lqlf(f,q,c2,c4, k=1, r11=0, r12=0, r3=0):
	'''
	Vypocet dolnofrekvencneho filtra LQ-LF
	
	Funkcia pracuje v dvoch modoch
	 - vypocet komponentov filtra
	 - kontrola vlastnosti filtra

	1. Vypocet komponentov filtra
	   Vstupne parametre
	     f,Q,C2,C4,K
	   Vystupne parametre
	     R11, R12, R3
	
	2. Kontrola parametrov filtra
	   Vstupne parametre
	     f,Q,C2,C4,K,R11, R12, R3
	   Vystupne parametre
	     f (vstupna hodnota f je ignorovana)
	    
	'''
	
	print '>>><<< Filter LQ-LF'
	print '       Input data '

	# priamy vypocet filra
	if r11==0:
		print '         f   = ', f, ' [Hz]'
		print '         Q   = ', q
		print '         K   = ', k
		print '         C2  = ', c2, ' [nF]'
		print '         C4  = ', c4, ' [nF]'
		
		c2=c2*1e-9
		c4=c4*1e-9
		s=1.0/(2.0*q*q)*c2/c4

		if s==2.0:
			print '>>><<< Error:'
			print '       Value C2 > ',4*q*q*c4 *1e-9, ' [nf]'
			return
		
		P=(s-1)+sqrt((s-1)*(s-1)-1)
		r1=1.0/(2*pi*f*sqrt(P*c2*c4))
		r3=P*r1
		
		if k==1:
			r11=r1
			r12=1e90
		else:
			r11=r1/k
			r12=r1/(1-k)
		
		print '       Output data'
		print '         R11 = ', r11, ' [Ohm]'
		print '         R12 = ', r12, ' [Ohm]'
		print '         R3  = ', r3, ' [Ohm]'
		return
	
	else:		# kontrola parametrov
		print '         Q   = ', q
		print '         K   = ', r12/(r11+r12)
		print '         C2  = ', c2, ' [nF]'
		print '         C4  = ', c4, ' [nF]'
		print '         R11 = ', r11, ' [Ohm]'
		print '         R12 = ', r12, ' [Ohm]'
		print '         R3  = ', r3, ' [Ohm]'
		print '       Output data'
		
		r1=r11*r12/(r11+r12)
		c2=c2*1e-9
		c4=c4*1e-9
		f=1.0/(2*pi)*1/sqrt(r1*r3*c2*c4)
		print '         f   = ', f, ' [Hz]'
		return

#=======================================================================
if __name__ == '__main__':
	
	print sys.argv[1:]

	if len(sys.argv)<5:
		print ">>><<< LQLF Filter Calculation "
		print "       For parameter calculation use "
		print "           python lqlf.py f Q C2 C4 K"
		print "       or for parameter test"
		print "           python lqlf.py f Q C2 C4 K R11 R12 R3"
		print ""
		exit(2)
	else:
		p=[0,0,0,0,0,0,0,0]
		i=0
		for x in sys.argv[1:]:
			p[i]=float(x)
			i=i+1
		if p[4]==0 : p[4]=1
		lqlf(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7])

	
