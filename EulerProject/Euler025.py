"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =  0.5 
1/3 =  0.(3) 
1/4 =  0.25 
1/5 =  0.2 
1/6 =  0.1(6) 
1/7 =  0.(142857) 
1/8 =  0.125 
1/9 =  0.(1) 
1/10 =  0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from math import *
from decimal import *
import time
starttime,sol = time.time(), 0

def properDivisors(n):
#does not work for numbers less than 10	

	lowfactors = []
	upperlimit = int(sqrt(n))
	  
	for x in xrange(2,upperlimit+1) :
		if n%x == 0:
			lowfactors.append(x)
	
	if lowfactors == [] :
		return [0 , 1]
	
	if upperlimit**2 == n :
		highfactors = [ n/x for x in lowfactors[:-1] ]	
	else :	
		highfactors = [ n/x for x in lowfactors ]	
	
	return [1] + lowfactors + highfactors[::-1]
"""
for i in range(2,11):
	tempstr = str(Decimal(1.0)/Decimal(float(i)))
	print i, tempstr[2:]
print 
"""
#resarch if number devides by 2 and 5 then its a terminating decimal

potential = []

for i in range(11,1001):
	if properDivisors(i)[0] == 0:
		print i, properDivisors(i)
		potential.append(i)
		
for x in potential:
	print x , Decimal(1.0)/Decimal(x)

	
print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# WA 76 T 0.0520000457764
# WA 983 with reaserach not programming 


