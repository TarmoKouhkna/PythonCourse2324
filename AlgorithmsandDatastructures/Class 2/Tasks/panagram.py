def is_pangram(sentence):
    # Create a set to store the unique letters found in the sentence
    letters = set()

    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is an alphabet letter (ignore numbers and punctuation)
        if char.isalpha():
            # Add the lowercase version of the letter to the set
            letters.add(char.lower())

    # Check if the set of letters contains all 26 letters of the alphabet
    return len(letters) == 26


# Test cases
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("The quick brown fox jumps over the"))  # False
