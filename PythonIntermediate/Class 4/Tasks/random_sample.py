import random


def random_sample(collection, sample_size):
    """
    Generate a random sample of items from a collection.

    Args:
    - collection: The collection of items to sample from.
    - sample_size: The size of the sample to generate.

    Yields:
    - Randomly selected items from the collection.
    """
    # Convert the collection to a list if it's not already
    collection = list(collection)

    # Ensure that the sample size is not greater than the size of the collection
    sample_size = min(sample_size, len(collection))

    # Generate a random sample
    sample = random.sample(collection, sample_size)

    # Yield each item from the sample
    for item in sample:
        yield item

# Example usage
my_collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generate a random sample of size 3
for item in random_sample(my_collection, 3):
    print(item)
