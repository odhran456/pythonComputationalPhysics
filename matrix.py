import numpy as np

M = np.array([[1,3,-5,2],[0,4,-2,1],[2,-1,3,-1],[1,1,1,1]])
b = np.array([0,6,5,10])
x = np.linalg.solve(M,b)

print(M[1][1])

print(x)
