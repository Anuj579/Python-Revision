class Employee:
    language = "Python" #This is a class attribute
    salary = 1000000
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod   #We can use this if we dont want to use the class attribute in a method
    def greet():
        print("Good Morning")

Anuj = Employee()
print(Anuj.language, Anuj.salary)

Anuj.greet()
Anuj.getInfo()
# Employee.getInfo(Anuj) #This and above line are same. It will give the same result