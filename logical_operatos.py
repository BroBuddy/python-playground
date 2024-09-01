temperature = 20
is_sunny = False

if temperature >= 25 and is_sunny:
    print("It is hot and sunny outside")
elif temperature <= 0 and is_sunny:
    print("It is cold and sunny outside")
elif 25 > temperature > 0:
    print("It is warm outside")
elif temperature >= 25 and not is_sunny:
    print("It is hot and cloudy outside")
elif temperature <= 0 and not is_sunny:
    print("It is cold and cloudy outside")