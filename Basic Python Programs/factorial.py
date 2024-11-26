def FACT(n):
    if n==1:
        return 1
    else:
        return(n*FACT(n-1))

K=int(input("Enter a number:"))
M=FACT(K)
print(M)
