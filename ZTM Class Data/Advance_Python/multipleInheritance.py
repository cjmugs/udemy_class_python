class User():
    def sign_in(self):
        print('Please sign in . . . ')

        # inherited from the parent class inside the () // Member is the subclass of User
class Human(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
        print(f'Human {self.name} you have attack with {self.power} amount of damage')

    def attack(self):
        print(f'attacking with {self.power}')

class Monster(Human):
    def __init__(self, name, power, sp_abilty):
        Human.__init__(self, name, power)
        self.sp_abilty = sp_abilty
        print(f'Monster {self.name} you have attack with {self.power} amount of damage and sp ability of {self.sp_abilty}')

# Instance of the parent class
person1 = Human('Bill', 50)
monster1 = Monster('Goldbar', 150, "fire")

# Calling the class/ instance of that class and method
person1.sign_in()
person1.attack()
monster1.attack()
print(f'{person1.name} {person1.power}')
print(f'{monster1.name} {monster1.power} {monster1.sp_abilty}')
print(monster1.name)
print(monster1.sp_abilty)