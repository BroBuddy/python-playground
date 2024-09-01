import random

def spin_row():
    symbols = ['🍒', '🍇', '🍊', '🔔', '⭐']

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
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100

    print("##############################")
    print("Python Slot Machine")
    print("##############################")
    print("Symbols: 🍒 🍇 🍊 🔔 ⭐")
    print("##############################")

    while balance > 0:
        print(f"Your current balance: ${balance}")

        bet = input("> Place your bet amount: ")

        if not bet.isdigit():
            print("##############################")
            print(f"{bet} is not a valid amount.")
            print("##############################")
            continue

        bet = int(bet)

        if bet > balance:
            print("##############################")
            print(f"Bet must be smaller or equal to ${balance}")
            print("##############################")
            continue

        if bet <= 0:
            print("##############################")
            print(f"Bet must be greater than 0")
            print("##############################")
            continue

        balance -= bet

        row = spin_row()
        print("##############################")
        print("Spinning...")
        print_row(row)
        print("##############################")

        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout}")
            balance += payout
        else:
            print("Sorry, you lost this round")

        print("##############################")
        play_again = input("> Do you wanna spin again (y/n): ").lower()

        if play_again != 'y':
            break

    print("############################################")
    print(f"Game over, your final balance is ${balance}")
    print("############################################")

if __name__ == '__main__':
    main()