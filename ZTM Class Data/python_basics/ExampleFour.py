 # Exercise List Methods 2
 
 # Using this List
basket = ["Banana","Apples","Oranges","Blueberries"]

basket.pop(0)
basket.pop(2)
class Item_add():
    def __init__(self):
        item_1 = "Apples"
        item_2 = "Kiwi"
        basket.insert(0, item_1)
        basket.insert(5, item_2)
        new_list = basket
        print(new_list)
        
Item_add()
print(basket.count('Apples'))
basket.clear()
print(basket)


       