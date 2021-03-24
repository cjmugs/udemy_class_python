# assignment expression
 # := --> looks like a walrus

# Example
string = "Hello, worlds!"

if ((n:= len(string)) > 10):
    print(f"too long {len(string)} elements")

# Another example 
# loops through and prints until it cant anymore
while (n := len(string) > 1):
    print(string)
    string = string[:-1]
print(string)