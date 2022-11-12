len=int(input("how many number's do you save?"))
inputvaluelist=[]
for n in range(0,len):
    inputvalue=int(input("enter a value"))
    if inputvalue>=100:
        inputvaluelist.append("OVER")
    else:
            inputvaluelist.append(inputvalue)
            print(inputvaluelist)
    
