class Employee:
    language = "Py" #This is a class attribute
    salary = 1000000

Anuj = Employee()
Anuj.name = "Anuj" #This is an instance attribute
print(Anuj.name ,Anuj.language, Anuj.salary)

Rohan = Employee()
Rohan.name = "Rohan Singh"
print(Rohan.name ,Rohan.language, Rohan.salary)

# Here name is instance attribute and salary and language are class attribute as they directly belongs to the class