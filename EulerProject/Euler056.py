import time
#from math import sqrt
#from collections import Counter
starttime = time.time()
solfound,sol = False, 0

def sumOfDigitis(n):
	temp = str(n)
	sum = 0 
	for x in temp: sum += int(x)
	return sum

powers = range(95,100) 
numbers = range(95,100) 

for n in numbers:
	for p in powers:
		if sumOfDigitis(n**p) > sol :sol = sumOfDigitis(n**p)
			#print n, p , sumOfDigitis(n**p)



print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# 972 T .00999999046326






