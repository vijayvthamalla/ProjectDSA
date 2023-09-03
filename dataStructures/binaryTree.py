class Node:

    def __init__(self, value):
        self.node = value
        self.lchild = None
        self.rchild = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def display(self):
        self._display(self.root, 0)
        print()

    def _display(self, p, level):
        if p is None:
            return
        self._display(p.rchild, level + 1)
        print()

        for i in range(level):
            print("    ", end='')
        print(p.info)
        self._display(p.lchild, level + 1)
