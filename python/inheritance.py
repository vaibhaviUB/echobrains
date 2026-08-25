'''
6. Inheritance
---------------

class A():
    def __init__(self):
        print("cons1")
class B(A):
    def __init__(self):
        super().__init__() #to access both the super and sub class constructors just be creating object for subclass
        print("cons2")
class C(B):
    def __init__(self):
        super().__init__() #to access both the super and sub class constructors just be creating object for subclass
        print("cons3")
obj=C()


1...single inheritance
class A()
class B(A)
2.multilevel inheritance
class A()
class B(A)
class C(B)
3...multiple inheritance
class C(A,B)
4...Hierarchical inheritance
class A()
class B(A)
class C(A)
5...Hybrid inheritance
combination of multiple and hierarchical inheritance



1. single----

print("single inheritance--")
class good():
    def __init__(self):
        print("Greetings")
class morning(good):
    def __init__(self):
        super().__init__()
        print("Good morning")
a=morning()


2. multilevel inheritance----

print("Multilevel--")
class one():
    def __init__(self):
        print("Im class one")
class two(one):
    def __init__(self):
        super().__init__()
        print("Im class two")
class three(two):
    def __init__(self):
        super().__init__()
        print("Im class three")
b=three()


3.multiple

print("multiple inh--")
class Father():
    def dad(self):
        print("Father's property")
class Mother():
    def mom(self):
        super().__init__()
        print("Mother's Property")
class child(Father,Mother):
    def __init__(self):
        super().__init__()
        print("Im the kid")
c=child()
c.dad()
c.mom()

using constructor---
class Father():
    def __init__(self):
        print("Father's property")
        super().__init__()
class Mother():
    def __init__(self):
        print("Mother's Property")
class child(Father,Mother):
    def __init__(self):
        super().__init__()
        print("Im the kid")
c=child()


4.Hierarchical inheritance

print("hierarchical--")
class Animal:
    def eat(self):
        print("Animal eats food")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Cat(Animal):
    def meow(self):
        print("Cat meows")
d=Dog()
d.eat()
d.bark()
c=Cat()
c.eat()
c.meow()


5.Hybrid--

print("hybrid----")
class School:
    def study(self):
        print("Students study")
class Teacher(School):
    def teach(self):
        print("Teacher teaches")
class Student(School):
    def learn(self):
        print("Student learns")
class Monitor(Teacher, Student):
    def manage(self):
        print("Monitor manages the class")
m = Monitor()
m.study()
m.teach()
m.learn()
m.manage()


Tasks---
1. create a class called fruit, craete a var called colro using __init__ method
craete a object called apple "pass the color variable as a aparameter through object"
'''
class fruit():
    def __init__(self,color):
        self.color=color
        print("the color is :",self.color)
apple=fruit("red")
banana=fruit("yellow")

'''

2. create a class called tecaher
craete a variable=name and register number using constructor
create a function called display which should display the name and register number of the teacher
create t1 and t2 object and pass the name and reg no value through object.
'''
class teacher():
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print("name of the teacher:",self.name)
        print("register number of teacher:",self.reg)
t1=teacher("vaibhavi",20)
t2=teacher("kavana",21)
t1.display()
t2.display()

'''
3. create a class called claculator
craete 2 variable a and b
craete a function called add, sub, mul,div all functions should take 2 variables as parameter
pass the a and b value through object()
'''

class Calculator:
    def add(self, a, b):
        print("Addition:", a + b)
    def sub(self, a, b):
        print("Subtraction:", a - b)
    def mul(self, a, b):
        print("Multiplication:", a * b)
    def div(self, a, b):
        print("Division:", a / b)
c = Calculator()
c.add(10, 5)
c.sub(10, 5)
c.mul(10, 5)
c.div(10, 5)






        
    





























