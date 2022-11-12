li=[]
n=int(input("enter the size of list:"))
for i in range(0,n):
    e=int(input("enter the elements in the list:"))
    li.append(e)
print("positive number in the given list are:")
for i in li:
    if i>0:
       print(i,end="")
