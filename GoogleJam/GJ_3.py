import time
import sys
import string
starttime,sol = time.time(), 0

def isRecycledPair(n, m):
	temp = str(n)
	for x in range(1,len(str(n))):
		newtemp  = int(temp[-x::] + temp[0:-x])
		if newtemp == m:
			return True
	return False
	
def recyclePairs(lower, upper):
	result = []
	test = ""
	for x in range(lower, upper+1):
		temp = str(x)
		for x in range(1,len(str(x))):
			newtemp  = int(temp[-x::] + temp[0:-x])
			#print "testing ", temp, newtemp
			if newtemp > lower and newtemp < upper :
				if int(temp) < newtemp :
					if len(temp) == len(str(newtemp)):
						#print temp, newtemp
						result.append([int(temp), newtemp])
	return len(result)
		


file_1 = open('C-small-attempt0.in-1.txt','r')
file_2 = open('GJ_3_sol.txt', 'w')
numoflines = int(file_1.readline())	
	



for x in range(numoflines):
	limits = file_1.readline().split(" ")
	lower = int(limits[0])
	upper = int(limits[1])
	print >> file_2, "Case #{0}: {1}".format(x+1, str(recyclePairs(lower, upper)))
	#print >> file_2, "Case #{0}: {1}".format(x+1, str(googleDancers(file_1.readline().strip())).strip())




print "================================================================"	
print "Answer ", sol, "found in", time.time() - starttime
print "================================================================"	