#Title: QCE in Higher Dimensions

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
plt.rcParams['text.usetex'] = True

def rQC_line(Y,eh=0):
    n = len(Y)-1
    #grap(u-) = (X,Yd)
    Yd = [Y[0]]
    for j in range(n):
        Yd.append(min([Yd[j]-eh,Y[j+1]]))

    #rap(u+) = (X,Yi)
    Yi = [k for k in range(n+1)]
    Yi[n] = Y[n]
    for k in range(1,n+1):
        j = n+1-k
        Yi[j-1] = min([Yi[j]-eh,Y[j-1]])

    #grap(u) = max{u-,u+}
    Ymax = []
    for k in range(n+1):
        Ymax = Ymax + [max(Yd[k],Yi[k])]
    return Ymax

#A continuous function g
# a,b = -1,1
# c,d = -2,2
# n,m = 200,300
# name = 5

# def g(x,y):
# 	if y<0:
# 		return np.sqrt(x**2+(y+1)**2)
# 	else:
# 		return np.sqrt(x**2+(y-1)**2)

a,b = -1,1
c,d = -1,1
n,m = 200,200
name = 6

def g(x,y):
	return np.exp(x**3)-y**2

# a,b = -np.pi,np.pi
# c,d = -np.pi,np.pi
# n,m = 300,300
# name = 7
# def g(x,y):
# 	return np.sin(x)+np.sin(y)


X = []
for k in range(n):
	X = X + [a + (b-a)/(n-1)*k]
Y = []
for k in range(m):
	Y = Y + [c + (d-c)/(m-1)*k]

Z=[]
for y in range(m):
	Z.append([])
	for x in range(len(X)):
		Z[y].append(g(X[x],Y[y]))

Zmax=[]
for y in range(m):
	Zmax.append([])
	Zmax[y] = rQC_line(Z[y],eh=0)


for x in range(n):
	T = []
	for y in range(m):
		T = T+[Zmax[y][x]]
	T = rQC_line(T,eh=0)
	for y in range(m):
		Zmax[y][x] = T[y]


Z = np.array(Z)
Zmax = np.array(Zmax)
X, Y = np.meshgrid(X, Y)

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')
#ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0)
ax.plot_wireframe(X, Y, Z,color='red', rstride=10, cstride=10,linewidth=0.5)
ax.set_title('$g_'+str(name)+'$')

ax = fig.add_subplot(1, 2, 2, projection='3d')
surf = ax.plot_surface(X, Y, Zmax, cmap=cm.coolwarm,linewidth=0)
ax.plot_wireframe(X, Y, Zmax,color='blue', rstride=10, cstride=10,linewidth=0.5)
ax.set_title('$QC^D(g_'+str(name)+')$')

plt.savefig('QCEg_'+str(name)+'.pdf',bbox_inches='tight')
plt.show()
