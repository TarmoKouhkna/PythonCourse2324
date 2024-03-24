# Write a program that will determine the number of vowels in a given string.
# vowels = ['a', 'e', 'i', 'o', 'u']

vowels = "aeiouAEIOU"

text = "Tere tere vana kere Tarmo"
amount_of_vowels = 0

for char in text:
    if char in vowels:
        amount_of_vowels += 1

print(f"Number of vowels in the text: {amount_of_vowels}")
