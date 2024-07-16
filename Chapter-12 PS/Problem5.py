n = int(input("Enter a number: "))

tableList = [n*i for i in range(1,11)]

with open('Tables.txt', 'a') as f:
    f.write(f"The Table of {n}: {str(tableList)} \n")