a = [(1, 1), (2, 1), (3, 1), (4, 3), (5, 3), (6, 3), (7, 7), (8, 7), (9, 7)]
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
# pass 1: create nodes dictionary
nodes = {}
for i in a:
    child, parent = i
    nodes[child] = { 'id': id }

# pass 2: create trees and parent-child relations
forest = {}
tree = {}
for i in source:
    parent, child = i
    node = {parent: {child: {}}}
    # either make the node a new tree or link it to its parent
    if not parent:
        # start a new tree in the forest
        forest.update(node)
    else:
        # add new_node as child to parent
        tree = nodes[parent_id]
        if not 'children' in parent:
            # ensure parent has a 'children' field
            parent['children'] = []
        children = parent['children']
        children.append(node)

print forest