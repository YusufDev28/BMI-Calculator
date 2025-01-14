# BMI Calculator

age = 26
weight = float(input("Weight: "))
height = float(input("Height: "))
overweight = False

bmi = weight / (height * height)
if bmi < 18.5:
    print("You are in underweight")
elif bmi >= 18.5 and bmi < 25:
    print("You are healthy")
else:
    print("You are overweight")