import csv


def read_cars_csv(filename):
    cars = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cars.append(row)
    return cars


def find_wife_favorite_cars(cars):
    wife_favorite_cars = []
    for car in cars:
        if car['car_color'].lower() == 'red' and int(car['car_accidents']) == 0 and int(car['car_year']) >= 2018:
            wife_favorite_cars.append(car)
    return wife_favorite_cars


def print_wife_favorite_cars(wife_favorite_cars):
    if wife_favorite_cars:
        print("Cars that your wife might like:")
        for car in wife_favorite_cars:
            print(
                f"Make: {car['car_make']}, Model: {car['car_model']}, Year: {car['car_year']}, Color: {car['car_color']}, Accidents: {car['car_accidents']}")
    else:
        print("Sorry, no cars matching your wife's preferences were found.")


def main():
    filename = 'cars.csv'
    cars = read_cars_csv(filename)
    wife_favorite_cars = find_wife_favorite_cars(cars)
    print_wife_favorite_cars(wife_favorite_cars)


if __name__ == "__main__":
    main()
