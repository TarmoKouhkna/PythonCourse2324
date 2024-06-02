import os
import multiprocessing


def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)


def process_file(filename):
    word_count = count_words(filename)
    print(f"File '{filename}' has {word_count} words.")


if __name__ == "__main__":
    # List of files to process
    files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

    # Create a multiprocessing pool
    pool = multiprocessing.Pool()

    # Map the process_file function to each file in parallel
    pool.map(process_file, files)

    # Close the pool to release resources
    pool.close()
    pool.join()
