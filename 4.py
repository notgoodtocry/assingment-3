import random

a=int(input("tol"))
b=[]

for i in range (a):
    c=random.randint (1 , 1000000)
    b.append(c)
    break
print( b)

