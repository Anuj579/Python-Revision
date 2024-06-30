class Abc:
    a = 100

x = Abc()
print(x.a) # Prints the class attribute because instance attribute is not present

x.a = 0 # Instance attribute is set
print(x.a) # Prints the instance attribute because instance attribute is present

print(Abc.a) # Prints the class attribute