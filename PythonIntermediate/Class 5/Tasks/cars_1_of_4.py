import csv


def read_cars_csv(filename):
    cars = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            make_model = row['car_make'] + '+' + row['car_model']
            year = int(row['car_year'])  # Convert year to integer
            if make_model not in cars or year > int(cars[make_model]['car_year']):  # Convert year to integer
                cars[make_model] = row
    return cars


def print_latest_cars(cars):
    for make_model, car in cars.items():
        print(f"Latest car for {make_model}:")
        for key, value in car.items():
            print(f"  {key}: {value}")
        print()


def main():
    filename = 'cars.csv'
    cars = read_cars_csv(filename)
    print_latest_cars(cars)


if __name__ == "__main__":
    main()
