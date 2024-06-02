def integer_to_binary(d):
    # Ensure the integer is non-negative
    if d < 0:
        raise ValueError("Input must be a non-negative integer")

    # Create an empty binary string
    binary_string = ""

    # Special case for 0
    if d == 0:
        return "0"

    # Process the integer to build the binary string
    while d > 0:
        r = d % 2
        if r == 1:
            binary_string = "1" + binary_string
        else:
            binary_string = "0" + binary_string
        d = d // 2

    return binary_string


# Get user input
try:
    user_input = int(input("Enter a non-negative integer: "))
    binary_representation = integer_to_binary(user_input)
    print(f"The binary representation of {user_input} is: {binary_representation}")
except ValueError as e:
    print(e)
