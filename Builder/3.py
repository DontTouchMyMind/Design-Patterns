tree_list = ['Parents', 'Children', 'GrandChildren']

tree_dict = {}
for key in reversed(tree_list):
    tree_dict = {key: tree_dict}

print(tree_dict)