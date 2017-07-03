import time
starttime,sol = time.time(), 0
def isPandigital(n):
	for x in range(1,10):
		if not str(x) in n: return False
	return True

for x in range(9499,8999,-1):
	if isPandigital(str(x) + str(x*2)):
		sol = int(str(x) + str(x*2))
		break

	
print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# A 932718654 T 0.0