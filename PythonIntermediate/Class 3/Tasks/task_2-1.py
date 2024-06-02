import re

text = "Say hello to the world"
pattern = r'\bhello\b'
matches = re.findall(pattern, text)
print(matches)
