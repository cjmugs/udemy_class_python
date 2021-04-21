# List Comprehensions

# This does the same as the code below  - - Treat it like a for loop 
my_list = [char for char in "Jello"]

for char in "Jello":
    my_list.append(char)

# Another Example
my_list2 = [num for num in range(0,300)]

# Another Example multiple range * 2
my_list3 = [num*2 for num in range(0,300)]


# Another Example with an if condition
my_list4 = [num**2 for num in range(0,300) if num % 2 ==0]



print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)