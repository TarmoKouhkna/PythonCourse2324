import csv
import json


def json_to_csv(json_data, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        writer.writerow(["right_side", "left_side"])

        # Determine the maximum length of the lists
        max_length = max(len(json_data["right_side"]), len(json_data["left_side"]))

        # Fill in missing values with None
        right_side = json_data.get("right_side", [])
        left_side = json_data.get("left_side", [])

        right_side += [None] * (max_length - len(right_side))
        left_side += [None] * (max_length - len(left_side))

        # Write data
        for i in range(max_length):
            writer.writerow([right_side[i], left_side[i]])


json_data = {
    "right_side": [3, 5, 3, 6, 4, 2, 3, 6, 8, 4, 3, 2],
    "left_side": [1.2, 4.3, 5.4, 6.9, 9.9, 7.2]
}

csv_filename = "numbrid_tabelisse.csv"
json_to_csv(json_data, csv_filename)
print("CSV file created successfully:", csv_filename)
