from tkinter import *
from tkinter import messagebox
from time import sleep
import random

window = Tk()
window_size = 600
window.geometry(f"{window_size}x{window_size//2}")
window.resizable(False, False)
window.title("Birthday")

age = 42
money = age
win_streak = 3

def get_dialog():
	message_text = "Buddy ist richtig geil"
	messagebox.showinfo(message=message_text, title = "Infos")
        
def create_menu():
    navbar = Menu(window)

    first_tab = Menu(navbar, tearoff=0)
    second_tab = Menu(navbar, tearoff=0)

    navbar.add_cascade(label="Games", menu=first_tab)
    navbar.add_cascade(label="Help", menu=second_tab)

    first_tab.add_command(label="Start page", command=main)
    first_tab.add_separator()
    first_tab.add_command(label="Number guessing game", command=first_screen)
    first_tab.add_command(label="Rock / Paper / Scissors", command=second_screen)

    second_tab.add_command(label="Info", command=get_dialog)
    second_tab.add_command(label="Exit", command=window.quit)

    # window.config(menu=navbar)

def first_screen():
    global money
    lowest_num = 1
    highest_num = age * 12
    is_running = True
    guesses = 0
    answer = random.randint(lowest_num, 2)
    
    frame_color = "red"
    frame = generateFrame(frame_color)

    generateLabel(frame, "Number guessing game", frame_color, frame.winfo_width()/2, 20, 20)
    showMoney(frame, frame_color)
    generateLabel(frame, f"Wow, {age} years are equal to {highest_num} months.", frame_color, frame.winfo_width()/2, 80)
    generateLabel(frame, f"Select a number between {lowest_num} and {highest_num}.", frame_color, frame.winfo_width()/2, 110)

    while is_running:
        guess = input("> Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)

            if guess < lowest_num or guess > highest_num:
                print("❕ That number is out of range.")
                print(f"Select a number between {lowest_num} and {highest_num}.")
            elif guess < answer:
                sleep(0.5)
                money -= 1
                print(f"⬆️ Try higher!")
                guesses += 1
            elif guess > answer:
                sleep(0.5)
                money -= 1
                print(f"⬇️ Try lower!")
                guesses += 1
            else:
                print()
                print("***********************************")
                print(f"✅ Correct, the answer is '{answer}'.")
                print(f"Number of guesses: {guesses}.")
                
                button = Button(frame, text="Start 2nd Game", fg=frame_color, command=winfo_width)
                button.place(x=frame.winfo_width()/2, y=140)

                is_running = False
        else:
            print("❕ Invalid guess")
            print(f"Select a number between {lowest_num} and {highest_num}.")

def second_screen():
    global money
    options = ("rock", "paper", "scissors")
    player_points = 0
    computer_points = 0

    frame_color = "green"
    frame = generateFrame(frame_color)

    generateLabel(frame, "Rock / Paper / Scissors", frame_color, frame.winfo_width()/2, 20, 20)
    showMoney(frame, frame_color)
    generateLabel(frame, "A rock beats scissors, scissors beat paper by cutting it, and paper beats rock by covering it.", frame_color, frame.winfo_width()/2, 80)
    
    try:
        while player_points < win_streak and computer_points < win_streak:
            player = None
            computer = random.choice(options)

            while player not in options:
                print()
                player = input("> Enter a choice (rock, paper, scissors): ")

            sleep(0.5)

            print()
            print(f"Atix chooses: {player}")
            print(f"Buddy chooses: {computer}")
            print()

            if player == computer:
                print("❕It's a tie!")
            elif player == options[0] and computer == options[2]:
                print("✅ You win by smashing!")
                player_points += 1
            elif player == options[1] and computer == options[0]:
                print("✅ You win by covering!")
                player_points += 1
            elif player == options[2] and computer == options[1]:
                print("✅ You win by cutting!")
                player_points += 1
            else:
                print("❌ You lose!")
                money -= 1
                computer_points += 1

        print()
        print("***********************************")
        print(f"Atix has {player_points} points.")
        print(f"Buddy has {computer_points} points.")
                    
        button = Button(frame, text="Start 3rd Game", fg=frame_color, command=third_screen)
        button.place(x=frame.winfo_width()/2, y=140)
    except Exception:
        print("Could not start this game.")

def third_screen():
    words = (
        'antman',
        'wolverine',
        'spiderman',
        'daredevil',
        'punisher',
        'blade',
        'wasp',
        'deadpool',
        'vision',
        'hawkeye',
        'hulk',
        'thor',
        'beast',
        'ironman',
        'rogue',
        'elektra',
        'cyclops',
        'iceman',
        'storm',
        'colossus')
    
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    answer = random.choice(words)
    hint = ["_"] * len(answer)

    frame_color = "orange"
    frame = generateFrame(frame_color)

    generateLabel(frame, "Hangman - Marvel Edition", frame_color, frame.winfo_width()/2, 20, 20)
    showMoney(frame, frame_color)
    generateLabel(frame, f"Guess the hero with {len(answer)} letters.", frame_color, frame.winfo_width()/2, 80)

    try:
        while is_running:
            display_man(wrong_guesses)
            display_hint(hint)

            guess = input("> Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("❕ Invalid input.")
                continue

            if guess in guessed_letters:
                print(f"❕ {guess} is already guessed.")
                continue

            guessed_letters.add(guess)
            
            if guess in answer:
                for index in range(len(answer)):
                    if answer[index] == guess:
                        hint[index] = guess
            else:
                wrong_guesses += 1
                money -= 1

            if "_" not in hint:
                display_man(wrong_guesses)
                print(f"✅ You win with just {wrong_guesses} wrong guess(es).")
                is_running = False
            elif wrong_guesses >= 6:
                display_man(wrong_guesses)
                print(f"❌ You lose, the answer was '{answer}'.")
                is_running = False
    except Exception:
        print("Could not start this game.")

def main():
    frame_color = "orange"
    frame = generateFrame(frame_color)

    generateLabel(frame, "Happy Birtday Gaming", frame_color, frame.winfo_width()/2, 20, 20)
    showMoney(frame, frame_color)
    generateLabel(frame, "You have to complete 4 really tough games.", frame_color, frame.winfo_width()/2, 80)
    
    button = Button(frame, text="Start 1st Game", fg=frame_color, command=first_screen)
    button.place(x=frame.winfo_width()/2, y=140)

def showMoney(frame, frame_color):
    generateLabel(frame, f"Current money: {money:.2f}€", frame_color, frame.winfo_width()/2, 50)

def generateFrame(frame_color):
    frame_color = frame_color
    frame = Frame(window, width=window_size, height=window_size, bg=frame_color)
    frame.place(x=0, y=0)

    frame.grid(row=0, column=0, sticky="NW")
    frame.grid_propagate(0)
    frame.update()

    return frame

def generateLabel(frame, text, frame_color, x, y, size=12):
    label = Label(frame, text=text, bg=frame_color)
    label.config(font=("Verdana", size))
    label.place(x=x, y=y, anchor="center")

def display_man(wrong_guesses):
    hangman_art = {
        0: ("│     │",
            "│     │",
            "│     │"),
        1: ("│  o  │",
            "│     │",
            "│     │"),
        2: ("│  o  │",
            "│  |  │",
            "│     │"),
        3: ("│  o  │",
            "│  |  │",
            "│ /   │"),
        4: ("│  o  │",
            "│  |  │",
            "│ / \\ │"),
        5: ("│  o  │",
            "│ /|  │",
            "│ / \\ │"),
        5: ("│  o  │",
            "│ /|\\ │",
            "│ / \\ │"),
    }

    print("┌─────┐")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("└─────┘")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

create_menu()
main()

window.mainloop()