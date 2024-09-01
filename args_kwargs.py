total = 0

def add_nums(*args):
    # print(type(args))
    total = 0
    for num in args:
        total += num
    return total

result = add_nums(1, 2, 3, 4, 5)
print(result)
print()

#############################################################

def print_address(**kwargs):
    # print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(
    street="Hauptstr. 1",
    city="Berlin",
    state="Berlin",
    zip='12345'
)
print()

#############################################################

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value)

shipping_label(
    'Herr',
    'John',
    'Doe',
    street="Hauptstr. 1",
    city="Berlin",
    state="Berlin",
    zip='12345'
)