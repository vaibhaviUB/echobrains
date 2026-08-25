
#loops 
1. WHILE LOOP

while condition:
    stmt

a=0
while a<=5:
    print(a)
    a+=1

a=5
while a>=0:
    print(a)
    a-=1

a=""
while a!="python":
    a=input("enter the best programming language:")
print("yess!!, It's correct")




j=int(input("enter the number :"))
n=1
while n<=10:
    print(j,"X",n, "=", j*n)
    n+=1


a=int(input("enter a number"))
while a<=10:
    if a%2==0:
        print("even")
    else:
        print("odd")
    a+=1

#right angled triangle
n=1
while(n<=5):
    print(n*" *")
    n+=1

#sqare box
n=1
while(n<=5):
    print(5*" *")
    n+=1

    
#hallowsquare using while loop
i=0
while i<=6:
    j=0
    while j<=6:
        if i==0 or i==3 or i==6 or j==0 or j==3 or j==6 or i==j or j+i==6:
            print(" *",end="")
        else:
            print(" 2",end="")
        j+=1
    i+=1
    print()

task --1
A
BC
DEF
GHIJ

x=65
i=1
while i<= 4:
    j=1
    while j<=i:
        print(chr(x),end="")
        x+=1
        j+=1
    print()
    i+=1

task --2
1
23
456
78910

x=1
i=1
while i<=4:
    j=1
    while j<=i:
        print(x,end="")
        x+=1
        j+=1
    print()
    i+=1


task --3
1
12
123
1234

i=1
while i<=4:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1

task --4
1234
123
12
1

i = 4
while i >= 1:
    x = 1
    while x <= i:
        print(x, end="")
        x += 1
    print()
    i -= 1

task --5
  *
 ***
*****

i = 1
while i <= 3:
    s = 1
    while s <= 3 - i:
        print(" ", end="")
        s += 1
    k = 1
    while k <= i * 2 - 1:
        print("*", end="")
        k += 1
    print()
    i += 1



































    
