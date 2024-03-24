import requests
import csv


# Function to fetch data from SWAPI
def fetch_swapi_data(url):
    response = requests.get(url)
    data = response.json()
    return data


# Function to write data to CSV file
def write_to_csv(data, filename):
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header only if file is empty
        csvfile.seek(0, 2)
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write data
        for item in data:
            writer.writerow(item)


# Main function to fetch all people from SWAPI and write to CSV
def fetch_all_people():
    base_url = "https://swapi.dev/api/people"
    next_url = base_url

    while next_url:
        data = fetch_swapi_data(next_url)
        people = data.get('results', [])
        write_to_csv(people, 'swapi_people.csv')
        next_url = data.get('next')


fetch_all_people()
