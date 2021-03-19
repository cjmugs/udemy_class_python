# Return
def sum(num1, num2):
    return num1 + num2
print(sum(4,5))
print(sum(10,5))


# a function should do one thing really well
# a function should RETURN something

def adding(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func(num1, num2)

total = adding(10, 20)
print(total)

# Return automatically exits the function