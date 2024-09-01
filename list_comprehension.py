doubles = [x * 2 for x in range(1, 11)]

# for x in range(1, 11):
#     doubles.append(x * 2)

print(doubles)

fruits= ["apple", "banana", "coconut", "orange"]
fruits = [fruit.upper() for fruit in fruits]

print (fruits)

numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]

print(positive_nums)