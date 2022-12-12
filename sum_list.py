x=int(input("enter the limit:"))
count=0
sum=0
list=[]
while(count<x):
    a=int(input("Enter a value:"))
    list.append(a)
    count=count+1
print("The list is:",list)
for i in list:
    sum=sum+i
print("sum of all items in a given list is:",sum)
