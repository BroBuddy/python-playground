foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

for price in prices:
    total += price

print("----- Your Cart -----")
print(f"Foods: {foods}")
print(f"Prices: {prices}")
print("----- ----- -----")
print(f"Your total is: ${total}")