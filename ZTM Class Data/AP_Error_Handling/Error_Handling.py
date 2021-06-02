# Error Handling using a try and except block

    # To make it run continiously put in a while loop
while True:
    try:
        age = int(input("What is your age? "))
        print(age)

    except:
        print("Not a value, please enter a number")