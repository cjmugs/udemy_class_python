
# open = opens files
# mode w = writes to a file / creates a new one
with open ('C:/Users/Owner/Desktop/Test.py', mode='w') as my_file:
    text = my_file.write(' This is where someone like you would write something!')

# mode a = appends to the end of the file
with open ('C:/Users/Owner/Desktop/Test.py', mode='a') as my_file:
    text = my_file.write('\n We are adding a lot of data to this file')
my_file.close()