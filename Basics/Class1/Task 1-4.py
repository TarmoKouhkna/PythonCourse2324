# Equation x2 + y2 + z2 – 3xyz solution

print("Equation solution")
x = int(input("Please enter value for X:"))
y = int(input("Please enter value for Y:"))
z = int(input("Please enter value for z:"))

solution = (x + y + z) * (x*x + y*y + z*z - x*y - y*z - x*z)

print("Equation solution is ", solution)
