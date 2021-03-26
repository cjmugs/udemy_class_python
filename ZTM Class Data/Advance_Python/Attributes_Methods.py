
class PlayerCharacter:
    # Class object attribute
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age =age

    def run(self):
        print('Run')
        return 'done'

player1 = PlayerCharacter('Max', 2)
player2 = PlayerCharacter('Melanie', 8)
player3 = PlayerCharacter('Chris', 39)
player4 = PlayerCharacter('Kim', 38)

print(player1.run())

print(player1.name, player1.age)
print(player2.name, player2.age)
print(player3.name, player3.age)
print(player4.name, player4.age)
print(player1.membership, player2.membership, player3.membership, player4.membership) 