from H1 import *
hRead = open("F:\\test\\1.1\\14.txt", "r")
hWrite = open("F:\\test\\1.1\\14ans.txt","w")
n=int(hRead.readline())
U = [0]*n
for i in range(n):
    U[i]=list(map(int, hRead.readline().split()))
L=[[0 for i in range(n)] for i in range(n)]
P=[[0 for i in range(n)] for i in range(n)]
for i in range(n):
    P[i][i]=1
A=eqMat(U,n)
funLUP(U,L,P,n)
writeMat(P,hWrite)
hWrite.write("это P\n")
writeMat(U,hWrite)
tranMat(P,n)
hWrite.write("это U\n")
writeMat(L,hWrite)
hWrite.write("это L\n") 
writeMat(A,hWrite)
hWrite.write("это A\n")
LU = multMat(L,U,n)
LUP =multMat(P,LU,n)
#writeMat(LU,hWrite)
#hWrite.write("это LU\n")
writeMat(LUP,hWrite)
hWrite.write("это LUP\n")
hWrite.write(str(round(abs(opMatLU(U,n)), 4)))
hWrite.write("\nэто определитель\n")
b=list(map(int, hRead.readline().split()))
z=multVM(b,P,n)
Q=fiAns(U,L,n,z)
hWrite.write("(")
for i in Q:
    hWrite.write(str(round(i, 4)))
    hWrite.write(" ")
hWrite.write(")\n")

hWrite.write("это решение для вектора\n")
hWrite.write("(")
for i in b:
    hWrite.write(str(round(i, 4)))
    hWrite.write(" ")
hWrite.write(")\n")
hWrite.write("\n")
C=[[] for i in range(n)]
y=[0 for i in range(n)]

for i in range(n):
    y[i]=1;
    z=multVM(y,P,n)
    C[i]=fiAns(U,L,n,z)
    y[i]=0;
tranMat(C,n)
writeMat(C,hWrite)
hWrite.write("это обратная матрица\n")
hRead.close()
hWrite.close()