def count_vowels(text):
    vowels = "aeiouAEIOU"
    amount_of_vowels = 0

    for char in text:
        if char in vowels:
            amount_of_vowels += 1

    return amount_of_vowels

text = "Tere tere vana kere Tarmo"
result = count_vowels(text)
print(f"Number of vowels in the text: {result}")
