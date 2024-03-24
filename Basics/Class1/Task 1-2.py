# This algebra monster, equation to solve a3 – b3, formula: (a – b)(a2 + ab + b2)

print("Algebra monster solution")
a = int(input("Please enter value for A:"))
b = int(input("Please enter value for B:"))

solution = (a - b)*(a*a + a*b + b*b)
solution2 = a**3 - b**3

print("Algebra monster solution is ", solution, "or", solution2)
