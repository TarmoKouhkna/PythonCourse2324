MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I',
              '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
              '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
              '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W',
              '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
              '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
              '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
              '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def morse_to_text(morse_code):
    words = morse_code.strip().split('   ')  # Split the input into words after removing leading/trailing spaces
    decoded_text = []
    for word in words:
        letters = word.split(' ')  # Split each word into letters
        decoded_word = ''
        for letter in letters:
            decoded_word += MORSE_CODE[letter]  # Translate each letter and append to the word
        decoded_text.append(decoded_word)  # Append the decoded word to the result
    return ' '.join(decoded_text)  # Join the decoded words with spaces to form the final text


# Test cases
morse_code1 = '.... . -.--   .--- ..- -.. .'
morse_code2 = '...   ---   ...'
morse_code3 = ' . '

print(morse_to_text(morse_code1))  # Output: "HEY JUDE"
print(morse_to_text(morse_code2))  # Output: "SOS"
print(morse_to_text(morse_code3))  # Output: "E"
