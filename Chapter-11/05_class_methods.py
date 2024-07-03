class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

o = Employee()
o.a = 34
o.show()