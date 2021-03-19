# a basic function with parameter inside the brackets
# parameters define the function
def say_hello(name, emoji):
    print(f'whats up {name} {emoji} !')

# arguements = what is inside of the brackets
# arguements call the function
say_hello('Chris', ':)')

# keyword arguements
# giving the arguements keywords and values
say_hello(emoji=':)', name='Thomas')
