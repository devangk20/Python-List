def string():
    a=input("Enter the sring as an element")
    l.append(a)
def integer():
    a=int(input("Enter the integer as an input"))
    l.append(a)
l=[]
num=int(input("Enter the number "))
for i in range(num):
    ch=int(input("Enter\n\n1.String\t2.Integer"))
    if ch==1:
        string()
    if ch==2:
        integer()
print(l)
