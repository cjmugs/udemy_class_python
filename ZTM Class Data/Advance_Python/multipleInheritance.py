class User():
    def sign_in(self):
        print('Please sign in . . . ')

        
        # inherited from the parent class inside the () // Member is the subclass of User
class Human(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with {self.power}')

class Monster(Human):
    def __init__(self, name, power, sp_abilty):
        self.sp_abilty = sp_abilty
        Human.__init__(self, name, power)
       

# Instance of the parent class
person1 = Human('Bill', 50)
monster1 = Monster('Goldbar', 150, "fire")

# Calling the class/ instance of that class and method
person1.sign_in()
person1.attack()
monster1.attack()
print(person1.name)