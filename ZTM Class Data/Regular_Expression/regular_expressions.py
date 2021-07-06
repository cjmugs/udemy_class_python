import re
pattern = re.compile(r"([a-zA-Z]).([a])")
string = "Fuck my wife annoys the shit out of me!"
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a)
print(b)
print(c)
print(d)