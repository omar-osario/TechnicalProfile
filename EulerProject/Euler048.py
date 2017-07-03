
import time
from sets import Set
from math import *
starttime,sol = time.time(), 0

tempint = 0
for x in range(1,101):
	tempint += x**x
sol = str(tempint)[-10::]

print "Answer ", sol, "found in", time.time() - starttime
#0.0119998455048
#0.00100016593933