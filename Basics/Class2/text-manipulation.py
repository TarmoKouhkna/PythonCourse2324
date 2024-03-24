example_text = "Blood type is Beer"

# Length of the string
length = len(example_text)
print(length)

# What is the index of this character(first one)
print(f"Index of the letter 'y' in the text is {example_text.index('y')}")

# What is the amount of certain letters in the text
print(f"Amount of letter 'B' in the text is {example_text.count('B')}")

# What is the character in the index 6 of the text
print(f"The character at the index 6 is {example_text[0]}")

# What are the charaters at the index range
print(f"The text in the index range is '{example_text[6:13]}'")

# What are the every second character at the index range
print(f"The text in the index range is '{example_text[6:13:2]}'")
print(f"The text in the index range is '{example_text[::2]}'")
# text[fromIndex:toIndex:step]

# String reversed
print(f"This is the reversed text: {example_text[::-1]}")

# Upper/lower case
print("Converting text to Upper or lowercase")
print(example_text.upper())
print(example_text.lower())
print(example_text.capitalize())

