
from os import *
from shutil import *
from string import *

sum = 0 ; 
for x in range(3,1000,3):
	if x % 5 != 0 :
		sum += x	

for x in range(5,1000,5):
	sum += x
	
print(sum)