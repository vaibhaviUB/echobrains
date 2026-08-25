'''
polymorphism
-------------

1. method overriding--- 2 same methods, child class will override 

class father():
    def age(self):
        print("im 50")
class son(father):
    def age(self):
        print("im 20")
obj=son()
obj.age()

2. method overloading--- is it possile in python...? - possible indirectly by using default parameters and using *args
'''


