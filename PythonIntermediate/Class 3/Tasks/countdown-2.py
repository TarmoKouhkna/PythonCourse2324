def countdown(start):
    while start >= 0:
        yield start
        start -= 1


# Print the countdown numbers
for num in countdown(10):
    print(num)
