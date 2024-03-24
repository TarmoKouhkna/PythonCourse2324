# Write a program that would
# ask user to input text
# split the received text in half and
# print first part normally and a second part reversed to output.

text = input("Please enter text:")
half = len(text) // 2
first_half = text[:half]
second_half = text[half:]
second_half_reversed = second_half[::-1]

print(first_half)
print(second_half_reversed)
