import csv
f=open("D:\\#OP67\\CSV Files\\finding values in a csv file.csv","w",newline='')
print("The list should be in the form [schno,name,marks]")

cvw=csv.writer(f)
z=['School_No.','Name','Marks']
cvw.writerow(z)
L=[]
for i in range(5):
    RNO=int(input("Enter a the roll number: "))
    Name=input("Enter the name of the candidate:")
    Marks=int(input("Enter the marks of the candidate:"))
    L=[RNO,Name,Marks]
    cvw.writerow(L)



f.close()




import csv
f=open("D:\\#OP67\\CSV Files\\finding values in a csv file.csv","r",newline='\r\n')
cvr=csv.reader(f)
i=str(input("Enter the schoolnumber you want to search:"))
for rec in cvr:
    if rec[0]==i:
        print(rec)

f.close()
