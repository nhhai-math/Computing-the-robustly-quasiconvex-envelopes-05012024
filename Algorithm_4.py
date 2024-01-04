#Title: QCE in one dimensional

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['text.usetex'] = True

#A continuous function g
a = -1
b = 1
n = 50
def g(x):
	return np.log(x**4-3*x**2+x+5)
	# return np.sqrt(x**3-x+2)
	# return (x-1)*(x-2)*(x-3)*(x-4)*(x-5)
	# return np.e**(-x**3+x)
num_name=1

h=(b-a)/n
e=0

X = []
Y = []
for k in range(n+1):
	X = X + [a + (b-a)/n*k]
	Y = Y + [g(a+(b-a)/n*k)]
plt.plot(X,Y,label='$g_'+str(num_name)+'$')

#u-
Yd = [Y[0]]
for k in range(n):
	Yd.append(min([Yd[k]-e*h,Y[k+1]]))
#plt.scatter(X,Yd,label='$u^-$')

#u+
Yi = [k for k in range(n+1)]
Yi[n] = Y[n]

for k in range(1,n+1):
	j = n+1-k
	Yi[j-1] = min([Yi[j]-e*h,Y[j-1]])

#u
Ymax = []
for k in range(n+1):
	Ymax = Ymax + [max(Yd[k],Yi[k])]
plt.plot(X,Ymax,'o',label='$QCE(g_'+str(num_name)+')$')
		
plt.legend(loc='upper right',fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('QCEg_'+str(num_name)+'.pdf')
plt.show()
