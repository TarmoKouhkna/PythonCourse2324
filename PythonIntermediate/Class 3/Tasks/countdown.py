def countdown(start):
    while start >= 0:
        yield start
        start -= 1


# Example usage
start_value = 10
countdown_gen = countdown(start_value)

# Print the countdown
for num in countdown_gen:
    print(num)
