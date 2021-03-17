user_dic = {
    'username' : 'Bill',
    'age' : 36,
    'weapons' : ['Axe'],
    'is_active' : True,
    'is_banned' : False,
    'clan' : "Warrior"
}
user2 = {
    'username' : 'George',
    'age' : 29,
    'weapons' : ['Sword'],
    'is_active' : True,
    'clan' : "Ninja"
}
print(user_dic.keys())

# This adds a new weapon
user_dic['weapons'].append("knives")
print(user_dic)

#  This adds an update to that dictionary
user2.update({'is_banned' : False})
print(user2)

#  This updates the users status
user_dic['is_banned'] = True
print(user_dic)

# This adds a new user by coping the original user and updating with new data 
user3 = user_dic.copy()
user3.update({'age' : 48, 'username' : 'Ben'})
print(user3)



