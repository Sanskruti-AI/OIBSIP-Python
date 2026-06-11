print("===== BMI CALCULATOR =====")

weight = float(input("Enter your weight in kg: "))
height_m = float(input("Enter your height in meters: "))

if height_m <= 0:
    print("Height must be a positive number.")
    raise SystemExit(1)

bmi = weight / (height_m * height_m)

print("\n===== RESULT =====")
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
