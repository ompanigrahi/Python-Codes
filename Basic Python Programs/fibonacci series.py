def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)



#Main

n=int(input("Enter the number of terms you required: "))
for i in range(1,n+1):
    print(fib(i),end=',')
print("._.")
