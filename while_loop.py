# name = input("What is your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("What is your name: ")

# print (f"Hello {name}")

age = int(input("What is your age: "))

while age < 0:
    print("Age can't be negative")
    age = input("What is your age: ")

print (f"You are {age} years old")