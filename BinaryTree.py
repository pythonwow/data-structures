from timeit import default_timer as timer
from datetime import timedelta

class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_children(self):
        return [self.left, self.right]

    def has_left(self):
        return True if self.left is not None else False

    def has_right(self):
        return True if self.right is not None else False


class BinaryTree:
    ''''polacz delete i todelete w jedną funkcję'''

    def __init__(self):
        self.root = None

    def insert(self, values):
        def get_place_to_insert(node, value):
            while isinstance(node, Node):
                if value <= node.value:
                    if node.left is None:
                        return node, True
                    node = node.left
                elif value > node.value:
                    if node.right is None:
                        return node, False
                    node = node.right
        if not isinstance(values, list):
            values = [values]
        for value in values:
            if self.root is None:
                self.root = Node(value)
            else:
                node, to_left = get_place_to_insert(self.root, value)
                if to_left:
                    node.left = Node(value)
                else:
                    node.right = Node(value)

    def find(self, value):
        node = self.root
        while node.value is not value:
            node = node.left if value <= node.value else node.right
            if node is None:
                return None
        return node

    def delete(self, value):
        def get_parent(node, parent):
            if node is parent:
                return False
            while node not in parent.get_children():
                parent = parent.left if node.value <= parent.value else parent.right
            return parent

        def get_succ(node):
            if node.has_right():
                succ = node.right
                while succ.left:
                    succ = succ.left
            elif node.has_left():
                succ = node.left
                while succ.right:
                    succ = succ.right
            else:
                succ = False
            return succ

        node = self.find(value)
        if node is None:
            return None
        parent = get_parent(node, self.root)
        succ = get_succ(node)
        if succ:
            succ_parent = get_parent(succ, node)
            if succ_parent:
                if succ_parent.has_left():
                    if succ_parent.left is succ:
                        succ_parent.left = None
                    elif succ_parent.has_right():
                        if succ_parent.right is succ:
                            succ_parent.right = None
        if not parent:
            self.root.value = succ.value
        elif not succ:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
        elif parent.left == node:
            parent.left.value = succ.value
        elif parent.right == node:
            parent.right.value = succ.value



st = timer()
tree = BinaryTree()
values = [5, 3, 6, 2, 4, 6, 10, 11, 10, 0, 1]
tree.insert(values)
tree.delete(3)
et = timer()
diff = (et - st)
print(timedelta(seconds=et-st))



