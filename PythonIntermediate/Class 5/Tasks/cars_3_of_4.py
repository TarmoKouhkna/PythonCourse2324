import csv


def read_cars_csv(filename):
    cars = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cars.append(row)
    return cars


def find_lucky_finds(cars):
    lucky_finds = []
    for car in cars:
        mileage = int(car['car_mileage'])
        price = float(
            car['car_price'].replace('$', '').replace(',', ''))  # Remove $ and , from price and convert to float
        if mileage < 150000 and price < 10000:
            lucky_finds.append(car)
    return lucky_finds


def print_lucky_finds(lucky_finds):
    if lucky_finds:
        print("Lucky finds (mileage below 150,000 and price below $10,000):")
        for car in lucky_finds:
            print(
                f"Make: {car['car_make']}, Model: {car['car_model']}, Mileage: {car['car_mileage']}, Price: {car['car_price']}")
    else:
        print("No lucky finds found.")


def main():
    filename = 'cars.csv'
    cars = read_cars_csv(filename)
    lucky_finds = find_lucky_finds(cars)
    print_lucky_finds(lucky_finds)


if __name__ == "__main__":
    main()
