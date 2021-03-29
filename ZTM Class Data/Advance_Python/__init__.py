class PlayerCharacter:
    # Class object attribute
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age =age
        if (age < 18):
            print("Restricted") 
 
# A method to
    def shout(self):
        print(f'Hello my name is {self.name} and my age is {self.age}')

# Another method 
   # def attack(self):
       # self.hit_points = 50
      #  print(f'you just lost {self.hit_points} points')
     
# Instances of the class PlayerCharacter
player1 = PlayerCharacter('Max', 20)


