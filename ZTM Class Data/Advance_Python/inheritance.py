# inheritance example

class User():
    def sign_in(self):
        print('Logged in')
        
        # inherited from the parent class inside the ()
class Member(User):
    pass

user1 = Member()
print(user1.sign_in())