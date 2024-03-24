# Implement a function that takes a list of numbers as input
# and returns the sum, average, maximum, and minimum values.
# Use this function on a list entered by the user.

"""
In the function, we:
Calculate the sum using the built-in sum() function.
Calculate the average value using a statistical library.
Find the maximum and minimum.
Return the results as a dictionary.
Then, we ask the user to input a list of numbers, convert it into a list of numbers, and display the results.
"""


# import statistics
#
# def calc_list_stats(numbers):
#   sum_val = sum(numbers)
#   avg_val = statistics.mean(numbers)
#   max_val = max(numbers)
#   min_val = min(numbers)
#
#   results = {
#     "sum": sum_val,
#     "average": avg_val,
#     "maximum": max_val,
#     "minimum": min_val
#   }
#
#   return results
#
# user_list = list(map(int, input("Input list of numbers separated by commas: ").split(",")))
#
# stats = calc_list_stats(user_list)
# print(stats)

# Let's write a function to calculate statistics for a list of numbers without using imports:
# Now we can use this function to calculate statistics for a list of numbers without using imports.

def calc_list_stats(numbers):
    sum_val = 0
    for num in numbers:
        sum_val += num

    avg_val = sum_val / len(numbers)

    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num

    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num

    results = {
        "sum": sum_val,
        "average": avg_val,
        "maximum": max_val,
        "minimum": min_val
    }

    return results


user_list = list(map(int, input("Input list of numbers separated by commas: ").split(",")))

stats = calc_list_stats(user_list)
print(stats)
