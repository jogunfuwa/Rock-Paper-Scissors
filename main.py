import random

print("Welcome to the Game")
print("Enter choice \n R for Rock, \n P for paper, and \n S for scissor \n")

user_choice = input("Enter a choice -->")
possible_actions = ["R", "P", "S"]
computer_choice = random.choice(possible_actions)
print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")
elif user_choice == "R":
    if computer_choice == "S":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_choice == "P":
    if computer_choice == "R":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_choice == "S":
    if computer_choice == "P":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
