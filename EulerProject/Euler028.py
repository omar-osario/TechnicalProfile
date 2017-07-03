
#from os import *
#from string import *
import time
starttime = time.time()

sum = 1 
for x in range(3,1002,2) :
	sum += 4*x**2 - 6*x + 6
print sum

print "Execution time ", time.time() - starttime