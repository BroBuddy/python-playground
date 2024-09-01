prime_numbers = []
number = int(input("Enter a number: "))

def check_factor(number):
    factor = 1

    for num in range(2, number + 1):
        if number % num == 0:
            factor += 1

    return factor == 2

for num in range(1, number + 1):
    if check_factor(num):
        prime_numbers.append(num)

print("--------------------------------")
print(f"Prime numbers found: {prime_numbers}")
print("--------------------------------")
print(f"There are: {len(prime_numbers)} prime numbers")