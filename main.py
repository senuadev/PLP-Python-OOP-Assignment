# Assignment 1: Design Your Own Class! 

# Base Class
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self._sound = sound  # Protected attribute (encapsulation)

    def make_sound(self):
        return f"{self.name} says {self._sound}"

    def describe(self):
        return f"{self.name} is a {self.species}."

# Dog Subclass
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog", "Woof!")
        self.breed = breed
    def fetch(self):
        return f"{self.name} the {self.breed} is fetching the stick!"

# Cat Subclass
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat", "Meow")
        self.color = color

    def scratch(self):
        return f"{self.name}, the {self.color} cat, is scratching the couch."

# Examples
buddy = Dog("Simba", "Golden Retriever")
whiskers = Cat("Whiskers", "orange")

print(buddy.describe())
print(buddy.make_sound())
print(buddy.fetch())

print(whiskers.describe())
print(whiskers.make_sound())
print(whiskers.scratch())



# Activity 2: Polymorphism Challenge! 🎭

class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

class Truck(Vehicle):
    def move(self):
        return "Trucking 🚚"

# Examples
vehicles = [Car(), Plane(), Boat(), Truck()]
for v in vehicles:
    print(v.move())
