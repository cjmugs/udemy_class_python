# inheritance example

class User():
    def sign_in(self):
        # Global variable
        power = self.power
        
        if (power > 10):
            print('Logged in')
        else:
            print('Sorry not powerful enough to enter')
        
        # inherited from the parent class inside the () // Member is the subclass of User
class Member(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with {self.power}')

#Instance of the parent class
user1 = Member('Bill', 50)

# Calling the class/ instance of that class and method
user1.sign_in()
user1.attack()

