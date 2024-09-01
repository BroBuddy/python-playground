def show_balance(balance):
    print(f"Your current balance is ${balance:.2f}")

def deposit():
    print("####################")
    amount = float(input("> Enter an amount to be deposited: "))
    
    if amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
    
def withdrawn(balance):
    print("####################")
    amount = float(input("> Enter an amount to be withdrawn: "))
    
    if amount > balance:
        print(f"Amount must be smaller than balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running = True

    while is_running:
        print("####################")
        print("Banking Program")
        print("####################")
        print("1. Show Balance")
        print("1. Deposit")
        print("1. Withdrawn")
        print("1. Exit")
        print("####################")

        choice = input("> Enter your choice (1-4): ")

        if choice == '1':
                show_balance(balance)
        elif choice == '2':
                balance += deposit()
                show_balance(balance)
        elif choice == '3':
                balance -= withdrawn(balance)
                show_balance(balance)
        elif choice == '4':
                is_running = False
        else:
            print("####################")
            print("This is not a valid choice")

    print("####################")
    print("Thank you! Bye")
    print("####################")

if __name__ == '__main__':
    main()