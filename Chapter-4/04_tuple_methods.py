a = (1, 34, "Rahul", 34.6, 34, True, "Anuj")
print(a)

new = a.count(34) # tuple are immutable, we cannot change the tuple but can create new tuple from the existing one
print(new)

i = a.index(34)
print(i)