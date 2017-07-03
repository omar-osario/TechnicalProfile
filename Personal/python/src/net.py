import time
import sys
import string
import socket

__all__ = ["testIPrange", "getallipv4", "isPasswordStrong" ]

def testIPrange(IP):
	validips = []
	octs = IP.split('.')
		
	for a in range(1,255):
		ip = '.'.join((octs[0], octs[1], octs[2], str(a)))
		try :
			info = socket.gethostbyaddr(ip)
		except socket.herror , msg:	continue
		validips.append([info[2][0], info[0]])
	return validips
	
def getallipv4(website):
	iplist = []
	info = socket.getaddrinfo(website,80) 
	for x in info : 
		if x[0] == socket.AF_INET : #IPv4 addres
			try :
				temp = socket.gethostbyaddr(x[4][0])
			except: 
				continue
			iplist.append([temp[0], temp[2][0]])
			
		#if x[0] == socket.AF_INET6 : #IPv6 addres
			#temp = socket.gethostbyaddr(x[4][0])
			#ips.append([temp[0], temp[2][0]])
	return iplist
	
def isPasswordStrong(password, minlength=8, minupper=1, minlower=1, mindigit=1, minsymbol=1 ):
	ucount = 0
	lcount = 0 
	dcount = 0
	scount = 0
	
	if len(password) < minlength : return False
	
	for x in password : 
		if x in string.lowercase : lcount += 1
		if x in string.uppercase : ucount += 1
		if x in string.digits : dcount += 1
		if x in specialchar : scount += 1
	
	if ucount < minupper : return False
	if lcount < minlower : return False
	if dcount < mindigit : return False
	if scount < minsymbol : return False
	
	return True