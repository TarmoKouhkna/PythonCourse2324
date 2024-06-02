def infinite_range(start, step):
    num = start
    while True:
        yield num
        num += step


# Example usage
start_value = 10
increment = 2
numbers = infinite_range(start_value, increment)

# Print the first 5 numbers
for _ in range(10):
    print(next(numbers))
