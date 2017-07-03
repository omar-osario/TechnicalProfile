# import sys
# import string
# import os


from os import *
from sys import *
from shutil import *
from string import *

# listdir = os.listdir
path="C:\\Users\\IBM_ADMIN\\Desktop"  

dirList = listdir(path)
for fname in dirList :
	dotposition = rfind(fname, ".")			#find where the last '.' is"
	type = fname[(dotposition+1):]			#extract the file extension
	if type != fname :
		print str(len(fname)).rjust(2), str(fname).ljust(40), str(dotposition).rjust(5), str(type).rjust(5)
	else :
		print fname, " is a folder"
		pass
