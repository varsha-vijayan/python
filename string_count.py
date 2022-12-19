s=input("enter the string:")
l=[]
d={}
count=0
for i in s:
    l.append(i)
    d[i]=s.count(i)
print(d)
