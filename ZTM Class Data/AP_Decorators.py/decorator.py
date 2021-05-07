# Decorators have the @ -->followed by a name

def hello(func):
    func()

def greet():
    print("Whats up!")

a = hello(greet)

print(a)


# The Power of Decorators
def my_decorator(func):
    def wrap_func():
        print('***************')
        func()
        print('***************')
    return wrap_func()

@my_decorator
def hello_hi():
    print('Hellollloooo')

@my_decorator
def bye():
    print('See ya later')

hello_hi()
bye()
