# inheritance example

class User():
    def sign_in(self):
        print('Logged in')
        
        # inherited from the parent class inside the ()
class Member(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with {self.power}')

user1 = Member('Bill', 50)
print(user1.sign_in())
print(user1.attack())
