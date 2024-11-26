
L=[1,2,3,4]
for i in range(1,6):
    n=int(input("Enter a number: "))
    fact=1
    for i in range(1,6):
        fact=fact*i
    L.append(fact)
print(L)    
