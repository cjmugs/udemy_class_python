my_list = [1,2,3]
print(my_list)
# lambda is a ONE time function
print(list(map(lambda item: item*2, my_list)))


# Another example

list_2 = ["Hello", "Good", "Bye"]
print(list(map(lambda item: item, list_2)))
