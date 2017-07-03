import time
from sets import Set
starttime = time.time()

sum = 1 
x = range(2,101)
temp = []

for a in x :
	temp.append([])
	for b in x :
		temp[a-2].append(a**b)
	#asdas
	
result = []
for y in temp:
	for z in y :
		result.append(int(z))

if result:
    result.sort()
    last = result[-1]
    for i in range(len(result)-2, -1, -1):
        if last == result[i]:
            del result[i]
        else:
            last = result[i]
	
#print result	
print len(result)	
print "Execution time ", time.time() - starttime