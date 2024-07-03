class Employee: # Base Class
    company = "ITC"
    name = 'Xyz'
    def show(self):
        print(f"The name of the Employee is {self.name} and the compnay is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"The language used by the coder is {self.language}")


class Programmer(Employee, Coder): # Derived Class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The language of the Employee is {self.language}")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()