
def funLU(U,L,n):
    for i in range(n):
        for j in range(i,n):
            L[j][i]=U[j][i]/U[i][i]
    for k in range(1,n):
        for i in range(k-1,n):
            for j in range(i,n):
                L[j][i]=U[j][i]/U[i][i]
        for i in range(k,n):
            for j in range(k-1,n):
                U[i][j]=U[i][j]-L[i][k-1]*U[k-1][j]
def multMat(L,U,n):
    LU =[[0 for i in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                LU[k][i]+=L[k][j]*U[j][i]
    return LU
def writeMat(U,hWrite):
    for i in U:
        hWrite.write("(")
        for j in i:
            hWrite.write(str(round(j, 4)))
            hWrite.write(" ")
        hWrite.write(")\n")
def printMat(U):
    for i in U:
        print("(",end="")
        for j in i:
            print(round(j, 4),end=" ")
        print(")")

def eqMat(U,n):
    A=[[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j]=U[i][j]
    return A
def opMatLU(U,n):
    a=1
    for i in range(n):
        a*=U[i][i]
    return a
def opMat(A,n):
    U=eqMat(A,n)
    L=[[0 for i in range(n)] for i in range(n)]
    funLU(U,L,n)
    return opMatLU(U,n)
def UMult(U,n,b):
    y=[0 for i in range(n)]
    for i in range(n):
        SUM=0
        for j in range(n-i,n):
            SUM-=y[j]*U[n-1-i][j]
        y[n-1-i]=(b[n-1-i]+SUM)/U[n-1-i][n-1-i]
    return y
def LMult(L,n,y):
    x=[0 for i in range(n)]
    for i in range(n):
        SUM=0
        for j in range(0,i):
            SUM-=x[j]*L[i][j]
        x[i]=(y[i]+SUM)/L[i][i]
    return x
def fiAns(U,L,n,b):
    return UMult(U,n,LMult(L,n,b))
def tranMat(A,n):
    for i in range(n):
        for j in range(n):
            if i>j:
                c=A[i][j]
                A[i][j]=A[j][i]
                A[j][i]=c


def D3Mat(v,n,b):
    for i in range(1,n):
        v[i][1]-=v[i][0]*v[i-1][2]/v[i-1][1]
        b[i]-=b[i-1]*v[i][0]/v[i-1][1]
    for i in range(1,n):
        b[n-i-1]-=b[n-i]*v[n-i-1][2]/v[n-i][1]
    for i in range(n):
        b[i]/=v[i][1]
    return b