##
#	This script is made to make sure that change notifications are sent at most every
#	hour, this is done by creating and empty file that has the time of the last change
#	in th name (Epoch time), and then every other change is compared to that time.
#	if time is more than one hour then anothe email is sent 
#
#
##
#!/usr/bin/python

import os
import re
import sys
from  time import *

# Edit this to edit time before sending next email in seconds ( 3600 to set to one hour)
timeBeforeSendingEmail = 5

#timestamp file extension
timestampEstension = ".timestamp" 
timeInFilename = strftime("%Y%m%d-%H%M%S")
timeInEpoch = int(time())

logDirectory = "C:\\Users\\IBM_ADMIN\Documents\\Scripting\\Python" + "\\ts"
TimeFilename = ""
"""
print logDirectory 
if os.path.exists(logDirectory) :
	print "Log Folder found" 
else :
	print "Log Folder not found and will be created"
	os.mkdir(logDirectory)
"""
	
	
opt = {}
try:
	count = 1
	
	# Go through each argument
	
	while count <= (len( sys.argv ) - 1 ):
		# See if the current arguement is in the list of switches

		for switch in [ "-env", "-app", "-help" ]:
			if sys.argv[ count ] == "-help":
				raise
			if sys.argv[ count ] == switch:
				opt[ switch[1:] ] = sys.argv[ ( count + 1 ) ]

		count += 1
	
	if opt[ "env" ] == None: 
		raise
	
	if opt[ "app" ] == None: 
		raise

except:
  # If an exception is raised in the try ... 
	print
	print "USAGE: " + sys.argv[ 0 ] + " -env <environment name> -app <application name>"
	print
	print "You need to execute this program with with the -env and -app arguments "
	print "This script will exit without updating the time"

	sys.exit()

applicationName = opt[ "app" ]
enviromentName = opt[ "env" ]
#directory on where the timestamp should reside 



# Get the time stampfile
for fname in os.listdir(logDirectory):
	fileDetails = fname.split('_')
	#print "File ::: ", fname #debugging
	if len(fileDetails) == 3 :
		#print fileDetails[0], fileDetails[1] #debugging
		if fileDetails[0] == applicationName and fileDetails[1] == enviromentName :
			#print "File Found" #debugging
			TimeFilename = fname  
			break 


# if file is not existent, then create it 
if TimeFilename == "" :
	print "File Created" #debugging
	TimeFilename = applicationName + "_" + enviromentName + '_' + timestampEstension
	TimeFile = open(os.path.join(logDirectory,TimeFilename), "w")
	TimeFile.write(str(timeInEpoch)) 
	TimeFile.write(str("\nLast updated on:" + strftime("%Y-%m-%d %H:%M:%S"))) 
	TimeFile.close()

#if file is there, check for time difference, if all is good, store new time otherwise do nothing
else :
	TimeFile = open(os.path.join(logDirectory,TimeFilename), "r")
	tempTimeValue = int(TimeFile.readline())
	TimeFile.close()
	if timeInEpoch - tempTimeValue > timeBeforeSendingEmail + 1:
		print "Time value updated" #debugging
		TimeFile = open(os.path.join(logDirectory,TimeFilename), "w")
		TimeFile.write(str(timeInEpoch)) 
		TimeFile.write(str("\nLast updated on:" + strftime("%Y-%m-%d %H:%M:%S"))) 
		TimeFile.close()
	else :
		print "Not Enough time has passed" #debugging
