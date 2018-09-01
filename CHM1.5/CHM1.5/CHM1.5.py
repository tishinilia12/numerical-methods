
from H1 import *
hRead = open("F:\\test\\1.5\\14.txt", "r")
hWrite = open("F:\\test\\1.5\\ans14.txt","w")
n=int(hRead.readline())
e=float(hRead.readline())
A = [0]*n
for i in range(n):
    A[i]=list(map(int, hRead.readline().split()))
c=0
Y=False
while not(Y):
    hWrite.write("итерация номер ")
    hWrite.write(str(c))
    hWrite.write("\n")
    writeMat(A,hWrite)
    c+=1
    Q=bildQ(A,n)
    A=multMat(A,Q,n)
    tranMat(Q,n)
    A=multMat(Q,A,n)
    i=0
    while i<=n:
        if i==n:
            Y=True
            break
        if chekQR(A,n,e,i):
            i+=1
        elif chekQRP(A,n,e,i) and chekQR(A,n,e,i+1):
            i+=2
        else:
            break
for i in range(n-1):
    if abs(A[i+1][i])>e:
        ax=1
        bx=-A[i+1][i+1]-A[i][i]
        cx=A[i+1][i+1]*A[i][i]-A[i+1][i]*A[i][i+1]
        D=bx*bx-4*cx*ax
        x1=(-bx+D**0.5)/2
        x2=(-bx-D**0.5)/2
        A[i+1][i+1]=x1
        A[i][i]=x2
        A[i][i+1]=0
        A[i+1][i]=0
writeMatCom(A,hWrite)
hRead.close()
hWrite.close()