numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end=" ")
print()

numbers = (1, 2, 3, 4, 5)

for number in reversed(numbers):
    print(number, end=" ")
print()

my_dic = {'A': 1, 'B': 2, 'C': 3}

for key, value in my_dic.items():
    print(f"{key}: {value}")