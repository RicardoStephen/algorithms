class BinaryTreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        vals = []
        def visit(node):
            if isinstance(node.val, str):
                vals.append(''.join(["'" + str(node.val) + "'"]))
            else:
                vals.append(str(node.val))
        self.inorder(visit)
        return ''.join(['[', ', '.join(vals), ']'])

    ############################################################################
    # Tree traversal
    ############################################################################
    
    def inorder(self, visit):
        if self.left: self.left.inorder(visit)
        visit(self)
        if self.right: self.right.inorder(visit)

    def preorder(self, visit):
        visit(self)
        if self.left: self.left.preorder(visit)
        if self.right: self.right.preorder(visit)

    def postorder(self, visit):
        if self.left: self.left.postorder(visit)
        if self.right: self.right.postorder(visit)
        visit(self)

def magic_printer(tree_and_traversal):
    vals = []
    tree_and_traversal(lambda x: vals.append(str(x.val)))
    print(', '.join(vals))

if __name__ == '__main__':
    
    ctor = BinaryTreeNode

    sherry = ctor(0)
    terry = ctor(40)
    milhouse = ctor(25, sherry, terry)
    lisa = ctor(100)
    nelson = ctor(75, None, lisa)
    bart = ctor(50, milhouse, nelson)

    print(bart)
    print()
    
    x = magic_printer(bart.inorder)
    y = magic_printer(bart.preorder)
    z = magic_printer(bart.postorder)
