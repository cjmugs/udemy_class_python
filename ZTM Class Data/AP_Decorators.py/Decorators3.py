# (Decorators 3)
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('***************')
        func(*args, **kwargs)
        print('***************')
    return wrap_func

@my_decorator
def hi(greeting, emoji = ':) :) :)'):
    print(greeting, emoji)

hi('Whats up Ben, you are crazy')
