import random
import time
import sys

def main():
    age = 42
    money = age
    win_streak = 3
    dots = 3

    start_welcome(money)
    ready_check()
    sleeper(dots)
    money = number_suessing_game(money, age)
    ready_check()
    sleeper(dots)
    money = rps_game(money, win_streak)
    ready_check()
    sleeper(dots)
    money = hangman_game(money)
    ready_check()
    sleeper(dots)
    money = slot_machine_game(money)
    sleeper(dots)
    happy_birthday(money)

def show_money(money):
    print()
    print(f"💰 Current credit: {money:.2f}€")

def generate_header(icon, title, text, subtext = ""):
    print()
    print("***********************************")
    print(f"{icon} {title}")
    print("***********************************")
    print(f"{text}")
    print(f"{subtext}")

def start_welcome(money):
    generate_header(
        "🎉",
        "Happy Birtday Gaming",
        "You have to complete 4 really tough games.",
        f"Unfortunately, for every mistake you will lose {1:.2f}€.")
    show_money(money)
    
def ready_check():
    print()
    ready = input("> Do you wanna play a game? (y/n) ").lower()

    if ready != "y":
        print("❕ Your answer is invalid.")
        ready = input("> Do you wanna play a game? (y/n) ").lower()

def sleeper(dots):
    for _ in range(dots, 0, -1):   
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.3)
    print()

def number_suessing_game(money, age):
    lowest_num = 1
    highest_num = age * 12
    answer = random.randint(lowest_num, highest_num)
    guesses = 0
    is_running = True

    generate_header(
        "🔢",
        "Number guessing game",
        f"Wow, {age} years are equal to {highest_num} months.",
        f"Select a number between {lowest_num} and {highest_num}.")
    show_money(money)

    while is_running:
        print()
        guess = input("> Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)

            if guess < lowest_num or guess > highest_num:
                print("❕ That number is out of range.")
                print(f"Select a number between {lowest_num} and {highest_num}.")
            elif guess < answer:
                time.sleep(0.5)
                money -= 1
                print(f"⬆️ Try higher!")
                guesses += 1
            elif guess > answer:
                time.sleep(0.5)
                money -= 1
                print(f"⬇️ Try lower!")
                guesses += 1
            else:
                print()
                print("***********************************")
                print(f"✅ Correct, the answer is '{answer}'.")
                print(f"Number of guesses: {guesses}.")
                show_money(money)
                is_running = False
        else:
            print("❕ Invalid guess")
            print(f"Select a number between {lowest_num} and {highest_num}.")
    
    return money

def rps_game(money, win_streak):
    generate_header(
        "🎲",
        "Rock / Paper / Scissors",
        "A rock beats scissors, scissors beat paper by cutting it, and paper beats rock by covering it.")
    show_money(money)

    options = ("rock", "paper", "scissors")
    player_points = 0
    computer_points = 0

    while player_points < win_streak and computer_points < win_streak:
        player = None
        computer = random.choice(options)

        while player not in options:
            print()
            player = input("> Enter a choice (rock, paper, scissors): ")

        time.sleep(0.5)

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
    show_money(money)

    return money

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

def hangman_game(money): 
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

    generate_header(
        "🧔",
        "Hangman - Marvel Edition",
        f"Guess the hero with {len(answer)} letters.")
    show_money(money)

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

    return money

def spin_row():
    symbols = ['🍒', '🍇', '🍊', '🔔', '💰']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍇':
            return bet * 4
        elif row[0] == '🍊':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '💰':
            return bet * 20
    return 0

def slot_machine_game(money):
    generate_header(
        "🎰",
        "Slot Machine",
        "In the last game you can invest your money wisely.",
        "Symbols: 🍒 = x3, 🍇 = x4, 🍊 = x5, 🔔 = x10, 💰 = x20")
    show_money(money)

    is_running = True

    while money > 0 and is_running:
        print()
        bet = input("> Place your bet amount: ")

        if not bet.isdigit():
            print("***********************************")
            print(f"❕ {bet} is not a valid amount.")
            print()

        bet = int(bet)

        if bet > money:
            print("***********************************")
            print(f"❕ Bet must be smaller or equal to {money:.2f}€")
            print()

        if bet <= 0:
            print("***********************************")
            print(f"❕ Bet must be greater than 0")
            print()

        money -= bet

        row = spin_row()
        print()
        print("Spinning...")
        print_row(row)
        print()

        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"✅ You won {payout:.2f}€.")
            money += payout
        else:
            print("❌ Sorry, you lost this round.")

        show_money(money)
        play_again = input("> Do you wanna spin again (y/n): ").lower()

        if play_again == 'n':
            is_running = False
            break

    return money

def happy_birthday(money):
    generate_header(
        "🥳",
        f"Prince Atix won: {money:.2f}€",
        "Happy Birthday to You!")

    print(r'''
                   |_|  /| |_)|_)\_/
                   | | /-| |  |   /
               _     _ ___     _
              |_) | |_) |  |_|| \  /| \_/
              |_) | | \ |  | ||_/ /-|  /

                               .--------.
                             .: : :  :___`.
                           .'!!:::::   \_\ `.
                      : . /%O!!:::::::: \_\. \
                     [""]/%%O!!:::::::::  : . \
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.'\%%OO!!!::::::::::::/
         :    .   /        \%OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     /__\`-.
        \::::::/ ||)|/|)|)|\|           /
---------`::::'--|._ ~**~ _.|----------( -----------------------
           )(    |  `-..-'  |           \    ______
           )(    |          |,--.       ____/ /  / \ ,-._.-'
        ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-.
          ''')
    
    print()
    
if __name__ == '__main__':
    main()