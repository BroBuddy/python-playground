user_name = input("Enter an username: ")

if len(user_name) > 12:
    print("Your username can't be more than 12 characters")
elif not user_name.find(" ") == -1:
    print("Your username can't contain spaces")
elif not user_name.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {user_name}")