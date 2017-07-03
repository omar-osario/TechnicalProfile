import time
starttime,sol = time.time(), 0

wordtoletter = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand']


lettersinnum = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8, 6, 6, 5, 5, 5, 7, 6, 6, 7, 8]

def numberToWord(n):
	if n <= 20 : return wordtoletter[n]
	
	temp = ""
	onesandtens = 0
	digits = []
	for x in str(n):
		digits.append(int(x))
	
	if n > 99 and n <= 999: 
		temp +=  wordtoletter[digits[-3]] + ' hundred '
		if digits[-1] > 0 or digits[-2] > 0 : temp += 'and '
	
	onesandtens  = digits[-2]*10 + digits[-1]
	if onesandtens < 21 : 
		temp += wordtoletter[onesandtens]
	else : 
		temp += wordtoletter[digits[-2]+18] + "-" + wordtoletter[digits[-1]]
		
	return temp 
		
def LettersInNumber(n):
	
	if n <= 20 : return lettersinnum[n]
	temp = 0
	onesandtens = 0
	digits = []
	for x in str(n):
		digits.append(int(x))
	
	if n > 99 and n <= 999: 
		temp +=  lettersinnum[digits[-3]] + 7 #' hundred '
		if digits[-1] > 0 or digits[-2] > 0 : temp += 3 #'and '
	
	onesandtens  = digits[-2]*10 + digits[-1]
	if onesandtens < 21 : 
		temp += lettersinnum[onesandtens]
	else : 
		temp += lettersinnum[digits[-2]+18] + lettersinnum[digits[-1]]
		
	return temp 

for x in range(1,1000):
	sol += LettersInNumber(x)
	
print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol + 11, time.time() - starttime)
print "*****************************************************************"	
#tried 21121 -> wrong
#tried 21124 correct
#1.24099993706
#0.00499987602234
