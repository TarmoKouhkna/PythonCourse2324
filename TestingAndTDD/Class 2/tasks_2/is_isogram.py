def is_isogram(word):
    word = word.lower()  # Convert to lowercase for case insensitivity
    iso = set()    # iso = set() is used to create an empty set called iso.
    for letter in word:
        if letter.isalpha():
            if letter in iso:
                return False
            iso.add(letter)
    return True
