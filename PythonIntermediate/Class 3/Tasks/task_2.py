import re


def check_phone_number(phone_number):
    # Regular expression pattern for Estonian phone number format: +372 XXXXXXXX
    pattern = r'^\+372\s\d{7}'


    # Check if the phone number matches the pattern
    if re.match(pattern, phone_number):
        return True
    else:
        return False


# Test cases
phone_numbers = ["+372 5177400", "+372 5181100", "+370 5177111"]

for number in phone_numbers:
    if check_phone_number(number):
        print(f"{number} is a valid Estonian phone number")
    else:
        print(f"{number} is not a valid Estonian phone number")

