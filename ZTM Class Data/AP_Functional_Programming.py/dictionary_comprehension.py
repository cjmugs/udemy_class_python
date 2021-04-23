# Set Dictionary

simple_dict = {
    'a': 1,
    'b': 2
}
# can add for loops and if statements
my_dict = {key: value**2 for key, value in simple_dict.items() 
# This produces only even using  --> %2==0
if value%2 == 0}
print(my_dict)


# Another Example
           # key:value then the for loop
my_dict2 = {num:num*2 for num in [1,2,3]
if num%2 == 0}
print(my_dict2)