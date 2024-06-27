#  1 inch = 2.54 cm

def inch_to_cm(n):
    return n*2.54

n = int(input("Enter a number: "))

print(f"{n} inches = {inch_to_cm(n)}cms")