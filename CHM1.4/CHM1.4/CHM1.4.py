from H1 import *
hRead = open("F:\\test\\1.4\\14.txt", "r")
hWrite = open("F:\\test\\1.4\\ans14.txt","w")
n=int(hRead.readline())
e=float(hRead.readline())
A = [0]*n
for i in range(n):
    A[i]=list(map(int, hRead.readline().split()))
hWrite.write("e=")
hWrite.write(str(e))
hWrite.write("\n")
writeMat(A,hWrite)
hWrite.write("это матрица\n")
ans,MU=metIak(A,n,e)
writeMat(ans,hWrite)
hWrite.write("это матрица c собствеными значениями\n")
writeMat(MU,hWrite)
hWrite.write("собственые векторы по столбцам \n")
tranMat(MU,n)
for i in range(n):
    zzz=multMV(A,MU[i],n)
    writeV(zzz,hWrite)
    for j in range(n):
        MU[i][j]*=ans[i][i];
    writeV(MU[i],hWrite)
    hWrite.write("вектор номер ")
    hWrite.write(str(i+1))
    hWrite.write("\n")
hRead.close()
hWrite.close()