class Pets():
    animal = []
    def __init__(self, animals):
        self.animal = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())