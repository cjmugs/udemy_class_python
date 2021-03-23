# Just an Example
def driver_id():
    name = input('Please enter name: ')
    age = int(input('Please enter your age: '))
    
    if int(age) < 18:
        print(f"Sorry, {name} you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print(f"Powering On. Enjoy the ride {name}!");
    elif int(age) == 18:
        print(f"Congratulations {name} on your first year of driving. Enjoy the ride!")
driver_id()

