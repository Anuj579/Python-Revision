'''
1 for snake
-1 for water
0 for gun
'''

import random

def play_game():
    # Computer randomly chooses one of the options
    computer = random.choice([0, 1, -1])

    # Player input
    player = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

    # Dictionary to map player input to corresponding numbers
    playerDict = {"s": 1, "w": -1, "g": 0}

    # Check if the player input is valid
    if player in playerDict:
        playerNum = playerDict[player]

        # Dictionary to map numbers to choices
        choices = {1: "Snake", -1: "Water", 0: "Gun"}

        # Display the choices made by the computer and the player
        print("Computer chose:", choices[computer])
        print("You chose:", choices[playerNum])

        # Determine the winner
        if computer == playerNum:
            print("It's a tie")
        else:
            if (computer == 1 and playerNum == -1):
                print("You Lose")
            elif (computer == -1 and playerNum == 1):
                print("You Win")
            elif (computer == 0 and playerNum == 1):
                print("You Lose")
            elif (computer == 1 and playerNum == 0):
                print("You Win")
            elif (computer == 0 and playerNum == -1):
                print("You Win")
            elif (computer == -1 and playerNum == 0):
                print("You Lose")
            else:
                print("Something went wrong!")
    else:
        print("Invalid input. Please enter 's' for Snake, 'w' for Water, or 'g' for Gun.")

# Main loop
while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break

print("Thank you for playing!")
