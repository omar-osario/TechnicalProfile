from __future__ import print_function
import os
import sys

def factorial(n):
    if n == 0 or n==1 :
        return 1
    else:
        return n * factorial(n-1)

def factorial_sub(n,m): #return partial factorial 
	res = n 
	while m > 0 :
		n 		-= 	1
		m 		-= 	1 
		res 	*= 	n 
	return res 

def number_faces(d,k):
		# Hypercube dimension d
		# face dimension k ( k=0 -> corner, k=1 -> edge, k=2 => face ..etc )
		
		# if we just want to figure out number of vertices  k = 0
		if k == 0 : return pow(2,d)
			
		# if we just want to figure out number of lines k = 1
		if k == 1 : return pow(2,d-1)*d
			
		# if we just want to figure out number of faces k = 2
		if k == 2: return pow(2,d-3)*d*(d-1)
			
		# Straight forward answer 
		if d == k : return 1
			
		# Straight forward answer 
		if d -1 == k : return 2*d
		
		# General equation
		return pow(2, d-k)*factorial_sub(d,k-1)/factorial(k)

#creating an hash for storing the result for future comparing 
dimensionFaces = {}
num_of_sol = 0 
x = 1 

# While we don't have at least 10 solutions keep going
while num_of_sol < 10 :			

	# loop through the face dimensions 0,1,2 , vertex, line and face respectively 
	for y in range (0,x+1) :
		
		# Storing the [x,y] pair 
		pair = [x,y] 
		
		# Skip trivial answers that don't classify as a solution 
		if x == y : 
			continue 
			
		# Getting the number of y-dimensional faces in an x-dimensional hypercube
		temp = int(number_faces(x,y))
		
		# Store the pair in the hash where the key is number y-dimensional faces in an x-dimensional hypercube
		if temp in dimensionFaces :
			# add the pair to the hash 
			dimensionFaces[temp].append(pair)
			
			# if more that 2 pair exist then print out solution 
			if len(dimensionFaces[temp]) > 2 :
				print ( "Solution :"  + str(dimensionFaces[temp]))
				num_of_sol += 1
				
		else :
			dimensionFaces[temp] = [pair]
		
	x += 1 
