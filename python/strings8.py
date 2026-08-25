#strings -- they are immutable, collection of characters and number denoted with single or double qoutes

a="hi"
print(a[0])

b="hello"
#inbuilt functions---
print(b[-4])
print(b.upper())
print(len(b))
print(b.count("l"))

#slicing the string
#syntax ---- var[start:stop:step]
a="hello i'm 'Agent'"
print(a[::])#whole string as output
print(a[::-1])#reverse string using slicing
print(a[-6:-1])
print(a[6:9])


#LIST -- collection of different elements , it is mutable, it is denoted by []
l=[] #empty list without funct
print(type(l))

a=list() #empty list with func
print(type(a))

lis=[1,"hi",[10,20],True,3.0]
print(lis)
lis[1]="hello"
print(lis)
print(lis[2][0])

A=[10,[8,[4,0],9,6],20]
print(lis[2][1][1])


#append() --- var.append(value)
lis=[1,2,3,4]
lis.append(5)
print(lis)




#TASK -- square a list into new list
a=[1,2,3,4,5]
b=[]
for i in a:
    b.append(i**2)
print(a)
print("square of list is:",b)

#TASK -- fiter the list using even number upto 10 into new list
n=[1,2,3,4,5,6,7,8,9,10]
m=[]
for i in n:
    if i%2==0:
        m.append(i)
print(n)
print("even number from the list are:",m)

#TASK --fiter the list using odd number upto 10 into new list
n=[1,2,3,4,5,6,7,8,9,10]
m=[]
for i in n:
    if i%2!=0:
        m.append(i)
print(n)
print("Odd number from the list are:",m)

#TASK --sum of n numbers program by taking user input into list and then sum the list
x = int(input("Enter a number: "))
y = []
for i in range(1,x+1):
    y.append(i)
print("list:",y)
print("sum =",sum(y))












          


