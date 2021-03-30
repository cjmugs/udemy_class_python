class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
       
    def shout(self):
        print(f'Hello my name is {self.name} and my age is {self.age}')

player1 = PlayerCharacter('Max', 20)

print(player1.shout())
