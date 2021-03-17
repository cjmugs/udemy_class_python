# Username and Password 

import getpass

username = input('What is your username? ')
password = getpass.getpass("Please enter your password: ")


password_length = len(password)
hidden_password = '*' * password_length

print(f'{username}, your password {hidden_password} is {len(password)} letters long')