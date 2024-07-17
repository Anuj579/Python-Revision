from functools import reduce

l = [2,78,5,6,7]

# greater = lambda a,b : a>b
def greater(a,b):
    if a>b:
        return a
    return b

max = reduce(greater, l)
print(max)