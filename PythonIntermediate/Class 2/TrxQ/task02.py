import csv
import json


def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)

    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)


csv_to_json('trxq_albums.csv', 'trxq_albums.json')
