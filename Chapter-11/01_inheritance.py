class Employee: # Base Class
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The language of the Employee is {self.language}")

class Programmer(Employee): # Derived Class
        company = "ITC Infotech"
        def showLanguage(self):
            print(f"The language of the Employee is {self.language}")


a = Employee()
b = Programmer()
print(a.company)
print(b.company)