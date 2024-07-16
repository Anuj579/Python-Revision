a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    print(f"The division of a and b is : {a/b}")

except ZeroDivisionError:
    print("Infinite")
