import numpy as np 
import matplotlib.pyplot as plt

u = 1.8
g = 9.8
y0 = 1

theta = np.linspace(0,1.9,100)

sx = ((u * np.cos(theta)) / 9.8 ) * ((u * np.sin(theta)) + ((((u**2)*(np.sin(theta)**2))+(2*y0*g))**0.5))

fx = 0*theta

plt.plot(theta,sx)
plt.plot(theta,fx)

plt.show()
#plt.savefig('figure')
