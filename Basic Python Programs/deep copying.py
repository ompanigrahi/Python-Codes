T=(1,2,3,4,5,6,7,8,9,10)
for i in range(2,len(T)):
    j=i*(i+1)
    T=list(T)
    T[i]=j
  
print(tuple(T))
