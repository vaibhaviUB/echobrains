'''
f=open("one.txt","r")
a=f.read()
print(a)
f.close()


with open("one.txt","r") as f:
v=f.read()
    print(v)



f=open("one.txt","w")
f.write("hello\n")
f.write("hi\n")
with open("one.txt","w") as f:


f=open("one.txt","a")
f.write("hiii")
f.close()


with open("one.txt","r") as f:
    v=f.read()
    print(v)


with open("one.txt","w") as f:
    f.write("hello\n")
    f.write("good")
    f.write("hi")
    


#decorator----
def add_chocolate(func):
    def wrapper():
        print("adding chocolate")
        func()
    return wrapper
@add_chocolate
def ice_cream():
    print("Vanilla ice cream")
ice_cream()

#try with inbuilt or static method decorator
#implement real world eg in generator



#generator


def add():
    return 1
    return 2
    return 3
a=add()
print(a)
print(a)


def add():
    yield 1
    yield 2
    yield 3
a=add()
print(next(a))
print(next(a))
print(next(a))
print(next(a)) # this line gives stop iteration error


# create a generator that prints number from 1 to 10
def numbers():
    for i in range(0,11):
        yield i
        
for num in numbers():
    print(num)



#create generator fun. that generates even num from 1 to 20
def n():
    for i in range(2,21,2):
        yield i
for a in n():
    print(a)


#create a generator that genertes square of numbers from 1 to 10
def a():
    for i in range(1,11):
        yield i
for b in a():
    print(b*b)


#regex
import re
text = "My age is 25 and my friends age is 30"
result = re.findall(r"\d+",text)
print(result)


import re
text = "My age is 25 and my friends age is 30"
result = re.sub(r"\d+","X",text)
print(result)


import re
text = "I LOVE Python!!! #coding"
result = re.sub(r"[^a-zA-Z\s]","",text)
print(result)


import re
text = "I LOve Python Coding"
result = re.match("Python", text)
print(result)
'''
















