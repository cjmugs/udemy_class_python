
class PlayerCharacter:
    # Class object attribute
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age =age

# A method to
    def shout(self):
        print(f'Hello my name is {self.name} and my age is {self.age}')

# Another method 
    def attack(self):
        self.hit_points = 50
        print(f'you just lost {self.hit_points} points')
     
# Instances of the class PlayerCharacter
player1 = PlayerCharacter('Max', 2)
player2 = PlayerCharacter('Melanie', 8)
player3 = PlayerCharacter('Chris', 39)
player4 = PlayerCharacter('Kim', 38)

print(player1.shout())
print(player2.shout())
print(player3.shout())
print(player4.shout())

print(player1.attack())
