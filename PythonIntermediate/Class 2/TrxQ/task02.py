import csv
import json


# Define a function to convert CSV to JSON
def csv_to_json(csv_file, json_file):
    # Initialize an empty list to store CSV data
    data = []

    # Open the CSV file in read mode
    with open(csv_file, 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append each row to the data list
            data.append(row)

    # Open the JSON file for writing
    with open(json_file, 'w') as file:
        # Write the data to the JSON file in a pretty-printed format
        json.dump(data, file, indent=4)


# Call the function to convert 'trxq_albums.csv' to 'trxq_albums.json'
csv_to_json('trxq_albums.csv', 'trxq_albums.json')
