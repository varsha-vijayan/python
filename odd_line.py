fn = open('bcd.txt', 'r') 
fn1 = open('nfile.txt', 'w') 
cont = fn.readlines() 
type(cont) 
for i in range(0, len(cont)): 
     if(i % 2 ! = 0): 
        fn1.write(cont[i]) 
    else: 
        pass
fn1.close() 
fn1 = open('nfile.txt', 'r') 
cont1 = fn1.read() 
print(cont1) 
fn.close() 
fn1.close()

INPUT TEXT FILES: 
bcd.txt
Welcome to the world of python 
Python programming !!!!!! 
Python was developed by Guido Van Rossum Python is derived from many other languages. 
Python source code is available under GNU.

nfile.txt
Welcome to the world of python 
Python was developed by Guido Van Rossum 
Python source code is available under GNU 
