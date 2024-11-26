import pickle
fh=open("D:\\#OP67\\Text Files\\file pointer testing.txt",'wb')
f="a"
pickle.dump(f,fh)
fh.close()



fh=open("D:\\#OP67\\Text Files\\file pointer testing.txt",'rb')
o=pickle.load(fh)

fh.seek(0,2)
k=fh.tell()
print(k)
fh.close()
