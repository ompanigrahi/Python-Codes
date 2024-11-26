def JPS(a,n):
    if n==1:
        return a
    else:
        return(a*JPS(a,n-1))

K=int(input("Enter a number:"))
Z=int(input("Enter a number:"))
M=JPS(K,Z)
print(M)
