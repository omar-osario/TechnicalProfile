import time
from mth import *
from gen import *
from math import sqrt
starttime,sol = time.time(), 0
solfound = False

"""
A mathematician purchased four items in a grocery store. He noticed that when he added the prices of the four items, the sum came to $7.11, and when he multiplied the prices of the four items, the product came to $7.11.
"""
res = 7.11
res_s = 712


# Assume all item prices are in the x.xx format

for a in range (res_s,1,-1) :
	if solfound : break
	print '\rChecking', a , '\b...' 
	for b in range (res_s-a+1,1,-1) :	
		print '\r',b,
		if float(a)/100.0 * float(b)/100.0 > res : break
		for c in range (res_s-(a+b)+1,1,-1) :
			if float(a)/100.0 * float(b)/100.0 * float(c)/100.0 > res : break
			for d in range (res_s-(a+b+c)+1,1,-1):
				if (a+b+c+d) == res_s :
					if (float(a)/100.0*float(b)/100.0*float(c)/100.0*float(d)/100.0) == res :
						sol = [a,b,c,d]
						solfound = True
					
				
print '*'*65
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print '*'*65
# from 0 the solution is generated in 426.761000156
# from 711 the solution is generated in 0.406000137329

