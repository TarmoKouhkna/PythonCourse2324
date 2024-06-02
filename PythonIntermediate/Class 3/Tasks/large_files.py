def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()


# Example usage
file_path = 'mockaroo.csv'
for line in read_large_file(file_path):
    print(line)
