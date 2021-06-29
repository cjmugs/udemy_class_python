from random import randint
import sys

# This generates random intergers 
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    try:
        guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
        if 0 < guess < 11:
            if guess == answer:
                print('You got it right')
                break
            else:
                print('That is wrong!')

    except ValueError:
        print('Please enter a number')
        continue