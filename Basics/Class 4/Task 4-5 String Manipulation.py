# Write a function that accepts a string and replaces all spaces with underscores.
# Additionally, convert the string to lowercase.
# Display the modified string.

"""
In this function:
We use the replace() method to replace all spaces with "_".
We use the lower() method to make the entire string lowercase.
We return the new modified string.
Then we take user input, process it with the function, and display the result.
"""


def modify_string(string):
    new_string = string.replace(" ", "_")
    new_string = new_string.lower()
    return new_string


user_input = input("Please input a string: ")
modified_string = modify_string(user_input)
print(modified_string)
