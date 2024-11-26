fh=open(r"D:\#OP67\Text Files\filehand.txt",'w')
fh.write("A library is a collection of modules a packages that together cater to a specific type of applications or requirements.")
fh.close()

fz=open(r"D:\#OP67\Text Files\filehand.txt")
S=fz.read(50)
print(S)
fz.close()
