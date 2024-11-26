import pickle
f=[]
fh=open("D:\\#OP67\\Text Files\\searching word.txt",'wb')
f=[1,2,3,4,5]
pickle.dump(f,fh)
fh.close()



import pickle
read=open("D:\\#OP67\\Text Files\\searching word.txt",'rb')
try:
    while True:
        L=pickle.load(read)
        print(L)
except EOFError:
    read.close()
search=int(input("Enter a number:"))
if search in L:
    print("The element exist in the List:)")
else:
    print("The number you have searched for doesnt exist in the list :(")

