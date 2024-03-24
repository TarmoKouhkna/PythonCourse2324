sentence = "Tere tere vana kere Tarmo"


def format_sentence(sentence):
    formatted_sentence = ""

    for index, char in enumerate(sentence):
        if (index + 1) % 3 == 0:
            char = char.upper()

        if (index + 1) % 4 == 3:
            char += "!"

        formatted_sentence += char

    return formatted_sentence


formatted_sentence = format_sentence(sentence)
print(formatted_sentence)
