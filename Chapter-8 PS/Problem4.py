# Write a recursive function to find the sum of first n natural numbers

'''
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n) = sum(n-1) + n
''' 

# def sum_of_natural_no(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum= n + sum_of_natural_no(n-1)
#     return sum

# n = int(input("Enter a number: "))
# print(sum_of_natural_no(n)) 

def sum(n):
    if n ==1:
        return 1
    return sum(n-1)+n

n = int(input("Enter a number: "))
print(sum(n))