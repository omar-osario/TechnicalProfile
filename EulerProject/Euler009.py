#Answer is 31875000

from os import *
from shutil import *
from math import *
import time
starttime = time.time()

SUITPRIMES = [2, 3, 5, 7]
primativePythagorean = [[3, 4, 5], [5, 12, 13], [7, 24, 25], [8, 15, 17], [9, 40, 41], [11, 60, 61], [12, 35, 37], [13, 84, 85], [16, 63, 65], [20, 21, 29], [28, 45, 53], [33, 56, 65], [36, 77, 85], [39, 80, 89], [48, 55, 73], [65, 72, 97],[20, 99, 101], [60, 91, 109], [15, 112, 113], [44, 117, 125], [88, 105, 137], [17, 144, 145], [24, 143, 145], [51, 140, 149], [85, 132, 157], [119, 120, 169], [52, 165, 173], [19, 180, 181], [57, 176, 185], [104, 153, 185], [95, 168, 193], [28, 195, 197], [84, 187, 205], [133, 156, 205], [21, 220, 221], [140, 171, 221], [60, 221, 229], [105, 208, 233], [120, 209, 241], [32, 255, 257], [23, 264, 265], [96, 247, 265], [69, 260, 269], [115, 252, 277], [160, 231, 281], [161, 240, 289], [68, 285, 293], [207, 224, 305], [273, 136, 305], [25, 312, 313], [75, 308, 317], [253, 204, 325], [323, 36, 325], [175, 288, 337], [299, 180, 349], [225, 272, 353], [27, 364, 365], [357, 76, 365], [275, 252, 373], [135, 352, 377], [345, 152, 377], [189, 340, 389], [325, 228, 397], [399, 40, 401], [391, 120, 409], [29, 420, 421], [87, 416, 425], [145, 408, 433], [437, 84, 445], [31, 480, 481]]

def isPrime(n):
	
	for x in SUITPRIMES :
		if n == x :
			return -1

	for x in SUITPRIMES :
		if n%x == 0 :
			return x
	
	upperlimit = int(sqrt(n))	
	
	for x in xrange(9,upperlimit +1,2) :
		if n%x == 0:
			return x 
	else :
		return -1

def findFactors(n):
	
	lowfactors = []
	highfactors = []
	print "The number i :", n
	upperlimit = int(sqrt(n))
	
	for x in SUITPRIMES :
		if n%x == 0:
			lowfactors.append(x)
			highfactors.append(n/x)
		
	for x in xrange(9,upperlimit +1,2) :
		if n%x == 0:
			lowfactors.append(x) 
			highfactors.append(n/x)
			
	if lowfactors == [] :
		return -1
	
	return lowfactors + highfactors[::-1]

def checkPalindromic(n):
	strnum = str(n)
	numofdigits = len(strnum)
	
	for x in range(0, numofdigits/2):
		if strnum[x] != strnum[numofdigits - x - 1]:
			# print strnum[0],  strnum[numofdigits - x - 1]
			
			return -1
	print numofdigits		
	return 1

soultionfound = 0 
tempvalues = []
tempmultiplayer = 0
result = 1 
	
for x in primativePythagorean :
	for y in range (1, 50) :
		temp = sum(x)*y
		if temp == 1000 :
			print "Bingo, the Pythagorean values are ", x, " and it multiplied by ", y
			soultionfound = 1 
			tempvalues = x
			tempmultiplayer = y
			break
	if soultionfound == 1:
		break 

for x in tempvalues:
	result *= x*tempmultiplayer

print result
print "Execution time ", time.time() - starttime