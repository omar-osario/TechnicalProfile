from math import pow

ulimit = 10000
power = 3

for a in range(1,ulimit):
	for b in range(1,ulimit):
		dummy = pow((a**power)+(b**power),(1.0/float(power)))
		if a*b % 2500 == 0 :print ',',
		if dummy == int(dummy):
			print
			print dummy, dummy*power, a, b 