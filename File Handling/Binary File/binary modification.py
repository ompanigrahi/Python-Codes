import pickle

fh=open("D:\\#OP67\\Text Files\\changing a letter binary.txt",'wb')
f=[6167,435,6231,430,6204,453]
pickle.dump(f,fh)
fh.close()


import pickle



fh=open("D:\\#OP67\\Text Files\\changing a letter binary.txt",'rb+')

d=[]

try:
    while True:
        k=fh.tell()
        d=pickle.load(fh)
        print(d)
        inp=int(input("Enter the element number:"))
        numb=int(input("Enter the number you want to replace: "))
        jps=int(input("Enter th enumber you want to replace with: "))
        if d[inp]==numb:
            d[inp]=jps
            fh.seek(k,0)
            
            pickle.dump(d,fh)
            print(d)

except EOFError:
    fh.close()
