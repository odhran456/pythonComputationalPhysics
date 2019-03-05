import numpy as np 

def f_(theta):
    return ((1.8 * np.cos(theta)) / 9.8 ) * ((1.8 * np.sin(theta)) + ((((1.8**2)*(np.sin(theta)**2))+(2*1*9.8))**0.5))

a = 1.25
b = 1.75

dtheta = abs(b-a)

while dtheta > 0.005:
    theta = (a+b)/2.0
    if (f_(a)*f_(theta)) < 0:
        b = theta
    else:
        a = theta
    dtheta = abs(b-a)

print(theta)
