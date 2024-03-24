"""
Write a Python program to count the number of even and odd numbers in a series of numbers:
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_count = 0
odd_count = 0

for numbers in numbers:
  if numbers % 2 == 0:
    even_count += 1
  else:
    odd_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")

