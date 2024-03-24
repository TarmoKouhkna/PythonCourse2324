"""
Write a Python program that accepts a string and calculates the number of digits and letters.
Use this to help to understand if character is numeric:
https://www.w3schools.com/python/ref_string_isnumeric.asp
"""

string = input("Insert string: ")

digit_count = 0
letter_count = 0

for char in string:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        letter_count += 1

print(f"Letters in string: {letter_count}")
print(f"Numbers in string: {digit_count}")
