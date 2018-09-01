hRead = open("F:\\test\\3.1\\14.txt", "r")
hWrite = open("F:\\test\\3.1\\ans14.txt","w")
import math
def f(a):
    return 1/math.tan(a)+a
x0=float(hRead.readline())
x1=list(map(float, hRead.readline().split()))
x2=list(map(float, hRead.readline().split()))
y1 = [0]*len(x1)
y2 = [0]*len(x2)
for i in range(len(x1)):
    y1[i]=f(x1[i])
for i in range(len(x2)):
    y2[i]=f(x2[i])
L1=0
for i in range(len(x1)):
    a=y1[i]
    for j in range(len(x1)):
        if i!=j:
            a*=(x0-x1[j])/(x1[i]-x1[j])
    L1+=a;
L2=0
for i in range(len(x2)):
    a=y2[i]
    for j in range(len(x2)):
        if i!=j:
            a*=(x0-x2[j])/(x2[i]-x2[j])
    L2+=a;
hWrite.write( "\nответ для первого набора для метода Лагранжа\n")
hWrite.write(str(L1))
hWrite.write("\nответ для второго набора для метода Лагранжа\n")
hWrite.write(str(L2))
def f1(x1,l,r,y1):
    if l==r:
        return y1[l]
    return (f1(x1,l,r-1,y1)-f1(x1,l+1,r,y1))/(x1[l]-x1[r])
L3=0
q=1
for i in range(len(x1)):
    L3+=q*f1(x1,0,i,y1)
    q*=x0-x1[i]
L4=0
q=1
for i in range(len(x2)):
    L4+=q*f1(x2,0,i,y2)
    q*=x0-x2[i]
hWrite.write("\nответ для первого набора для метода Ньютона\n")
hWrite.write(str(L3))
hWrite.write("\nответ для второго набора для метода Ньютона\n")
hWrite.write(str(L4))
hWrite.write("\nответ\n")
hWrite.write(str(f(x0)))
hRead.close()
hWrite.close()
