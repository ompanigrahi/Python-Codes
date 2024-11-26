def S(n):
    if n==1:
        return 1
    else:
        return(n+S(n-1))

K=int(input("Enter a number:"))
M=S(K)
print(M)
