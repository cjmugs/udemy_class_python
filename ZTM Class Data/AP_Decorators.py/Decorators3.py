# (Decorators 3)
def my_decorator(func):
    def wrap_func(x):
        print('***************')
        func(x)
        print('***************')
    return wrap_func

@my_decorator
def hi(greeting):
    print(greeting)

hi('Whats up yo')
