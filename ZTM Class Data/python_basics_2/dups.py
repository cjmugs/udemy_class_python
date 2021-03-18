# Finding dups in a list
list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# empty list that will get populated with and dups
duplicates = []

# Loop over the list 
for value in list:
    if list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)
