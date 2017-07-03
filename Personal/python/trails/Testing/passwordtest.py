import string
specialchar = ['@', '#', '$', '%', '&', '*', '+', '-', '=']
passes = [	'Welcoome1213',
			'aSDlfkj=02q@',
			'123yiu',
			'asdytiqwe',
			'as1qaZ2ws4rf$',
			'sdf$lk$ajwe0',
			'sdf$lk$ajwE0',
			'Aw@uTpl$T1$b$l']
		
		
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
	
	
for x in passes : 
	print x,isPasswordStrong(x)