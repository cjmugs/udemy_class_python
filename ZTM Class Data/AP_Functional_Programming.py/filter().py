my_list = [1,2,3,4,5,6,7,8,9]

# Filter Function
def multiply_by_2(item):
    return item*2

def check_odd(item):
    # This returns a a boolean value using
    # item divide by modulo 2 not equal to 0
   return item % 2 != 0 

# Map function creates/ returns a new list
print(list(map(multiply_by_2, [12,14,16])))

print(my_list)

# Filter function
print(list(filter(check_odd, my_list)))