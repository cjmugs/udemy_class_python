from functools import reduce

my_list = [1,2,3]
your_list = [4,5,6]
their_list = [7,8,9]

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator,my_list, 0))
