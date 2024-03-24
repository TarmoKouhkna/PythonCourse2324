# Write a program that
# would ask user to input text and
# print the amount of times the first character of user entered text is repeated.

user_input = input("Please enter text:")

first_char = user_input[0]

count = user_input.count(first_char)

print("Amount of times the first character of user entered text is", count)
