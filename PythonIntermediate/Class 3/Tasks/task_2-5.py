import re

text = "Visit us at http://example.com or https://www.example.org"

# Compile the regex pattern for matching URLs
pattern = re.compile(r'https?://(?:www\.)?\w+\.\w+')

# Find all matches using the findall() function
matches = pattern.findall(text)

# Print the matches
print("URLs found in the text:", matches)
