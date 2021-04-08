# polymorphism = many forms
# Parent Class
class User():
    def sign_in(self):
        print('Logged in')
        
# inherited from the parent class inside the () // Member is the subclass of User
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'{self.name} is attacking with {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'{self.name} is attacking with arrows left- {self.num_arrows}')


# Instance of the parent class
wizard1 = Wizard('Bill', 50)
archer1 = Archer('Mike', 100)

# Calls the class and method
archer1.attack()
wizard1.attack()

