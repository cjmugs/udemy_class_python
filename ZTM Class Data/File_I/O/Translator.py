try:
    with open('C:/Users/cjmug/Desktop/Translator.txt', mode='r') as file:
        read = file.read()
        print(read)
    file.close()

except FileNotFoundError as err:
    print('File does not exist')