fh=open(r'D:\#OP67\Text Files\fhandling.txt',"w")
for i in range(5):
    name=input("Enter your name: ")
    fh.write(name)
    fh.write("\n")
fh.close()

fz=open(r'D:\#OP67\Text Files\fhandling.txt')
S=fz.read()
print(S)
fz.close()
