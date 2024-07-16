#The Perfect Guess game

import random
print("Welcome to the Perfect Guess Game")

n = random.randint(1,100)

a = -1
guesses = 1
while(a != n):
    try:
        a = int(input("Guess the number (between 1 to 100): "))
        if a > n:
            print("Lower number please.")
            guesses+=1
        elif a<n:
            print("Higher number please.")
            guesses+=1
    except ValueError:
        print("Invalid input. Please enter a number between 1 to 100 only.")
        
print(f'You have successfully guessed the number {n} in {guesses} attempts.')