# To create a class called "Rectangle" with attributes for length and width, you can define
# the class with the desired attributes and methods. Here's an example implementation:

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# In this implementation, the `Rectangle` class has an `__init__` method that initializes
# the `length` and `width` attributes.
# The `calculate_area` method calculates and returns the area of the rectangle by multiplying the length and width.
# To create a subclass called "Square" that automatically sets the length and width to be equal, you
# can inherit from the `Rectangle` class and override the `__init__` method. Here's an example implementation:

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def calculate_perimeter(self):
        return 4 * self.length


# In this implementation, the `Square` class inherits from the `Rectangle` class. The `__init__`
# method is overridden to automatically set the length and width to be equal by passing the `side_length` argument
# to the `Rectangle` class's `__init__` method. The `calculate_perimeter` method calculates and returns
# the perimeter of the square by multiplying the side length by 4.
# You can create instances of the `Rectangle` and `Square` classes and call their respective methods to
# calculate the area and perimeter. Here's an example usage:

rectangle = Rectangle(5, 3)
print(rectangle.calculate_area())  # Output: 15

square = Square(4)
print(square.calculate_area())  # Output: 16
print(square.calculate_perimeter())  # Output: 16

# In this example, a `Rectangle` instance is created with a length of 5 and width of 3.
# The `calculate_area` method is called to calculate and print the area of the rectangle.
# Then, a `Square` instance is created with a side length of 4. The `calculate_area` and `calculate_perimeter`
# methods are called to calculate and print the area and perimeter of the square, respectively.
