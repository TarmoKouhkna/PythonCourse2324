# To create a class called "Car" with attributes like "make," "model," and "year,"
# you can follow the example provided in the documents. Here's an example implementation:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car = Car("Toyota", "Camry", 2021)
print(car.make)  # Output: Toyota
print(car.model)  # Output: Camry
print(car.year)  # Output: 2021

# In this example, the `Car` class is defined with an `__init__` method, which is a special method called a
# constructor. The constructor takes in the `make`, `model`, and `year` as parameters and assigns them to the
# corresponding attributes of the class using the `self` keyword.
# To create an instance of the `Car` class, you can simply call the class as if it were a function, passing in
# the required arguments. In this case, we create a `car` object with the make "Toyota," model "Camry," and year 2021.
# You can then access the attributes of the `car` object using dot notation, as shown in the `print` statements.
# This will output the values of the `make`, `model`, and `year` attributes respectively.
# To add a method to the `Car` class that calculates the car's age based on the current year, you can define a
# new method within the class. Here's an example:

import datetime


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def calculate_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.year
        return age


car = Car("Toyota", "Camry", 2021)
print(car.calculate_age())  # Output: 0 (assuming the current year is 2021)


# In this updated example, a new method called `calculate_age` is added to the `Car` class. This method uses
# the `datetime` module to get the current year and calculates the age of the car by subtracting the year attribute
# from the current year. The calculated age is then returned.
# To create a subclass of `Car` called "ElectricCar" with an additional attribute for battery capacity, you can
# define a new class that inherits from the `Car` class. Here's an example:
class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity


electric_car = ElectricCar("Tesla", "Model S", 2022, 75)
print(electric_car.make)  # Output: Tesla
print(electric_car.model)  # Output: Model S
print(electric_car.year)  # Output: 2022
print(electric_car.battery_capacity)  # Output: 75


# In this example, the `ElectricCar` class is defined as a subclass of the `Car` class using the syntax
# `class ElectricCar(Car)`. The `__init__` method of the `ElectricCar` class is overridden to include an additional
# parameter for `battery_capacity`. The `super()` function is used to call the `__init__` method of the parent
# class (`Car`) to initialize the inherited attributes (`make`, `model`, and `year`). The `battery_capacity`
# attribute is then assigned with the provided value.
# You can create an instance of the `ElectricCar` class and access its attributes in the same way as the `Car` class.
# To override the `calculate_age` method in the `ElectricCar` subclass to also calculate the remaining battery life,
# you can define a new version of the method within the subclass. Here's an example:

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def calculate_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.year
        remaining_battery_life = self.battery_capacity - (age * 10)  # Assuming 10% battery degradation per year
        return age, remaining_battery_life


electric_car = ElectricCar("Tesla", "Model S", 2022, 75)
print(electric_car.calculate_age())  # Output: (0, 75) (assuming the current year is 2022)

# In this updated example, the `calculate_age` method is overridden in the `ElectricCar` subclass.
# The method calculates the age of the car as before, but it also calculates the remaining battery
# life based on the assumption that the battery degrades by 10% per year. The remaining battery life is calculated
# by subtracting the product of the age and 10 from the battery capacity.
# When you call the `calculate_age` method on an instance of the `ElectricCar` class, it will return a tuple
# containing the age of the car and the remaining battery life.
