from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return "Roar"


class Bird(Animal, ABC):
    pass


class Sparrow(Bird):
    def make_sound(self):
        return "Chirp"


# Example usage
lion = Lion()
print("Lion sound:", lion.make_sound())

sparrow = Sparrow()
print("Sparrow sound:", sparrow.make_sound())
