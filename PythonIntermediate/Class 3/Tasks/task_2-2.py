import re

text = "I have 3 apples and 5 oranges"

# Define the regex pattern
pattern = r'\d'

# Find all matches using the findall() function
matches = re.findall(pattern, text)

# Print the matches
print("Digits found in the text:", matches)
