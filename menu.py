menus = [['egg', 'bacon', 'bagel', 'coffee'],['sandwich', 'soup', 'pickle juice'], ['salad', 'spaghetti', 'taco']]

betterMenus = {'Breakfast': ['egg', 'bacon', 'bagel', 'coffee'],
               'Lunch': ['blt', 'pb&j', 'turkey sanwich'],
               'Dinner': ['soup', 'salad', 'spaghetti']}

print(menus[0])
print(betterMenus['Lunch'])

for name, menu in betterMenus.items():
  print(name, ':', menu)