import random
import matplotlib.pyplot as plt


res = []

# iterations
for i in range(10000):
	#initialize teams
	a = 16
	b = 16
	#start killing players!!
	while a > 0 and b > 0:
		#calculating combat power
		a2 = int(a**2*1)
		b2 = int(b**2*1)
		#pick one to kill 
		r = random.randint(-a2, b2) 
		if r > 0:
			a -= 1
		elif r < 0:
			b -= 1 
	#record results
	diff = a - b
	res.append(diff)
	
plt.hist(res, 4*max(res)+1)
plt.show()
