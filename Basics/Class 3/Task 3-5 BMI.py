# Write program that calculates body mass index
# (bmi = weight / (height*height)).
# Weight(kg) and height(meters) would be passed by user input
#
# if bmi <= 18.5 print "Underweight"
# if bmi <= 25.0 print "Normal"
# if bmi <= 30.0 print "Overweight"
# if bmi > 30 print "Obese"

weight = float(input("Input the weight in kg: "))
height = float(input("Input the height in m: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {round(bmi, 2)}")

if 0 < bmi <= 18.5:
    print("Underweight")
elif bmi <= 25.0:
    print("Normal")
elif bmi <= 30.0:
    print("Overweight")
elif bmi > 30:
    print("Obese")
