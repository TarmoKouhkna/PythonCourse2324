import re

text = "Apples are awesome and so are bananas"

# Compile the regex pattern for words starting with "a" or "A"
pattern = re.compile(r'\b[Aa]\w+')

# Find all matches using the findall() function
matches = pattern.findall(text)

# Print the matches
print("Words starting with 'a' or 'A' found in the text:", matches)
