# Enter your height in meters e.g., 1.55
height = float(input("Enter Your Height : "))
# Enter your weight in kilograms e.g., 72
weight = int(input("Enter your Weight : "))
# 🚨 Don't change the code above 👆
bmi = float(weight/(height**2))

if bmi <18.5:
  print(f"Your BMI is {bmi}, you are underweigh.")

elif bmi >=30:
  print(f"Your BMI is {bmi}, you are obese.")

elif bmi >=25:
  print(f"Your BMI is {bmi}, you are slightly overweight.")

elif bmi >= 18.5:
  print(f"Your BMI is {bmi}, you have a normal weight.")

else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
