
fh=open("D:\\#OP67\\Text Files\\changing a letter.txt",'w')
f="abcdefghijklmnop"
fh.write(f)
fh.close()



fh=open("D:\\#OP67\\Text Files\\changing a letter.txt",'r+')

try:
    while True:
        k=fh.tell()
        n=fh.read(1)
        if n=='e':
            fh.seek(k,0)
            fh.write('E')


except EOFError:
    fh.close()
                
                
