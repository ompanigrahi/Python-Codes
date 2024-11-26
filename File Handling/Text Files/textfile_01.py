fh=open(r'D:\#OP67\textfile_01.txt','w')
for i in range(5):
    fh.write("This is my first program in file handling.")
    fh.write("\n")
fh.close()




fh=open(r'D:\#OP67\textfile.txt','r')
s=fh.read()
print(s)
fh.close()
