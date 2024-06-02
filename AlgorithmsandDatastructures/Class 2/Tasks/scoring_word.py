def highest_scoring_word(sentence):
    # Function to calculate the score of a word
    def word_score(word):
        return sum(ord(char) - ord('a') + 1 for char in word.lower())

    # Split the sentence into words
    words = sentence.split()

    # Initialize variables to store the highest scoring word and its score
    highest_word = ''
    highest_score = 0

    # Iterate through each word in the sentence
    for word in words:
        score = word_score(word)
        # Update the highest scoring word if the current word has a higher score
        if score > highest_score:
            highest_word = word
            highest_score = score

    return highest_word


# Example usage:
sentence = ("Cupcake ipsum dolor sit amet cake. Gummies cotton candy carrot cake soufflé pie bear claw chocolate ice "
            "cream. Dessert shortbread wafer tiramisu chupa chups. I love candy canes bonbon carrot cake caramels "
            "jelly beans. Cake chocolate cake shortbread cupcake carrot cake candy canes I love. Sweet cake "
            "cheesecake I love cupcake. Carrot cake muffin tart shortbread bonbon tart topping chocolate carrot cake.")
print(highest_scoring_word(sentence))
