import random

options = ("rock", "paper", "scissors")
running = True

while running:

    computer = random.choice(options)
    player = None

    while player not in options:
        player = input("Pick your play (rock/paper/scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
            print("Draw.")
    elif player == "rock" and computer == "Scissors":
            print("Victory!")
    elif player == "paper" and computer == "rock":
            print("Victory!")
    elif player == "scissors" and computer == "paper":
            print("Victory!")
    else:
            print("Defeat.")

    if not input ("Go again? (y/n)").lower()=="y":
            running = False

print("Thank you for playing!")