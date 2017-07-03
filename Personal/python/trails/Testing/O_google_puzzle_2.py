import time
from mth import *
from math import sqrt
starttime,sol = time.time(), 0
solfound = False

# Google puzzle #2, back in 2004 
"""
f (1)=7182818284  
f (2)=8182845904  
f (3)=8747135266  
f (4)=7427466391  
f (5)= __________ 
"""
# sum of digits in all number are 49

num = [7182818284, 8182845904, 8747135266, 7427466391]
l = 10 
for x in num :
	pos = e.find(str(x))
	print x, pos , isPrime(int(x)) , sumOfDigits(x)

for x in range(len(e)-l) :
	if sumOfDigits(int(e[x:x+l])) == 49 :
		print e[x:x+l] , x
	
print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	

