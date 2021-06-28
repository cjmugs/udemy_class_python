# To create a generator
def gen_func(num):
    for i in range(num):
        yield i
for item in gen_func(100):
    print(item)
    