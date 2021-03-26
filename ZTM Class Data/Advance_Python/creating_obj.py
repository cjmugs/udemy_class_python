# Creating our own oop

class PlayerCharacter:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('Run')
player1 = PlayerCharacter('Max')
player2 = PlayerCharacter('Melanie')

print(player1.name)
print(player2.name)