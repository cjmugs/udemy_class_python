# password has to have 8 chars
# contains any letters, numbers and $%#@
import re
try:
    pattern = re.compile(r"(^[a-zA-Z0-9_$%#@a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    string = 'T@cos1234#.com'
    a = pattern.search(string)
    print(a)

except:
    pass