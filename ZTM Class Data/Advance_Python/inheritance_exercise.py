class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

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
        sounds = "Meow Meow Meow"
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Mike(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_pets1 = Cat('Mike', 50)
my_pets2 = Cat('Sally', 40)
my_pets3 = Cat('Simon', 30)

print(my_pets1.walk())
print(my_pets2.walk())
print(my_pets3.walk())


#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []

#3 Instantiate the Pet class with all your cats use variable my_pets

#4 Output all of the cats walking using the my_pets instance