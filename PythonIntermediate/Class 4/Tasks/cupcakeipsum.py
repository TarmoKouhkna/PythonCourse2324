# Read text from file and split paragraphs into separate list elements
with open('cupcakeipsum.txt', 'r') as file:
    paragraphs = file.read().split('\n\n')

# Define function to perform required operations on each paragraph
def process_paragraph(paragraph):
    # Lowercase every letter
    paragraph = paragraph.lower()

    # Split paragraph into sentences
    sentences = paragraph.split('. ')

    # Remove sentences starting with 'c' or 'C'
    sentences = [sentence for sentence in sentences if not sentence.startswith('c')]

    # Reverse sentences containing the word 'roll'
    sentences = [sentence[::-1] if 'roll' in sentence else sentence for sentence in sentences]

    # Convert entire sentence to uppercase if it contains the word 'bears'
    sentences = [sentence.upper() if 'bears' in sentence else sentence for sentence in sentences]

    # Join sentences back into paragraph
    processed_paragraph = '. '.join(sentences)

    return processed_paragraph

# Process each paragraph concurrently
processed_paragraphs = [process_paragraph(paragraph) for paragraph in paragraphs]

# Write the final result to a new file with paragraphs separated by an extra empty line
with open('processed_cupcakeipsum.txt', 'w') as file:
    file.write('\n\n\n'.join(processed_paragraphs))
