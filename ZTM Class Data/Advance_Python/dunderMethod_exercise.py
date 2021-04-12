#By reading the python documentation, add 3 more magic/dunder methods of your choice to this Toy class. 
class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
        'name':'Tony',
        'has_pets': False,
    }

# Dunder Methods
  def __str__(self):
    return f"{self.color}"

  def __len__(self):
    return 505

  def __del__(self):
    return "deleted"

  def __call__(self):
      return('This is Call a function')

  def __getitem__(self,i):
      return self.my_dict[i]

# Instance of Toy
action_figure = Toy('red', 0)

# These 2 are the same way of calling the same thing
print(action_figure.__str__())
print(str(action_figure))

print(len(action_figure))
print(action_figure())
print(action_figure['name'])