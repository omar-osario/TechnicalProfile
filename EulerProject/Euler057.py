import time
import sys
import string
starttime,sol = time.time(), 0


n_past, d_past = 1,2
n_new, d_new = 1, 2

for x in range(1,1000):
	n_new = d_past
	d_new = 2*d_past + n_past
	
	if len(str(n_new + d_new)) > len(str(d_new)): sol += 1
	n_past = n_new
	d_past = d_new
	
print
print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
#0.0090000629425
#0.00799989700317