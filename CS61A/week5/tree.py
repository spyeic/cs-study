

class Tree:
    def __init__(self, value):
        self.branches = []
        self.value = value

    def append(self, tree):
        self.branches.append(tree)
