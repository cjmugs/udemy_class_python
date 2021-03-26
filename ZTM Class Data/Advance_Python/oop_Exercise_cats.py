#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
Fluffy = Cat('Fluffy', 10)
Mittens = Cat('Mittens', 6)
Doctor_Xavier_Jones_Burmingham_the_third = Cat('Dr. Xavier Jones Burmingham the third', 102) 


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)
    
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest_cat(Fluffy.age, Mittens.age, Doctor_Xavier_Jones_Burmingham_the_third.age)} years old')
