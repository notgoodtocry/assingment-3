import random

b = ["ketab" , "daftar" , "medad" ,"kodkar"]

a = int(input("Levels ? (0:ason, 1:motevaset , 2:sakht"))
if (a == 0):
    health = 15
elif (a == 1):
    health = 10
elif (a == 2):
    health = 5
    
c = random.choice(b)
d = []
for i in range(len(c)):
    d.append("_")

while health > 0:
    print(" ".join(d))
        
    if (("".join(d)) == c):
        print("barande shodi")
        break
    
    e = input()
    e = e.lower()
    
    if (e in c):
        print("bale joon barabare ast ba", health)
        for i in range(len(c)):
            if (c[i] == e):
                d[i] = e        
                
    else:
        health -= 1
        print( "joon nadari =", health)