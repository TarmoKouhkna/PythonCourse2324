import csv
from datetime import datetime


def read_cars_csv(filename):
    cars = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cars.append(row)
    return cars


def filter_cars(cars):
    filtered_cars = []
    for car in cars:
        purchase_date = datetime.strptime(car['car_purchase_date'], '%m/%d/%Y')  # Adjust format
        if purchase_date >= datetime(2015, 1, 1) and int(car['car_accidents']) == 0:
            filtered_cars.append(car)
    return filtered_cars


def print_filtered_cars(filtered_cars):
    if filtered_cars:
        print("Cars purchased since 2015/01/01 and had no car accidents:")
        for car in filtered_cars:
            print(f"Make: {car['car_make']}, Model: {car['car_model']}, Purchase Date: {car['car_purchase_date']}")
    else:
        print("No cars match the criteria.")


def main():
    filename = 'cars.csv'
    cars = read_cars_csv(filename)
    filtered_cars = filter_cars(cars)
    print_filtered_cars(filtered_cars)


if __name__ == "__main__":
    main()
