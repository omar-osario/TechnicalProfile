import time
starttime,sol = time.time(), 0

def isPandigital(n):
	for x in range(1,10):
		if not str(x) in n: return False
	return True
	
ans = []
for x in range(1,1000):
	for y in xrange(1,1000000/x):
		temp = x*y
		if temp > 987654321: break
		tempx = str(x) + str(y) + str(temp)
		if len(tempx) > 9: break
		if isPandigital(tempx) : 
			if not temp in ans : ans.append(temp)
			print x, y, temp

sol =  sum(ans)

print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"		
# A 45228 T 24.5050001144 
# A 45228 T 0.291000127792 
# A 45228 T 0.207000017166





