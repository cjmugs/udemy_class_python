def multiply_by_2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list



def divide_by_2(li):
    new_list2 = []
    for item in li:
        new_list2.append(item/2)
    return new_list2

print(multiply_by_2([1,2,3]))
print(divide_by_2([20,18,16]))