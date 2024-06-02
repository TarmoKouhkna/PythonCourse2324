import re

text = "Contact us at email@example.com or support@example.org"

# Define the regex pattern for email addresses
pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Find all matches using the findall() function
matches = pattern.findall(text)

# Print the matches
print("Email addresses found in the text:", matches)
