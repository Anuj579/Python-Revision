# Program to find whether a username contains less than 10 characters or no

username = input("Enter username: ")
if len(username) < 10:
    print("Username have less than 10 characters")
else:
    print("Username have 10 or more characters")