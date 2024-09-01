import random
import time

options = ("rock", "paper", "scissors")
player_points = 0
computer_points = 0

while player_points < 3 and computer_points < 3:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    time.sleep(0.5)

    print()
    print(f"Player chooses: {player}")
    print(f"Computer chooses: {computer}")
    print()

    if player == computer:
        print("It's a tie!")
    elif player == options[0] and computer == options[2]:
        print("You win!")
        player_points += 1
    elif player == options[1] and computer == options[0]:
        print("You win!")
        player_points += 1
    elif player == options[2] and computer == options[1]:
        print("You win!")
        player_points += 1
    else:
        print("You lose!")
        computer_points += 1

print()
print(f"Player points: {player_points}")
print(f"Computer points: {computer_points}")