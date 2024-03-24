def is_anagrams(first, second):
    return sorted(first) == sorted(second)


if __name__ == "__main__":
    text1 = input("Enter the first word: ")
    text2 = input("Enter the second word: ")

    if is_anagrams(text1, text2):
        print("These words are anagrams")
    else:
        print("These words are not anagrams")
