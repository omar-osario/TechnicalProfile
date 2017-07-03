import time
import sys
import string
from math import *
starttime,sol = time.time(), 0
def distanceBetweenPointsGrid(l, m):
	if l[0] == m[0] or l[1] == m[1]:
		return 2*sqrt((l[0]-m[0])**2 + (l[1]-m[1])**2) -1
	if l[0] > m[0]:
		x_factor = -0.5
	else :
		x_factor = 0.5
	if l[1] > m[1]:
		y_factor = -0.5
	else :
		y_factor = 0.5 
	return 2*sqrt((l[0]-m[0] + x_factor)**2 + (l[1]-m[1] + y_factor)**2)
	
location = [1, 1]
gridsize = [3, 3]

directions = 2*(gridsize[0]+gridsize[1] -2)
righttangles = [ 0, 90 , 180, 270 ]
halfrightangles = [ x + 45 for x in righttangles ]

for x in range(gridsize[0]):
	for y in range(gridsize[1]):

borderpoints = []

grid = [['#', '#', '#'], ['#', 'X', '#' ],[ '#', '#' ,'#' ]]
border_x = False
border_y = False

for x in range(gridsize[0]):
	for y in range(gridsize[1]):
		border_x = x == 0 or x == gridsize[0] - 1:
		border_y = y == 0 or y == gridsize[1] - 1:
		if border_x and border_y:
			x_opposite = (x + gridsize[0] - 1)% (gridsize[0] +1)
			y_opposite = (x + gridsize[0] - 1)% (gridsize[0] +1)

		if grid[x][y] == '#':
			grid[x][y] = distanceBetweenPointsGrid(location, [x, y])

for x in grid:
	print x

	


cellvalue = 1.0
print sqrt(.5**2 + 1.5**2)
#file_1 = open('B-large.in','r')
#file_2 = open('GJ_2_sol_L.txt', 'w')
#numoflines = int(file_1.readline())	
	
#for x in range(numoflines):
#	print >> file_2, "Case #{0}: {1}".format(x+1, str(googleDancers(file_1.readline().strip())).strip())




print "================================================================"	
print "Answer ", sol, "found in", time.time() - starttime
print "================================================================"	