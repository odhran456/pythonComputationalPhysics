import numpy as np 
import matplotlib.pyplot as plt

filename = '/home/msc/odm1/PYTHON_STUFF/www-personal.umich.edu/~mejn/computational-physics/stars.txt'
data = np.loadtxt(filename,delimiter=' ',unpack=True)

plt.scatter(data[0],data[1])
plt.gca().invert_xaxis()

plt.show()
