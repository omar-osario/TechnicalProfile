import time
starttime,sol = time.time(), 0
from math import sqrt

#maximum perimeter 10**9 so maximum side length = 333,333,333

print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# X 1525870544 T 0.0160000324249
# X 139613220658 T 0.069000005722
# X 1772363839 T 0.0550000667572
# X 1934726302 T 0.055999994278
# X 100568547810 T 0.047000169754
# X 7220496864 T 0.0439999103546
# X 159339984960 T 0.0439999103546

"""
res_m = [0, 2]
res_p = [1, 3]
ulimit = 10000000000
next_m = 5
next_p = 17
print  
while 3*next_m + 1 < ulimit:
	sol += 3*next_m + 1
	res_m.append(4*res_m[-1] - res_m[-2])
	#area_m = (float(next_m)-1.0)*sqrt(etrianglem(next_m))/4.0
	print res_m , 3*next_m + 1 , sol
	next_m = res_m[-1]**2 + 1


while 3*next_p - 1 < ulimit:
	sol += 3*next_p - 1
	res_p.append(4*res_p[-1] - res_p[-2])
	#area_p =  (float(next_p)-1.0)*sqrt(etrianglep(next_p))/4.0
	print res_p, 3*next_p - 1, sol
	next_p = (res_p[-1]**2)*2 - 1


counter = 3
test = 20 
step = 44 	
while counter < ulimit :
	temp = sqrt(test)
	#print counter, test
	if temp == int(temp) : 
		print counter, test
	test += step 
	step += 12 
	counter += 2
"""

