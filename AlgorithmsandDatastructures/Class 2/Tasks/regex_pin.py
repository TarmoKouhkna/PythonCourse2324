import re


def validate_pin(pin):
    # Regular expression pattern to match either 4 or 6 digits
    pattern = re.compile(r'^(\d{4}|\d{6})$')
    # Check if the PIN matches the pattern
    if pattern.match(pin):
        return True
    else:
        return False


# Test cases
print(validate_pin("1234"))  # Output: True
print(validate_pin("12345"))  # Output: False
print(validate_pin("a234"))  # Output: False
print(validate_pin("723455"))  # Output: False
