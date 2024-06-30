class Calculator:
    def __init__(self, num):
        self.num = num
    
    def square(self):
        print(f'Square of {self.num} is {self.num**2}')

    def cube(self):
        print(f'Cube of {self.num} is {self.num**3}')

    def squreRoot(self):
        print(f'Square root of {self.num} is {self.num**1/2}')

n = int(input("Enter a number: "))
a = Calculator(n)
a.square()
a.cube()
a.squreRoot()