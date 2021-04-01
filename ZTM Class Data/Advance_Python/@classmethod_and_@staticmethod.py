class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    def shout(self):
        print(f'Hello my name is {self.name} and my age is {self.age}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Max', 20)

print(player1.adding_things(2, 7))
