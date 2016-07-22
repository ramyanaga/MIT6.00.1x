def f(x):
	import math
	return 400*math.e**(math.log(0.5)/3.66 * x)

def radiationExposure(start, stop, step):
	totalExposure = float(0)
	i = float(start)
	while (i < stop):
		totalExposure+=float(f(i))*step
		i+=step
	return totalExposure

print radiationExposure(0, 4, 0.25)