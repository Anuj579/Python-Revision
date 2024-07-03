class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()  # this is also run the constructor of programmer function
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a) # prints the a attribute


# o = Programmer()
# print(o.a) # prints the a attribute
# print(o.b) # prints the b attribute
# # print(o.c) # shows an error because there is no c attribute

o = Manager()
print(o.a, o.b, o.c) 
