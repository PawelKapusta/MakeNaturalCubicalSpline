import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

def function(x):
    return 1/(1+5*pow(x,2))

pointsTab=[]
print("My calculated points")

for i in range(0, 65):
   pointsTab.append(-1 + (i / 32.0))
   print("x{} = {}".format((i +1), "%0.7f" % pointsTab[i]))
temp2=np.array(pointsTab)

functionValues=[]
for i in range(0, 65):
    functionValues.append(function(pointsTab[i]))

print("My results: ")
for a in functionValues:
    print(a)
temp=np.array(functionValues)

splajn=scipy.interpolate.CubicSpline(temp2, temp, bc_type='natural')


xplot=np.arange(-1,1,0.001)

plt.plot(temp2, temp, 'rx')
plt.plot(xplot,splajn(xplot), 'g')

plt.legend(['Points', 'Line'])
plt.title('Graph of Cubical spline')
plt.axvline()
plt.axhline()
plt.grid(True)
plt.savefig('Graph.png')
plt.show()
