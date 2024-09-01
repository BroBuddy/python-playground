menu = {
    "pizza": 3.00,
    "popcorn": 5.50,
    "nachos": 6.00,
    "snickers": 2.00,
    "water": 1.50,
    "cola": 3.50,
    "fanta": 2.50,
}

cart = []
total = 0

print("----- MENU -----")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----- ----- -----")

while True:
    food = input("Select an item (q to quit): ").lower()

    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    
print("----- ----- -----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print("----- ----- -----")
print(f"Total is: ${total:.2f}")