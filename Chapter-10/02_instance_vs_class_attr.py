class Employee:
    language = "Python" #This is a class attribute
    salary = 1000000

Anuj = Employee()
Anuj.language = "JavaScript" #This is an instance attribute
print(Anuj.language, Anuj.salary)   #Instance attribute take preference over class attributes