class Employee:
    language = "Python" #This is a class attribute
    salary = 1000000

    def __init__(self, name, language, salary): #dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod   #We can use this if we dont want to use the class attribute in a method
    def greet():
        print("Good Morning")

Anuj = Employee("Anuj", "JavaScript", 1200000)

print(Anuj.name, Anuj.language, Anuj.salary)
