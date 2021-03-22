# *args  **kwargs

# Example of *args
def super_function(*args):
    print(*args)
    return sum(args)
super_function(1,2,3,4,5)
print(super_function(1,2,3,4,5))

# Example of *kwargs
def fun(**kwargs):
    print(kwargs)
print(fun(num1=10, num2=15))