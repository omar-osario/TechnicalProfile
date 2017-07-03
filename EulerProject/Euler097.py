import time 
from math import pow
starttime = time.time()
solfound,sol = False, 0

# 2**32 = 4294967296 ( 10 digits long )

# the first 10 digits repeat every 7812500 numbers

start = 4294967296
upperlimit = 7830457 + 1 - 7812500
temp = start
for x in xrange(33,upperlimit):
	if x % 128 == 0 : temp %= 10**10
	temp *= 2
sol = str((temp*28433) + 1)[-10:]

print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# X 7479985153 T 11.9889998436
# X 4484175873 T 1.2380001545
# A 8739992577 T 2.35700011253
# A 8739992577 T 2.31599998474
# A 8739992577 T 2.3029999733
# A 8739992577 T 2.28600001335
# A 8739992577 T 0.0090000629425

