def integration(fn,a,b,N):
    I=0
    dx=(b-a)/float(N)
    for j in range(N):
        x = a + (dx*j)
        I = I + (fn(x)*dx)
    print(I)

def g(x):
    return (x**2) + 7

integration(g,2,4,10)
