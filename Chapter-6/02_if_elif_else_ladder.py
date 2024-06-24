a= int(input("Enter you age: "))

if (a>=18):
    print("You are eligible to vote")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0 which is not a valid age")
    
else:
    print("You are not eligible to vote")

print("End of program")