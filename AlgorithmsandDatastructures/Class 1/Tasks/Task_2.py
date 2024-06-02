# Given a string, use recursion to reverse it.

def reverse_string_recursive(s):
    # Base case: if the string is empty or has only one character, return it as is
    if len(s) <= 1:
        return s
    # Recursive case: return the last character plus the reverse of the rest of the string
    return s[-1] + reverse_string_recursive(s[:-1])


# Example usage:
input_string = "hello world !"
reversed_string = reverse_string_recursive(input_string)
print(reversed_string)
