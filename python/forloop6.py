

CONDITIONAL STATEMENTS--

#task -- 1
username="admin"
password="python123"
u=input("enter user name:")
p=input("enter password:")
if username == u:
    if password == p :
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid username")


#task --2
age= int(input("enter your age: "))
salary=int(input("enter monthly salary: "))
creditscore=int(input("enter credit score: "))
if age >= 21 and salary >=30000 and creditscore >= 700:
    print("loan is approved")
else:
    print("loan is rejected")


#task --3 
j=int(input("enter the number :"))
n=int(input("enter the num of table u want:"))
for i in range(1,n+1):
    print(j,"X",i,"=",j*i)

#task -- 5 (right angled triangle)
for i in range (5):
    for j in range(i):
        print("*",end="")
    print()


#task -- 4 (box task)
*****
*   *
*   *
*   *
*****
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 

#task --6
#A
#BC
#DEF
#GHIJK

x = 65
for i in range(5):
    for j in range(i):
        print(chr(x), end="")
        x += 1
    print()


#TASK -- 7
1
23
456
78910

a=1
for i in range(5):
    for j in range(i):
        print(a, end="")
        a += 1
    print()

'''
#TASK -- 8
AAAAA
ABBBA
ABBBA
AAAAA
'''
    
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("A",end="")
        else:
            print("B",end="")
    print()


#TASK -- 9
'''
1
12
123
1234
'''

for i in range(1,5):
    for j in range(1, i+1):
        print(j,end="")
    print()

'''
#TASK -- 10
1234
123
12
1
'''
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

'''
#TASK --- 11
   *
  ***
 *****
*******
'''

for i in range(1,5):
    for j in range(4-i):
        print(" ",end="")
    for j in range(2*i - 1):
        print("*",end="")
    print()    
        
    
#reverse a string
given_str="hello"
rev=""
for x in given_str:
    rev=x+rev
print(rev)
































