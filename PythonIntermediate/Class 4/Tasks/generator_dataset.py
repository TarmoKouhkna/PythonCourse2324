def record_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Assuming each record is on a new line


# Example usage:
file_path = "data.txt"
num_records = 10
data_generator = record_generator(file_path)

for i in range(num_records):
    record = next(data_generator)
    print(record)
