import time
from mth import *
from gen import *
from math import sqrt
starttime,sol = time.time(), 0
solfound = False

"""
IMO 1960 Problem 01 :
Determine all three-digit numbers N having the property that N is divisible by 11, and N/11 is equal to the sum of the squares of the digits of N.

IMO 1962 Problem 01
Find the smallest natural number n which has the following properties:
	(a) Its decimal representation has 6 as the last digit.
	(b) If the last digit 6 is erased and placed in front of the remaining digits, the resulting number is four times as large as the original number n.

IMO 1963 Problem 06
Five students, A,B,C,D,E, took part in a contest. One prediction was that the contestants would finish in the order ABCDE. This prediction was very poor. In fact no contestant finished in the position predicted, and no two contestants predicted to finish consecutively actually did so. A second prediction had the contestants finishing in the order DAECB. This prediction was better. Exactly two of the contestants finished in the places predicted, and two disjoint pairs of students predicted to finish consecutively actually did so. Determine the order in which the contestants finished.
"""

#problem 1 : 
sol_1 = []
for i in range(1,91):
	temp_n = str(i*11)
	temp_sum = 0
	for x in temp_n:
		temp_sum += int(x)**2
	if i == temp_sum : sol_1.append(i*11)
print 'Solution 1:', sol_1	
	
#problem 2 :
sol_2 = ''
for i in xrange(1000000):
	temp_1 = str('6'+str(i))
	temp_2 = str(i)+'6'
	#print temp_1, temp_2
	if int(temp_1) == 4*int(temp_2) :
		sol_2 = str(i)+'6'
		break
print 'Solution 2:', sol_2	

	
#problem 3 :
letters = 'abcde'
pred_1 = 'abcde'
pred_2 = 'daecb'
pred = []

# Generating all possibilities 
for i in letters  :
	for j in letters :
		if i == j : continue 
		for k in letters :
			if k == i or k ==j :continue
			for l in letters :
				if l == i or l ==j or l==k :continue
				for m in letters :
					if m == i or m ==j or m==k or m== l:continue
					pred.append([i+j+k+l+m, True])


# checking against the first prediction
# no contestant finished in the position predicted

for x in pred :
	for y in range(len(pred_1)) :
		if x[0][y] == pred_1[y] : 
			x[1] = False
			continue

# no two contestants predicted to finish consecutively actually did so
for x in pred :
	if not x[1] : continue 
	for y in range(len(letters)-1):
		if pred_1[y:y+2] in x[0] :
			x[1] = False
			continue

# Checking against the second prediction 

# Exactly two of the contestants finished in the places predicted	
for x in pred :
	if not x[1] : continue
	temp = 0 
	for y in range(len(pred_2)) :
		if x[0][y] == pred_2[y] :
			temp += 1
	if temp < 2 : x[1] = False

# Two disjoint pairs of students predicted to finish consecutively actually did so
for x in pred :
	if not x[1] : continue
	temp = 0 
	for y in range(len(pred_2)-1) :
		if pred_2[y:y+2] in x[0] :
			temp += 1
	if temp < 2 : x[1] = False


# Deleting the Conditions
for x in pred :
	if not x[1]: continue
	if x[0] == pred_1 or  x[0] == pred_2 :
		x[1] = False
		continue
# Printing solution

for x in pred : 
	if x[1] :
		sol_3 = x[0]
		
print 'Solution 3:', sol_3	
	

print '*'*65
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print '*'*65


