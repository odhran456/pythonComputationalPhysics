import numpy as np 
import matplotlib.pyplot as plt
filename = '/home/msc/odm1/RStatsnMaths/abalone.data'
data = np.loadtxt(filename,delimiter=',')
plt.hist([data[x][0] for x in range(len(data))])   
plt.show()
