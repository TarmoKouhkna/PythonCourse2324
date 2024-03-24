# Create a function that checks if two given strings are anagrams of each other.
# Allow the user to input two strings and use the function to determine if they are anagrams.

"""
To check for anagrams, we use the collections library and Counter.
Counter counts the number of each character in a string and returns it as a dictionary.
Then we just need to compare the counters of two words - if they are equal, it means the words are anagrams.
We input two words from the user and output the result of the check.
This approach allows us to quickly solve the task of checking for anagrams
without sorting characters in strings.
"""


# import collections
#
# def are_anagrams(word1, word2):
#   return collections.Counter(word1) == collections.Counter(word2)
#
# word1 = input("Input first word: ")
# word2 = input("Input second word: ")
#
# if are_anagrams(word1, word2):
#   print(f"{word1} and {word2} are anagrams")
# else:
#   print(f"{word1} and {word2} are anagrams")


# In this program:
#
# Converting words into lists of letters
# Let's sort these lists
# Comparing sorted lists
# If they are equal, the words are anagrams.
#
# This approach requires more calculations, but allows you to solve the problem
# without importing external libraries.

# "coronavirus" = "carnivorous"
def are_anagrams(word1, word2):
    word1_letters = list(word1)
    word2_letters = list(word2)

    word1_letters.sort()
    word2_letters.sort()

    if word1_letters == word2_letters:
        return True
    else:
        return False


word1 = input("Input the word: ")
word2 = input("Input the word: ")

if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams")
else:
    print(f"{word1} and {word2} are not anagrams")
