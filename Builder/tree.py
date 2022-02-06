# Написать функцию, строящую дерево по списку пар id (id родителя, id потомка),
# где None - id корневого узла.
# Пример работы:

class Node:
    def __init__(self, name, parent: 'Node' = None):
        self.parent = parent
        self.name = name
        self.children = []

    def add_child(self, obj: 'Node'):
        self.children.append(obj)

    @property
    def parent_name(self) -> str:
        return self.parent.name if self.parent else None




def to_tree(nodes: List[tuple]) -> dict:
    name_by_node = dict()




if __name__ == '__main__':

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
    expected = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }

    assert to_tree(source) == expected
