num=int(input("Enter a number:"))
def factor(num):
    print("The factor of",num,"are:")
    for i in range(1,num+1):
        if num%i==0:
            print(i)
factor(num)
