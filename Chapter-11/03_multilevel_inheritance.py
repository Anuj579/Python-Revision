class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # prints the a attribute
# print(o.b) # shows an error because there is no b attribute 

o = Programmer()
print(o.a) # prints the a attribute
print(o.b) # prints the b attribute
# print(o.c) # shows an error because there is no c attribute

o = Manager()
print(o.a) # prints the a attribute
print(o.b) # prints the b attribute
print(o.c) # prints the c attribute