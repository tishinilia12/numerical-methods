from H1 import *
hRead = open("F:\\test\\KR\\test5.txt", "r")
import matplotlib as mpl 
import matplotlib.pyplot as plt
from math import sinh as sh
from math import cosh as ch
def h(i,x):
    if i<0:
        return 0
    return x[i+1]-x[i];
def S_i(i,P,x):
    return sh(P*h(i,x))
def C_i(i,P,x):
    return ch(P*h(i,x))
def b_i(i,x,y):
    if i==0:
        return (y[i+1]-y[i])/h(i,x)
    if i==len(x)-1:
        return -(y[i]-y[i-1])/h(i-1,x)
    return (y[i+1]-y[i])/h(i,x)- (y[i]-y[i-1])/h(i-1,x)
def d_i(i,x,y,P):
    if i==-1 or i==len(x)-1:
        return 0;
    return (P*C_i(i,P,x)/S_i(i,P,x)-1/h(i,x))/(P*P)
def e_i(i,x,y,P):
    if i==-1 or i==len(x)-1:
        return 0;
    return(1/h(i,x)-P/S_i(i,P,x))/(P*P)
def f(x,ym,x_t,P,n):
    y=[i for i in ym]
    y.append(0)
    C_m=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        if i > 0:
            C_m[i][i-1]=e_i(i-1,x,y,P);
        C_m[i][i]=d_i(i-1,x,y,P)+d_i(i,x,y,P)
        if i<n-1:
            C_m[i][i+1]=e_i(i,x,y,P)
    Q_m=[0 for i in range(n)]
    for i in range(n):
        Q_m[i]=b_i(i,x,y)
    T_2=D3Mat(D3path(C_m,n),n,Q_m)
    i=0
    while not(x[i+1]>=x_t and x_t>x[i]):
        i+=1
    return (1/(S_i(i,P,x)*P*P))*(T_2[i]*sh(P*(x[i+1]-x_t))+T_2[i+1]*sh(P*(-x[i]+x_t)))+\
        (y[i]-T_2[i]/(P*P))*((x[i+1]-x_t)/h(i,x))+\
        (y[i+1]-T_2[i+1]/(P*P))*((-x[i]+x_t)/h(i,x))
n=int(hRead.readline())
x=list(map(float, hRead.readline().split()))
y=list(map(float, hRead.readline().split()))
P=float(hRead.readline())
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.axis([x[0], x[-1], min(y)-0.5, max(y)+0.5])

plt.title('exp spline')
plt.xlabel('x')
plt.ylabel('F(x)')
x_t=x[0]+0.00001
xs = []
s_vals = []
s_vals1 = []
while x_t < x[-1]:
    s_vals += [ f(x,y,x_t,P,n) ]
    xs += [x_t] 
    x_t += 0.007
x_t=x[0]+0.00001
while x_t < x[-1]:
    s_vals1 += [ f(x,y,x_t,P/10000,n) ]
    x_t += 0.007
plt.plot(xs, s_vals, color = 'blue', linestyle = 'solid',label = 'exp SP1')
plt.plot(xs,s_vals1, color = 'red', linestyle = 'solid',label = 'line')
plt.legend(loc = 'upper right')
fig.savefig('F:\\test\\KR\\expSP5.png')
hRead.close()
