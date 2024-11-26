def GCD(p,q):
    if q==0:
        return p
    return GCD(q,p%q)



a=int(input("Enter the first number:_"))
b=int(input("Enter the second number:_"))
x=GCD(a,b)
print(a)
