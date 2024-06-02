# Given any integer n, assume it as a list of numbers from 0 to n. Write a recursive functions to calculate SUM of all
# numbers and Multiplication result of all numbers.

def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)


def recursive_multiplication(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * recursive_multiplication(n - 1)


def print_results(n):
    sum_result = recursive_sum(n)
    multiplication_result = recursive_multiplication(n)
    print(f"The sum of numbers from 0 to {n} is: {sum_result}")
    print(f"The multiplication of numbers from 1 to {n} is: {multiplication_result}")


# Example usage:
n = 5
print_results(n)
