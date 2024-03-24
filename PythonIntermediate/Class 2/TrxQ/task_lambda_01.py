def is_palindrome(palindrome):
    return palindrome == palindrome[::-1]


my_list = ["rotor", "level", "radar", "mama"]

palindrome_words = filter(is_palindrome, my_list)

print("Palindrome words in the list are:")
for word in palindrome_words:
    print(word)
