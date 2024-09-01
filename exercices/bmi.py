height = float(input("How height are you (in m)?"))
weight = float(input("What is your weight (in kg)?"))

bmi = weight / (height * height)

print(f"Your bmi is: {round(bmi, 1)}")

if bmi > 40:
    weight_status = "Morbidly Obese"
elif bmi > 35:
    weight_status = "Severely Obese"
elif bmi > 30:
    weight_status = "Moderately Obese"
elif bmi > 25:
    weight_status = "Overweight"
elif bmi > 19:
    weight_status = "Healthy Weight"
else:
    weight_status = "Underweight"

print(f"Your current weight status is: {weight_status}")

min_weight = int(18.5 * (height * height))
max_weight = int(24.9 * (height * height))

print(f"Healthy Weight for your height is between {min_weight} and {max_weight} kg.")
