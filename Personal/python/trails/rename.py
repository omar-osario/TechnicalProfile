import os
from gen import *
from string import *


path ='C:/Users/IBM_ADMIN/Documents/Scripting/Python'
line = 100

print '*'*line

for fname in sorted(os.listdir(path)):
	if os.path.isdir(fname) : 	# Directory test
		
		# Enter Condition Here
		if True :
			pass
			
	else:						# File test
		# Getting name and extension
		dotposition = rfind(fname[::-1], ".")
		name = fname[:-dotposition-1]
		ext = fname[len(fname)-dotposition:]
		
		# Enter Condition Here
		if name[:2] == 'O_' : 
		
		# Enter Result Here
			newname = name[2:] + '.' + ext
			os.rename('/'.join((path,fname)), '/'.join((path,newname)))

