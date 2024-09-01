# for x in range(1, 11):
#     print(x)

# for x in reversed(range(1, 11)):
#     print(x)

for x in range(1, 21, 2):
    if x == 5:
        continue
    if x == 13:
        break
    else:
        print(x)