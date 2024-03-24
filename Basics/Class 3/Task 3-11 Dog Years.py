"""
Write a Python program to calculate a dog's age in dog years.
Note: For the first two years, a dog year is equal to 10.5 human years.
After that, each dog year equals 4 human years.
"""

years = float(input("Enter a dogs age: "))
if years <= 2:
    dog_human = years * 10.5
else:
    dog_human = ((years - 2) * 4) + 21

print("The dogs age in human years is: ", dog_human)

