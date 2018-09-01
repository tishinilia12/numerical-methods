from H1 import *
hRead = open("F:\\test\\3.2\\14.txt", "r")
hWrite = open("F:\\test\\3.2\\ans14.txt","w")
def h(i,x):
    return x[i]-x[i-1];
def c(i,C,n):
    if i<2:
        return 0
    if i>n-1:
        return 0
    return C[i-2]
def a(i,y):
    return y[i-1]
def b(i,C,y,x,n):
    return (y[i]-y[i-1])/h(i,x)-1/3*h(i,x)*(c(i+1,C,n)+2*c(i,C,n))
def d(i,C,x,n):
    return (c(i+1,C,n)-c(i,C,n))/3/h(i,x);
def F(i,C,y,x,n,X_T):
    return a(i,y) + b(i,C,y,x,n)*(X_T-x[i-1])+c(i,C,n)*((X_T-x[i-1])**2)+d(i,C,x,n)*((X_T-x[i-1])**3)
n=int(hRead.readline())
X_=float(hRead.readline())
x=list(map(float, hRead.readline().split()))
y=list(map(float, hRead.readline().split()))
C_m=[[0 for i in range(n-2)] for i in range(n-2)]
Q_m=[0 for i in range(n-2)]
for i in range(2,n):
    if i > 2:
        C_m[i-2][i-3]=h(i-1,x);
    C_m[i-2][i-2]=2*(h(i-1,x)+h(i,x))
    if i<n-1:
        C_m[i-2][i-1]=h(i,x);
for i in range(2,n):
    Q_m[i-2]=3*((y[i]-y[i-1])/h(i,x)-(y[i-1]-y[i-2])/h(i-1,x))
C=D3Mat(D3path(C_m,n-2),n-2,Q_m)
for i in range(1,n):
    if X_<=x[i] and X_>x[i-1]:
        F(i,C,y,x,n,X_)
        hWrite.write(f'f({X_})= {F(i,C,y,x,n,X_)}\n')
    hWrite.write(f'f(x)= {a(i,y)}+({b(i,C,y,x,n)})*(x-{x[i-1]})+({c(i,C,n)})*(x-{x[i-1]})**2+({d(i,C,x,n)})*(x-{x[i-1]})**3 при где x[{x[i-1]},{x[i]}]\n')

hRead.close()
hWrite.close()
