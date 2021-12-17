class Node:
    def __init__(self, elem):
        self.data = elem
        self.left = None
        self.right = None
        self.ltag = 0
        self.rtag = 0


def create_bitree(tree, isroot):
    elem = input('请输入数字')
    node = None
    if elem != '#':
        node = Node(elem)
        if isroot:
            tree.root = node
        node.left = create_bitree(tree, False)
        node.right = create_bitree(tree, False)
    return node


def preordertraverse(t):
    if t is None:
        return
    print(t.data)
    preordertraverse(t.left)
    preordertraverse(t.right)


def inordertraverse(t):
    if t is None:
        return
    inordertraverse(t.left)
    print(t.data)
    inordertraverse(t.right)


def postordertraverse(t):
    if t is None:
        return
    postordertraverse(t.left)
    postordertraverse(t.right)
    print(t.data)


pre = Node(1)


def intreading(t):
    if t:
        intreading(t.left)
        global pre
        if t.left is None:
            t.ltag = 1
            t.left = pre
        if pre.right is None:
            pre.rtag = 1
            pre.right = t

        pre = t
        intreading(t.right)


def inordertraverse_thr(t):
    while t is not None:
        while t.ltag == 0:
            t = t.left
        print(t.data)
        while t.rtag == 1 and t.right is not None:
            t = t.right
            print(t.data)
        t = t.right


class Tree:
    def __init__(self):
        self.root = None

    def root(self):
        return self.root
