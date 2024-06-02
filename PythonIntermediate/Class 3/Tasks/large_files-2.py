import os


def read_large_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                yield line.rstrip('\n')
    else:
        print(f"\n{file_path.title()} not found. Using 'mockaroo.csv' instead.\n")
        with open('mockaroo.csv', 'r') as file:
            for line in file:
                yield line.rstrip('\n')


# Example usage:
file_path = 'large_file.txt'
for line in read_large_file(file_path):
    print(line)

"""This code first checks if 'large_file.txt' exists using os.path.exists(). If it does, it reads 
from 'large_file.txt' as before. Otherwise, it prints a message indicating that 'large_file.txt' was not found and 
reads from 'mockaroo.csv'."""