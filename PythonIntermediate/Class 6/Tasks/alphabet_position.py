def alphabet_position(text):
    result = []
    for char in text:
        if char.isalpha():
            # Convert uppercase to lowercase for consistent indexing
            char = char.lower()
            # Get ASCII value of the character and subtract ASCII value of 'a'
            position = ord(char) - ord('a') + 1
            result.append(str(position))
    return ' '.join(result)


# Test cases
print(alphabet_position("The sunset sets at twelve o' clock."))
# Output: "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
print(alphabet_position("The narwhal bacons at midnight."))
# Output: "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
print(alphabet_position("The result is a wave of standing spectators that travels through the crowd."))
