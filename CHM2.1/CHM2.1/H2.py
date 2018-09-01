def f(x):
    return x**3 -2*x**2-10*x+15
def derf(x):
    return 3*x**2-4*x-10
def fx(x):
    return (x**3-2*x**2+15)/10
def fdx(x):
    return (3*x**2-4*x)/10
def metN(x0,e):
    xk=x0+1+e
    xk1=x0
    while abs(xk-xk1)>=e:
        xk=xk1
        xk1=xk-f(xk)/derf(xk)
    return xk1
def metI(x0,e):
    xk=x0+1+e
    xk1=x0
    while abs(xk-xk1)>=e:
        q=fdx(xk1)
        e=q/(1-q)*abs(xk-xk1)
        xk=xk1
        xk1=fx(xk)
    return xk1