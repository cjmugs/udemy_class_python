# While Loops
i = 0
my_list = [1,2,3]
while i < len(my_list):
    print(my_list[i])
    i += 1 

i = 0
while i < 50:
    print(i)  
    i = i + 1
else:
    print("Counter is Finished")

while True:
    response = input("Please say Hi!: ")
    if (response == "bye"):
        break

