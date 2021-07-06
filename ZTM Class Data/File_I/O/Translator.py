from translate import Translator

translator= Translator(to_lang="ja")
translator2= Translator(to_lang="it")

try:
    with open('C:/Users/cjmug/Desktop/Translator.txt', mode='r') as file:
        read = file.read()
        translation = translator.translate(read)
        translation2 = translator2.translate(read)
        with open('C:/Users/cjmug/Desktop/Translated.txt', mode='w') as new_file:
            new_file.write(translation2)
            print(translation)
            print(translation2)
    file.close()

except FileNotFoundError as err:
    print('File does not exist')