from H1 import *
hRead = open("F:\\test\\3.3\\14.txt", "r")
hWrite = open("F:\\test\\3.3\\ans14.txt","w")
n=int(hRead.readline())
x=list(map(float, hRead.readline().split()))
y=list(map(float, hRead.readline().split()))
A1=[[0 for i in range(2)] for i in range(2)]
A2=[[0 for i in range(3)] for i in range(3)]
b1=[0 for i in range(2)]
b2=[0 for i in range(3)]
for i in range(2):
    for j in range(2):
        for k in range(n):
            A1[i][j]+=x[k]**(i+j);
for i in range(2):
    for k in range(n):
        b1[i]+=x[k]**(i)*y[k];
for i in range(3):
    for j in range(3):
        for k in range(n):
            A2[i][j]+=x[k]**(i+j);
for i in range(3):
    for k in range(n):
        b2[i]+=x[k]**(i)*y[k];
Q1=sysans(A1,b1,2)
Q2=sysans(A2,b2,3)
hWrite.write(f'F1(x)={Q1[0]}+({Q1[1]})*x\n')
sum1=0
sum2=0
for i in range(n):
    sum1+=(Q1[0]+Q1[1]*x[i]-y[i])**2
for i in range(n):
    sum2+=(Q2[0]+Q2[1]*x[i]+Q2[2]*x[i]*x[i]-y[i])**2
hWrite.write(f'Ф={sum1}\n')
hWrite.write(f'F2(x)={Q2[0]}+({Q2[1]})*x+({Q2[2]})*x**2\n')
hWrite.write(f'Ф={sum2}\n')
hRead.close()
hWrite.close()
