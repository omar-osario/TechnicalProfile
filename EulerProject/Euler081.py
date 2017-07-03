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

	
def minimunSumPathMatrix(matrix):
	x = len(matrix)-1
	y = len(matrix[0]) -1
	
	# starting at the element in the bottom right corner
	temp = matrix[x][y]
	
	
	for a in range(x,0,-1) :
		matrix[a-1][y] += matrix[a][y] 
			
	for b in range(y,0,-1) :
		matrix[x][b-1] += matrix[x][b] 
	
	x -= 1
	y -= 1
	
	while not ( x == 0 and y == 0 ) :
		
		matrix[x][y] += min(matrix[x+1][y], matrix[x][y+1])
		
		for a in range(x-1,-1,-1) :
			matrix[a][y] += min(matrix[a+1][y],matrix[a][y+1])
	
		for b in range(y-1,-1,-1) :
			matrix[x][b] += min(matrix[x+1][b],matrix[x][b+1])
		
		x -= 1
		y -= 1
	
	return matrix[0][0] + min(matrix[1][0], matrix[0][1])

test = []
f = open('matrix.txt', 'r')

for line in f.readlines() :
	test.append([int(x) for x in line[:-1].strip().split(',')])

sol = minimunSumPathMatrix(test)

print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	

# X 563261 T Unkown
# A 427337 T 7.2380001545
# A 427337 T 0.00999999046326


