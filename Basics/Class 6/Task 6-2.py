"""
Create a class called "Rectangle" with attributes for length and width.
Add a method to the Rectangle class that calculates and returns the area.
Create a subclass of Rectangle called "Square" that automatically sets the length and width to be equal.
Add a method to the Square class that calculates and returns the perimeter.
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Now subclass square
class Square(Rectangle):
    def __init__(self, side, length, width):
        super().__init__(length, width)
        self.length = side
        self.width = side

    def perimeter(self):
        return 4 * self.length


