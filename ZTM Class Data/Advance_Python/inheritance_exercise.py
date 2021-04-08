class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

    def sing(self):
        sounds = "Meow Meow Meow"
        print(sounds)

class Cat(Pets):
    is_lazy = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

# Subclasses of Cat
class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Mike(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# This is how to create the list
my_cats = [Simon('Simon' , 4), Sally('Sally', 6), Mike('Mike', 25)]

# This instantiates the Pet class with all of the cats using variable my_pets
my_pets = Pets(my_cats)


# This calls the instance and method
my_pets.walk()
my_pets.sing()
