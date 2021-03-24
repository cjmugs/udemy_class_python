# Just an Example

def user_id():
    name = input('Please enter name: ')
    age = int(input('Please enter your age: '))
    if int(age) < 18:
        print(f"Sorry, {name} you are too young to operate this program. Powering off")
    elif int(age) > 18:
        print(f"Powering On. Enjoy the ride {name}!");
    elif int(age) == 18:
        print(f"Congratulations {name} on your first year of using the prgram. Enjoy the ride!")
print('Program starting . . .')


