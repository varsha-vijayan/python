a=[11,12,13,14,15]
b=[12,15,10,20]
L1=len(a)
L2=len(b)
sum1=0
sum2=0
count=0
if L1==L2:
    print("The two list contain same number of elements")
else:
    print("the list are of different length")
for i in a:
    sum1+=1
    i=i+1
print("sum of elements of a=",sum1)
for j in b:
    sum2+=j
    j=j+1
print("sum of elements of b=",sum2)
if sum1==sum2:
    print("Lists sums to same value",sum1)
else:
    print("Lists sums to different value",sum1,"and",sum2)
for i in range(0,L1):
    for j in range(0,L2):
        if b[j]==a[i]:
            count=count+1
            j=j+1
    i=i+1
           
print("no.of same elements:",count)
