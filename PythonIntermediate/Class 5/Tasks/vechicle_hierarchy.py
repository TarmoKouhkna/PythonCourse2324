class Vehicle:
    def __init__(self, speed, num_wheels):
        self.speed = speed
        self.num_wheels = num_wheels

    def move(self):
        print("Vehicle is moving")

    def calculate_speed(self):
        return self.speed


class Car(Vehicle):
    def __init__(self, speed, num_wheels, brand, fuel_type):
        super().__init__(speed, num_wheels)
        self.brand = brand
        self.fuel_type = fuel_type

    def move(self):
        print("Car is driving")

    def calculate_fuel_consumption(self):
        if self.fuel_type == "gasoline":
            return 10 * self.speed
        elif self.fuel_type == "diesel":
            return 8 * self.speed
        else:
            return None


class Bicycle(Vehicle):
    def __init__(self, speed):
        super().__init__(speed, num_wheels=2)

    def move(self):
        print("Bicycle is pedaling")

    def calculate_calories_burned(self):
        return 5 * self.speed


class Truck(Vehicle):
    def __init__(self, speed, num_wheels, cargo_capacity):
        super().__init__(speed, num_wheels)
        self.cargo_capacity = cargo_capacity

    def move(self):
        print("Truck is driving")

    def calculate_fuel_consumption(self):
        # Assuming a base fuel consumption of 5 units per speed, and 0.1 units per cargo_capacity
        return 5 * self.speed + 0.01 * self.cargo_capacity


# Example usage
car = Car(60, 4, "Toyota", "gasoline")
bicycle = Bicycle(20)
truck = Truck(50, 6, 1000)

print(car.calculate_speed())
print(car.calculate_fuel_consumption())

print(bicycle.calculate_speed())
print(bicycle.calculate_calories_burned())

print(truck.calculate_speed())
print(truck.calculate_fuel_consumption())
