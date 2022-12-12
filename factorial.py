num=int(input("Enter a value:"))
def factorial(num):
    factorial=1
    if num==1 or num==0:
       return 1
    for i in range(1,num+1):
        factorial=factorial*i
    return factorial
factorial(num)
print("factorial of",num,"is :",factorial(num))
