l = [2,5,15,23,45,54,63]

divisibleByFive = lambda x:x%5==0

a = filter(divisibleByFive, l)
print(list(a))