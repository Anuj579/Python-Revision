# Program to detect spam comment 
s1= 'make a lot of money'
s2= 'buy now'
s3= 'subscribe this'
s4= 'click this'

comment = input("Add comments here: ")

if s1 in comment or s2 in comment or s3 in comment or s4 in comment:
    print("This comment is spam")
else :
    print("This comment is not spam")