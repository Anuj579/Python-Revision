a= int(input("Enter you age: "))

# If statement no-1
if(a%2==0):
    print("Your age is even")
# End of If statement no-1


# If statement no-2
if (a>=18):
    print("You are eligible to vote")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0 which is not a valid age")
    
else:
    print("You are not eligible to vote")
# End of If statement no-2

print("End of program")