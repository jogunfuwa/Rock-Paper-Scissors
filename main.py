from random import randint

print("Welcome to the Game")
print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n")

#  list of play options
t = ["R", " P", "S"]


# assign a random play to the computer
computer = t[randint(0, 2)]


player = False

while player == False:

    player = input("R, P, S,? --")
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
        print("That's not a valid play. Check your options!")

    player = False
    computer = t[randint(0, 2)]
