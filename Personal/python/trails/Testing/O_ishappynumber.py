import time
from mth import *
from gen import *
from math import sqrt
starttime,sol = time.time(), 0
solfound = False

"""
A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers (or sad numbers).
"""

def isHappyNumber(n):

	temp_sum = []
	temp_str= str(n)
	while True:
		temp = 0
		for i in temp_str :
			temp += int(i)**2
		
		# Happy Number 
		if temp == 1 : 	return True
		
		# Sad Number 
		if temp in temp_sum : return False

		#Add the number to the Chain
		temp_sum.append(temp)
		
		temp_str = str(temp)
		

for x in range(0,1000) :
	if isHappyNumber(x) :
		print x , (x%2 == 0) 
print '='*40	
			
print '*'*65
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print '*'*65


