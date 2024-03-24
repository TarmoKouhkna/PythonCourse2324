"""
Write a function that takes a sentence as input and
returns the count of each word in the sentence.
Use a dictionary to store the word counts.
Allow the user to input a sentence and display the word count results.
"""

# In this function we:
# Create an empty dictionary to store the word count
# Divide the sentence into a list of words by spaces
# Loop through each word
# Checking if this word is already in the dictionary
# If there is, we increase the counter, if not, we add with counter 1
# Returning a dictionary with counting
# We then ask the user for a suggestion and display the result

import json


def count_words(sentence):
    word_counts = {}
    words = sentence.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


user_sentence = input("Please input sentence: ")
word_counts = count_words(user_sentence)

print(json.dumps(word_counts, indent=2))
