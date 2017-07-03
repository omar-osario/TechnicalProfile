from os import *
from shutil import *
from math import *
import time
starttime,sol = time.time(), 0

def nextCollatz(n):
	if (n%2 == 0):
		return n/2
	else :
		return (3*n + 1)

# Setting dictionary
# Collatz = {number:length of Collatz chain} 
Collatz = {1:0}

# Adding elements given from question
Collatz[2] = 1
Collatz[4] = 2
Collatz[8] = 3
Collatz[16] = 4
Collatz[5] = 5
Collatz[10] = 6
Collatz[20] = 7
Collatz[40] = 8
Collatz[13] = 9

# Setting the Largest Element we know
largestChainElement = 13
largestChainLength = Collatz[largestChainElement] ; 

# Setting the upper limit
MaxNumber = 1000000 
for element in range(3,MaxNumber):
	
	CurrentNumber = element
	rounds = 0 
	
	# Counting the rounds till the first known elements 
	while ( CurrentNumber not in Collatz):
		rounds += 1
		CurrentNumber  = nextCollatz(CurrentNumber)
	
	# If element already in the Collatz dictionary then no action needed 
	if (rounds==0):
		continue ; 
	# If element isnt then add element to dictionary 
	else :
		CollatzLength = Collatz[CurrentNumber] + rounds 
		Collatz[element] = CollatzLength
		# Test if element has a longer chain 
		if ( CollatzLength > largestChainLength ):
			largestChainElement = element
			largestChainLength = CollatzLength ;


#print(largestChainElement,":" ,largestChainLength)
sol = largestChainElement

#sol = largestChainElement
#x = 16 
#print(x,":" ,Collatz[x])

print ('*'*40)	
print ("**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime))
print ('*'*40)
# (True,837799,6.017688035964966)