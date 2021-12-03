# BMI Calculator

# asking user their dimensions
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")



bmi = int(weight) / float(height) ** 2 # formula for calculating BMI
print("You're BMI is" + str(round(bmi, 2))) #printBMI
