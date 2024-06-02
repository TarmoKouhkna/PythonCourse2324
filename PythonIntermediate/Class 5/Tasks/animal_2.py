class Animal:
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return "Roar"


class Bird(Animal):
    def make_sound(self):
        pass


class Sparrow(Bird):
    def make_sound(self):
        return "Chirp"


# Example usage
animals = [Lion(), Sparrow()]

for animal in animals:
    print(animal.__class__.__name__, "sound:", animal.make_sound())
