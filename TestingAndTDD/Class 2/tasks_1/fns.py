# Task 1: Write a function to add two numbers
def add(a, b):
    return a + b


# Task 2: Write a function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# Task 3: Write a function to reverse a string
def reverse_string(string):
    return string[::-1]


# Task 4: Write a function to check if a string is a palindrome
def is_palindrome(word):
    return word == word[::-1]


# Task 5: Write a function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Task 6: Write a function to find the maximum element in a list
def find_max(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


# Task 7: Write a function to check if a year is a leap year
def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


# Task 8: Write a function to remove duplicates from a list
def remove_duplicates(lst):
    # Create an empty dictionary to store unique elements
    unique_dict = {}

    # Iterate over the list
    for item in lst:
        # Add each item as a key in the dictionary
        # The value doesn't matter, we can use None
        unique_dict[item] = None

    # Return the keys of the dictionary as a list
    return list(unique_dict.keys())


# Task 9: Write a function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Convert the strings to lowercase and remove any whitespace
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Sort the characters in the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare the sorted strings
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

# Task 10: Write a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


