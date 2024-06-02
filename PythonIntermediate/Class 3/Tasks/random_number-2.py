def random_number_generator(start, end, num_samples):
    import random
    for _ in range(num_samples):
        yield random.randint(start, end)

# You need to call the generator function with the required arguments
# like so: random_number_generator(start, end, num_samples)
# For example:
start = 1
end = 100
num_samples = 10

# Now, you can iterate over the generator's results
for num in random_number_generator(start, end, num_samples):
    print(num)
