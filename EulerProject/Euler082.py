import time
import sys
import string
from math import *
starttime,sol = time.time(), 0
solfound = False



def minimunPathMatrix(matrix):
	x = y = len(matrix)-1
	temp = matrix[x][y]
	
	#print x,y
	while not ( x == 0 and y == 0 ) :
		#on the right
		if x == 0 : 
			y -= 1	
		#on the top
		elif y == 0 : 
			x -= 1	
		else :
			if matrix[x-1][y] < matrix[x][y-1] :
				x -= 1
			else :
				y -= 1
				
	#	print matrix[x][y]
		temp += matrix[x][y]
	return temp

	
def minimunSumPathMatrixRightToLeft(matrix):
	i = l = len(matrix)

	# setting the threshold for the starting minimum value
	max_v = 0
	for a in matrix:
		if a[l-1] > max_v : 
			max_v = a[l-1]
			print 'value updated to :', max_v
			
	print "Maximum Value around these parts is", max_v
	
	start_x = 0
	x = l-1
	y = l-1
	start_v = max_v
	
	# finding the minimum element in the right column to start with 
	for a in range(0,l):
		if matrix[a][y] < start_v :
			start_v = matrix[a][y]
			start_x = a
	
	print 'The minimum value on the right is on the ', start_x+1, 'th row and is', start_v 
	
	x = start_x
	
	#Calculating the first step in the search of the most right column 
	# all elements below the minimum
	for a in range(start_x,l-1) :
		matrix[a+1][y] += matrix[a][y] 
	
	# all elements above the minimum
	for a in range(start_x,-1,-1) :
		matrix[a-1][y] += matrix[a][y] 
			
	
	y -= 1
	# for next column there will always be three ways to get a cell above, right, below
	# unless its a border cell
	temp = []
	
	#calculating step if moved from the right
	for a in matrix :
		temp.append([a[y+1] + a[y]])
	
	
	#calculating step if moved from the top
	temp[0].append(matrix[0][y])
	for a in range(1,l) :
		temp[a].append(matrix[a-1][y] + matrix[a-1][y+1])
	
	#calculating step if moved from the top
	temp[l-1].append(matrix[l-1][y])
	for a in range(l-2,-1,-1) :
		temp[a].append(matrix[a+1][y] + matrix[a+1][y+1])
	
	for a in temp : print a[0]
	
	print 'comparing[' , x, '][' , y, ']' 
	print 'above', matrix[x+1][y]
	print 'below', matrix[x-1][y]
	print 'left', temp[x], '==>', min(temp[x])
	print '='*40
	print min(matrix[x+1][y], matrix[x-1][y], min(temp[x]))
	
	"""
	while not ( x == 0 and y == 0 ) :
		
		matrix[x][y] += min(matrix[x+1][y], matrix[x][y+1])
		
		for a in range(x-1,-1,-1) :
			matrix[a][y] += min(matrix[a+1][y],matrix[a][y+1])
	
		for b in range(y-1,-1,-1) :
			matrix[x][b] += min(matrix[x+1][b],matrix[x][b+1])
		
		x -= 1
		y -= 1
	
	return matrix[0][0] + min(matrix[1][0], matrix[0][1])
	"""

test = []
f = open('matrix_1.txt', 'r')

for line in f.readlines() :
	test.append([int(x) for x in line[:-1].strip().split(',')])

sol = minimunSumPathMatrixRightToLeft(test)

print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	

# X 563261 T Unkown
# A 427337 T 7.2380001545
# A 427337 T 0.00999999046326


