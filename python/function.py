#functions
'''
syntax---
def funtion_name():
    func_body
function_name() #funct calling

interview q -
diff between arguments and parameters

1. addition-- 
def add(a,b):
    print(a+b)#print will print but wont store 
add(2,3)
add(5,6)

def add(a,b):
    return(a+b) #to store the value it wont print
x=add(2,3)
print(x)
print(x+5)

def add(a,b):
    return(a+b)#to store the value it wont print
a=int(input("enter a value:"))
b=int(input("enter b value:"))       
x=add(a,b)
print(x)

#argumnets types
def add(a=2,b=5,c=0):#1.default arg
    print(a+b+c)
add(1,2)#2.positional arg
add(a=1)#3.keyword arg

def add(*a):#arbitary
    print(a[0]+a[1])
add(1,2)

'''
def rec(n):
    if n==6:
        return
    else:
        print(n)
        rec(n+1)
rec(0)


def rec(n):
    if n==0:
        return
    else:
        print(n)
        rec(n-1)
rec(5)


n=10
def rec(x):
    x=4
    print(x)
rec(n)
print(n)

n=[1,2,3]
def rec(x):
    x.append(4)
    print(x)
rec(n)
print(n)
    






















