# This is a few tests done in Python 
import sys
import string
import os
import zipfile
import time
from ctypes import windll
import win32api
import win32process
#import wmi
#import winshell
from win32com.client import GetObject
import mth



"""
#========== Self-reproducing Script =================
# Test 1: printing the contents of the script
#       ===========================
for line in open(sys.argv[0], 'r').readlines():
	print line.strip()
#============================================
"""
"""
#========== Home Directory Listing and zipping important files =================
Folders = [ 'C:/Users/IBM_ADMIN/SametimeTranscripts',
			'C:/Users/IBM_ADMIN/Downloads',
			'C:/Users/IBM_ADMIN/Desktop',
			'C:/Users/IBM_ADMIN/Documents',
		]
fname = 'listofinterestingfiles'
f = open( fname + '.txt', 'w')
for a in Folders :
	for root, dirs, files in os.walk(a):
		for name in files:
			f.write( os.path.join(root, name) + '\n')
		for name in dirs:
			f.write( os.path.join(root, name) + '\n')
f.close()
zipfileobj = zipfile.ZipFile(fname + '.zip','w')
zipfileobj.write(fname + '.txt', fname + '.txt', zipfile.ZIP_DEFLATED)
zipfileobj.close()
#========== Home Directory Listing and zipping important files =================

count = 0
#========== Printing Primes between 60000 and 63000 =================
for x in range(60001,63999,2) :
	if count == 7 : 
		count = 0
		print
	if mth.isPrime(x) : 
		count += 1
		print x, '\t',
	
"""


print 
print
print '*'*40
#for x in dir(win32api) : print x
print '*'*40
print '*'*40
print 'Please insert the USB'
print string.uppercase
bitmask = windll.kernel32.GetLogicalDrives()

for letter in string.uppercase:
	print bitmask, bitmask & 1, 
	if bitmask & 1:
		print letter,
	print
	bitmask >>= 1
		
print '*'*40
print '*'*40
win32api.Beep(1000, 1000)
win32api.Beep(2000, 1000)
win32api.Beep(3000, 1000)
win32api.Beep(4000, 1000)
print win32api.GetCommandLine()
print win32api.GetComputerName()
for x in range(5) : 
	print win32api.GetCursorPos() 
	time.sleep(0.1)

print win32api.GetCursorPos()
print win32api.GetLogicalDriveStrings()
print win32api.GetPwrCapabilities()
print win32api.GetSysColor(2)
print win32api.GetSystemInfo()
print win32api.GetSystemTime()
print win32api.GlobalMemoryStatus()
print win32process.EnumProcesses()

WMI = GetObject('winmgmts:')
processes = WMI.InstancesOf('Win32_Process')
process_list = [(p.Properties_("ProcessID").Value, p.Properties_("Name").Value) for p in processes]
for proc in sorted(process_list): print proc
