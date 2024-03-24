"""
Create a function that checks if a given string is a palindrome
(reads the same backward as forward).
Use this function to check whether a user-inputted string is a palindrome.
"""


# In this function we use the string slice [::-1] to reverse the string and compare it with the original one.
# If they are the same, we return True, otherwise False.
# We then ask the user to enter a word and call the is_palindrome function, printing a message indicating
# whether the entered word is a palindrome.
# Let's test it! This function quickly determines whether a word is a palindrome or not.

# saippuakivikauppias

def is_palindrome(string):
    reverse = string[::-1]
    if string == reverse:
        return True
    else:
        return False


user_input = input("Input string: ")
if is_palindrome(user_input):
    print(f"{user_input} is palindrome :-)")
else:
    print(f"{user_input} is not a palindrome :/")
