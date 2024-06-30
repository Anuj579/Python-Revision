class Microsoft:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

a = Microsoft("Anuj", 120000000, 121102)
print(a.name, a.company, a.salary, a.pin)

b = Microsoft("Raj", 800000, 132204)
print(b.name, b.company, b.salary, b.pin)
