from H1 import *
hRead = open("F:\\test\\1.2\\14.txt", "r")
hWrite = open("F:\\test\\1.2\\ans14.txt","w")

n=int(hRead.readline())
A = [0]*n
for i in range(n):
    A[i]=list(map(int,hRead.readline().split()))
b=list(map(int, hRead.readline().split()))
z=D3Mat(A,n,b)
hWrite.write(' '.join(map(str, z)));
hRead.close()
hWrite.close()