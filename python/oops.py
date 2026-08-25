'''
OOps -- oops is a programming paradigm based on the concept of objects.
object- instance of a class, represent real world entity
class- blueprint of objects

it helps in :
organizing code better
reusing the code(inheritance)
securig data(encapsulation)
handling complexity(abstraction, polymorphism)

1. creating class-

syntax-
class classname():
    methods
create object to access

intervie q-- what is diff between method and function
method- dependent ,it is inside the class and dependent on class
fucnt- indepndent and can be accessed directly

class A():
    def fun(self): #self is used for relation between class and method for proof
        print("hello")
a=A()
a.fun()

2. empty class
class A():
    pass


3.
class math():
    def add(self, a, b):
        print("addition:",a+b)
    def sub(self, a, b):
        print("subtraction:",a-b)
x=math()
x.add(1,1)
x.sub(2,1)


4. constructor---
without constructor you cant pass the argumnt in the menthod calling,
when u dont have to call again and again
whenever the object created it executes automatically

class math():
    def __init__(self, name, age):  #special method - constructor
        self.name=name
        self.age=age
        print("im a constructor")
    def sub(self):
        print("name:" , self.name)
x=math("vibe",20)
x.sub()


5. create a class called student
create a var name and register number using constructor
create a func called display which should display the name and regsiter number of the student


class student():
    def __init__(self, name, num):
        self.name=name
        self.num=num
    def display(self):
        print("name of the student:", self.name)
        print("register number of the student:", self.num)
n=student("vaibhavi",100)
n.display()
m=student("kavana",101)
m.display()
























    
    






