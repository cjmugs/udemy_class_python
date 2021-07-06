# password has to have 8 chars
# contains any letters, numbers and $%#@
import re
try:
    pattern = re.compile(r"[a-zA-Z0-9$%@#]{7,}[0-9]")
    password = 'T@cos1234'
    a = pattern.search(password)
    check = pattern.fullmatch(password)
    print(check)

except:
    pass