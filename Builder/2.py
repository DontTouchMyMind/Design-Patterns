from functools import reduce

tree_list = ['Parents', 'Children', 'GrandChildren']

lambda d1: reduce(lambda x, y: {y: x}, tree_list[::-1], {})

print(d1)