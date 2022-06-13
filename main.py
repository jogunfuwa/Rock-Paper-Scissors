from random import randint
import random

print("Welcome to the Game")
print("Enter choice \n R for Rock, \n P for paper, and \n S for scissors \n")

player = False

while player == False:

    player = input("Enter a choice -->")
    possible_actions = ["R", "P", "S"]
    computer = random.choice(possible_actions)
    print(f"\nPlayer chose {player}, computer chose {computer}.\n")

    if player == computer:
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
            print("Thank you for playing")
            break
    elif player == "P":
        if computer == "S":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
            print("Thank you for playing")
            break
    elif player == "S":
        if computer == "R":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
            print("Thank you for playing")
            break
    else:
        print("That's not a valid play. Check your spelling!")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = random.choice(possible_actions)
