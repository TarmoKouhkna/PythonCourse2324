import random


def random_number_generator(start, end, count):
    for _ in range(count):
        yield random.randint(start, end)


# Example usage
start_range = 1
end_range = 100
number_count = 5
random_numbers = random_number_generator(start_range, end_range, number_count)

# Print the sequence of random numbers
for num in random_numbers:
    print(num)
