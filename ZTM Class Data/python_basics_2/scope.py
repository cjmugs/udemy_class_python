# Scope -- what variables do I have access to?
    # Who has access to who

# Example of Scope
a = 1
def confussion():
    a = 5
    return a
print(a)
print(confussion())



# Scope Rules
    # 1 Starts with local scope rule
    # 2 parent a local scope
    # 3 Global scope --> no indentation   
    # 4 built in python Functions