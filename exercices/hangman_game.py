import random

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

def display_man(wrong_guesses):
    print("┌─────┐")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("└─────┘")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():    
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    answer = random.choice(words)
    hint = ["_"] * len(answer)

    print("###############")
    print("Hangman Game")
    print("###############")
    print()
    print(f"Guess the marvel hero with {len(answer)} letters.")

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("> Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("[X] Invalid input.")
            continue

        if guess in guessed_letters:
            print(f"[!] {guess} is already guessed.")
            continue

        guessed_letters.add(guess)
        
        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            print(f"You win with just {wrong_guesses} wrong guess(es).")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            print(f"You lose, the answer was '{answer}'.")
            is_running = False

if __name__ == '__main__':
    main()