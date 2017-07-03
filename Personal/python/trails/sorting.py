# import sys
# import string
# import os
reading = ('txt' , 'pdf' , 'doc', 'docx')
watching = ('ppt' , 'ppx' , 'mov', 'avi')
# reading = ('txt' , 'pdf' , 'doc', 'docx')

import os
#from os import *
from sys import *
from shutil import *
from string import *


path="C:\Users\IBM_ADMIN\Desktop"  
watchingFolder = "C:\Users\IBM_ADMIN\Desktop\Sort_watching"
readingFodler = "C:\Users\IBM_ADMIN\Desktop\Sort_reading"
miscFolder = "C:\Users\IBM_ADMIN\Desktop\Sort_misc"

dirList = os.listdir(path)
for fname in dirList :
		dotposition = rfind(fname, ".")			#find where the last '.' is"
		type = fname[(dotposition+1):]			#extract the file extension
		if type == fname :
			pass
		else :
			if type in reading :
				copy(os.path.join(path,fname), readingFodler)
				#print fname, " copied -- succesfully"
				print str(len(fname)).rjust(2), str(fname).ljust(50), str(dotposition).rjust(5), str(type).rjust(5)
