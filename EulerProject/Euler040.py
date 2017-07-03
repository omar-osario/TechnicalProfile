
import time
from sets import Set
from math import *
starttime = time.time()

digitbase = [0, 10, 190, 2890, 38890, 488890, 5888890]



sol = 1
temparray = ""

for x in range(0,1000000):
	temparray += str(x)

for x in range(0,7):
	sol *= int(temparray[10**x])


#sol = 1
print "Answer ", sol, "found in", time.time() - starttime
#2.1970000267