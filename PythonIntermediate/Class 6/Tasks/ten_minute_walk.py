def is_valid_walk(walk):
    # Check if the length of the walk is exactly ten minutes
    if len(walk) != 10:
        return False

    # Count the number of steps in each direction
    directions = {'n': 0, 's': 0, 'e': 0, 'w': 0}
    for direction in walk:
        directions[direction] += 1

    # Check if the number of north steps equals the number of south steps
    # and the number of east steps equals the number of west steps
    if directions['n'] != directions['s'] or directions['e'] != directions['w']:
        return False

    # If all conditions are met, return True
    return True


# Test cases
print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # True
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))  # False
print(is_valid_walk(['w']))  # False
print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # False
