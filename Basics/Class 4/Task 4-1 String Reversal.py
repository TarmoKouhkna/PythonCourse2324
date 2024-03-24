# Write a function that takes a string as input and returns its reverse.
# Use this function to reverse a string entered by the user.

"""
This function takes a string as input, and uses a for loop to iterate through each character of the string.
It adds each character to the beginning of a new reversed line. Then the function returns the reversed string.
We also ask the user to enter a string and print the result of the reverse_string function for that string
"""


def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


user_input = input("Input string: ")
print(reverse_string(user_input))
