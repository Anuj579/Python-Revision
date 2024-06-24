# Program to find whether a student has passed or failed if it requires a total of 40% and and at least 33% in each subject to pass. 3 subjects and take marks from the user

m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

total_percentage = (m1+m2+m3)/3 #total percentage

if total_percentage>=40 and m1>=33 and m2>=33 and m3>=33:
    print("You have passed: ", total_percentage)
else:
    print("You have failed: ", total_percentage)