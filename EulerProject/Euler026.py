from os import *
from shutil import *
from string import *
import time
from decimal import Decimal


starttime = time.time()

for x in range(1,50,2):
	print float(1.0/x)

print Decimal(1.0/9.0)

print "Execution time ", time.time() - starttime