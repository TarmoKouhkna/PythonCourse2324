# Write a program that will display the given sentence every third character will be capitalized
# and every fourth character will have an exclamation mark after it.

sentence = "Tere tere vana kere Tarmo"

formatted_sentence = ""

for index in range(len(sentence)):
    char = sentence[index]

    if (index + 1) % 3 == 0:
        char = char.upper()

    if (index + 1) % 4 == 3:
        char += "!"

    formatted_sentence += char

print(formatted_sentence)
