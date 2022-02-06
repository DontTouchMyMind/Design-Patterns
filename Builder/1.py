# tree_list = ['Parents', 'Children', 'GrandChildren']
#
#
# def build_tree(tree_list):
#     if tree_list:
#         return {tree_list[0]: build_tree(tree_list[1:])}
#     return {}
#
#
# print(build_tree(tree_list))

source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]


def to_tree(source):
    if source:
        parent, child = source[0]

        return
    return {}

# print(to_tree(source))


def to_tree_1(source):
    tree = {}
    current = []
    for parent, child in source:
        if not parent:
            tree[child] = {}
            current = source[1:]
        if current:
            to_tree(current)
    return tree

print(to_tree_1(source))