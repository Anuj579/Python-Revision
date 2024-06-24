s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(s)
print(len(s)) # length will be 2 because 20 and 20.0 are same
