try:
    with open('C:/Users/cjmug/Desktop/Translator.txt', mode='r') as new_file:
        read = new_file.read()
    new_file.close()

except FileNotFoundError as err:
    print('File does not exist')