import math
def df1dx1(x1,x2):
    return 2*x1/9
def df2dx1(x1,x2):
    return -1-math.exp(x1)
def df1dx2(x1,x2):
    return 8*x2/9
def df2dx2(x1,x2):
    return 3
def f1(x1,x2):
    return (x1**2)/9+(x2**2)*4/9-1
def f2(x1,x2):
    return 3*x2-math.exp(x1)-x1
def J(x1,x2):
    return df1dx1(x1,x2)*df2dx2(x1,x2)-df2dx1(x1,x2)*df1dx2(x1,x2)
def A1(x1,x2):
    return f1(x1,x2)*df2dx2(x1,x2)-f2(x1,x2)*df1dx2(x1,x2)
def A2(x1,x2):
    return df1dx1(x1,x2)*f2(x1,x2)-df2dx1(x1,x2)*f1(x1,x2)
def metN(x1,x2,e):
    s=e+1
    while s>e:
        x10=x1
        x20=x2
        x1=x1-A1(x10,x20)/J(x10,x20)
        x2=x2-A2(x10,x20)/J(x10,x20)
        s=((x10-x1)**2+(x20-x2)**2)**0.5
    v=[0]*2
    v[0]=x1
    v[1]=x2
    return v
def f_2(x1,x2):
    return ((-(x1**2)/4)+9/4)**0.5
def f_1(x1,x2):
    return math.log(3*x2-x1,math.exp(1))
def f_2d1(x1,x2):
    return abs(-0.25*x1/(9/4-x1**2)**0.5)
def f_2d2(x1,x2):
    return 0
def f_1d1(x1,x2):
    return abs(1/(3*x2-x1))
def f_1d2(x1,x2):
    return abs(3/(3*x2-x1))
def findq(x1,x2):
    return max( f_2d2(x1,x2)+f_2d1(x1,x2),f_1d2(x1,x2)+f_1d1(x1,x2))
def metI(x1,x2,e):
    s=e+1
    x10=x1+s
    x20=x2+s
    while max(abs(x10-x1),abs(x20-x2))>e:
        q=findq(x1,x2)
        e=q/(1-q)*max(abs(x10-x1),abs(x20-x2))
        x10=x1
        x20=x2
        x1=f_1(x1,x2)
        x2=f_2(x1,x2)
    v=[0]*2
    v[0]=x1
    v[1]=x2
    return v