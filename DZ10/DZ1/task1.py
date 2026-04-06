class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def make_sound(self):
        return "Some sound"


class Mammal(Animal):
    def make_sound(self):
        return "Roar"

    def give_birth(self):
        return f"{self.name} gives birth"


class Bird(Animal):
    def make_sound(self):
        return "Squawk"

    def lay_eggs(self):
        return f"{self.name} lays eggs"


class Reptile(Animal):
    def make_sound(self):
        return "Hiss"

    def shed_skin(self):
        return f"{self.name} sheds skin"


animals = [
    Mammal("Lion", "Mammal", 4),
    Bird("Falcon", "Bird", 2),
    Reptile("Python", "Reptile", 4),
]

for animal in animals:
    print(
        f"Animal: {animal.name}, Species: {animal.species}, Legs: {animal.legs}, Sound: {animal.make_sound()}"
    )
