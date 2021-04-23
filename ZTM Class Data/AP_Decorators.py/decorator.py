# Decorators have the @ -->followed by a name

def hello(func):
    func()

def greet():
    print("Whats up!")

a = hello(greet)

print(a)