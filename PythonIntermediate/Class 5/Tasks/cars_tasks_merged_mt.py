import csv
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor


def read_cars_csv(filename):
    cars = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cars.append(row)
    return cars


def find_latest_cars(cars):
    latest_cars = {}
    for car in cars:
        make_model = car['car_make'] + '+' + car['car_model']
        year = int(car['car_year'])
        if make_model not in latest_cars or year > int(latest_cars[make_model]['car_year']):
            latest_cars[make_model] = car
    return latest_cars


def filter_cars_purchased_since_2015(cars):
    filtered_cars = []
    for car in cars:
        purchase_date = datetime.strptime(car['car_purchase_date'], '%m/%d/%Y')  # Adjust format
        if purchase_date >= datetime(2015, 1, 1) and int(car['car_accidents']) == 0:
            filtered_cars.append(car)
    return filtered_cars


def find_lucky_finds(cars):
    lucky_finds = []
    for car in cars:
        mileage = int(car['car_mileage'])
        price = float(
            car['car_price'].replace('$', '').replace(',', ''))  # Remove $ and , from price and convert to float
        if mileage < 150000 and price < 10000:
            lucky_finds.append(car)
    return lucky_finds


def find_wife_favorite_cars(cars):
    wife_favorite_cars = []
    for car in cars:
        if car['car_color'].lower() == 'red' and int(car['car_accidents']) == 0 and int(car['car_year']) >= 2018:
            wife_favorite_cars.append(car)
    return wife_favorite_cars


def print_latest_cars(latest_cars):
    print("Latest cars for each make+model:")
    for car in latest_cars.values():
        print(f"Make: {car['car_make']}, Model: {car['car_model']}, Year: {car['car_year']}")


def print_filtered_cars(filtered_cars):
    if filtered_cars:
        print("\nCars purchased since 2015/01/01 and had no car accidents:")
        for car in filtered_cars:
            print(f"Make: {car['car_make']}, Model: {car['car_model']}, Purchase Date: {car['car_purchase_date']}")


def print_lucky_finds(lucky_finds):
    if lucky_finds:
        print("\nLucky finds (mileage below 150,000 and price below $10,000):")
        for car in lucky_finds:
            print(
                f"Make: {car['car_make']}, Model: {car['car_model']}, Mileage: {car['car_mileage']}, Price: {car['car_price']}")


def print_wife_favorite_cars(wife_favorite_cars):
    if wife_favorite_cars:
        print("\nCars that your wife might like:")
        for car in wife_favorite_cars:
            print(
                f"Make: {car['car_make']}, Model: {car['car_model']}, Year: {car['car_year']}, Color: {car['car_color']}, Accidents: {car['car_accidents']}")
    else:
        print("\nSorry, no cars matching your wife's preferences were found.")


def main():
    filename = 'cars.csv'
    cars = read_cars_csv(filename)

    with ProcessPoolExecutor() as executor:
        latest_cars_future = executor.submit(find_latest_cars, cars)
        filtered_cars_future = executor.submit(filter_cars_purchased_since_2015, cars)
        lucky_finds_future = executor.submit(find_lucky_finds, cars)
        wife_favorite_cars_future = executor.submit(find_wife_favorite_cars, cars)

        latest_cars = latest_cars_future.result()
        filtered_cars = filtered_cars_future.result()
        lucky_finds = lucky_finds_future.result()
        wife_favorite_cars = wife_favorite_cars_future.result()

    print_latest_cars(latest_cars)
    print_filtered_cars(filtered_cars)
    print_lucky_finds(lucky_finds)
    print_wife_favorite_cars(wife_favorite_cars)


if __name__ == "__main__":
    main()
