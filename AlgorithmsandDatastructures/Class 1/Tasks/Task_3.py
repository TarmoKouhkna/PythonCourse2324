# Given a number, write a recursive function to calculate a sum of it's digits. ex: "12345498741651"

def sum_of_digits(n):
    # Base case: If the number is a single digit, return it
    if n < 10:
        return n
    # Recursive case: Sum the last digit with the sum of digits of the remaining number
    else:
        return n % 10 + sum_of_digits(n // 10)


# Example usage
number = 12345498741651
result = sum_of_digits(number)
print("Sum of digits:", result)
