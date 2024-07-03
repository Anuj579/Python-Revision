class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self,num):
        return self.n + num.n
    
a = Number(2)
b = Number(4)

print(a+b)