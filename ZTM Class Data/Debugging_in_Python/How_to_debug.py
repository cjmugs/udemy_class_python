# Linting  = Catches errors before code is ran

#pdb = python debugger => built in module


import pdb

def sup(num1, num2):
    pdb.set_trace()
    return num1 + num2

sup(4, 'adfa')
