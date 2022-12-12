a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
largest=0
if a>b and a>c:
    largest=a
if b>a and b>c:
    largest=b
if c>a and c>b:
    largest=c
print("the largest number is:",largest)
      
