"""
Create a class called "Car" with attributes like "make," "model," and "year."
Create an instance of the Car class and print its attributes.
Add a method to the Car class that calculates the car's age based on the current year.
Create a subclass of Car called "ElectricCar" with an additional attribute for battery capacity.
Override the Car class's method in the ElectricCar subclass to also calculate the remaining battery life.
"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_age(self, current_year):
        return current_year - self.year


# create an instance of the class
my_car = Car('Ford', 'Focus', 2015)

# Displaying instance attributes
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")

# Calculating the age of the car
print(f"My car's age is: {my_car.car_age(2023)}")


# Creating an electric car subclass
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity


# Overriding the method
def car_age(current_year):
    age = super().car_age(current_year)
    battery_life = 80 - age
    return f"Age is {age} years, battery life is {battery_life} years remaining"


# Electric car copy
e_car = ElectricCar('Tesla', 'Model 3', 2020, 70)

print(f"Make: {e_car.make}")
print(f"Model: {e_car.model}")
print(f"Year: {e_car.year}")
print(f"Battery capacity: {e_car.battery_capacity}")
print(e_car.car_age(2023))
