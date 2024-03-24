import requests
import csv


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from", url)
        return None


def fetch_names(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('name') or data.get('title')
    else:
        print("Failed to fetch name from", url)
        return None


def write_to_csv(people, filename):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for person in people:
            homeworld_name = fetch_names(person['homeworld'])
            species_name = fetch_names(person['species'][0]) if person['species'] else None
            films_names = [fetch_names(film) for film in person['films']]
            writer.writerow(
                [person['name'], person['height'], person['mass'], person['hair_color'], person['skin_color'],
                 person['eye_color'], person['birth_year'], person['gender'], homeworld_name, species_name,
                 films_names])


def main():
    base_url = 'https://swapi.dev/api/people/'
    filename = 'star_wars_people.csv'

    # Write header row to CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['Name', 'Height', 'Mass', 'Hair Color', 'Skin Color', 'Eye Color', 'Birth Year', 'Gender', 'Homeworld',
             'Species', 'Films'])

    next_url = base_url

    while next_url:
        data = fetch_data(next_url)
        if data:
            write_to_csv(data['results'], filename)
            next_url = data['next']
        else:
            break

    print("Data has been written to", filename)


if __name__ == "__main__":
    main()
