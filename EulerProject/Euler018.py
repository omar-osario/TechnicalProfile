import time
starttime,sol = time.time(), 0
from math import *

# the # of possible route is 2**(n-1) where n is the number of levels in the pyramid


"""
def findPyramidSum(level,index,array):
	if level < len(array):
		print array[level+1][index],  array[level+1][index +1]
	#	return array[level+1][index],  array[level+1][index +1]
	return -1

def calculatePyramidSum(level,index,array, sumarray):
	if level < len(array):
		sumarray[level+1][index] = array[level+1][index]
		sumarray[level+1][index +1]  array[level+1][index +1]
	#	return array[level+1][index],  array[level+1][index +1]
	return -1

"""

test = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

def checkHighPointAbove(n):
	inc = 0
	numofpoints	= 0 
	level, order = [], []
	edgepoint = special = False
	if n[1] == 0 :
		level = range(n[0])
		order = [0]
		edgepoint = True 
	if n[1] == n[0]:
		#order = [n[1] - 1]  
		level = range(n[0])
		edgepoint = special = True 

	if edgepoint == False :
		level = range(n[1]+1)
		order = range(n[1]+1)
	if not special :
		print level, "------------",  order 
		for x in level:
			for y in order:
				print x, y
				if test[x][y] > 6:
					numofpoints += 1
					n[3] += 1
			inc += 1
			
	else : 
		print level, "------------",  order 
		for x in level:
			print x, x
			if test[x][x] > 6:
				numofpoints += 1
				n[3] += 1
			inc += 1
	
	
	print order
	return order, numofpoints
#for x in range(level-1,-1, -1):
#	if orderlow == 1 :
#	for y in range(orderlow,orderhigh):

	
#test = [[3], [7, 6], [4, 4, 5], [8, 5, 9, 4], [7, 8, 1, 5, 9]]

potentialpoints = []

for x in range(len(test)-1,-1, -1):
	for y in range(0,x):
		#print "testing",  test[x][y], '/t',  test[x][y+1]
		if test[x][y] > test[x][y+1]:test[x-1][y] += test[x][y]
		else : test[x-1][y] += test[x][y + 1]

sol = test[0][0]
print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# A 1070 - wrong
# A 1074 - right manual
# .15700006485
#0.00200009346008