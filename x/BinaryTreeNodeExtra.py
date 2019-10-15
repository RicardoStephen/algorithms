class BinaryTreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = str(val)
        self.left = left
        self.right = right

    def __str__(self):
        vals = []
        self.inorder(lambda x: vals.append(''.join(["'", str(x.val), "'"]) if
                                           isinstance(x.val, str) else
                                           str(x.val)))
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

    ############################################################################
    # Miscellany
    ############################################################################
    
    def is_balanced(self):
        def get_height_balanced(node):
            if not node:
                return 0, True
            lheight, lbalanced = get_height_balanced(node.left)
            rheight, rbalanced = get_height_balanced(node.right)
            return (max(lheight, rheight) + 1,
                    lbalanced and rbalanced and abs(lheight - rheight) <= 1)
        return get_height_balanced(self)[1]

    def is_symmetric(self):
        def check_mirrors(lsubtree, rsubtree):
            if not lsubtree and not rsubtree:
                return True
            elif lsubtree and rsubtree:
                return (lsubtree.data == rsubtree.data and
                        check_mirrors(lsubtree.left, rsubtree.right) and
                        check_mirrors(lsubtree.right, rsubtree.left))
            else:
                return False
    return check_mirrors(self.left, self.right)

    ############################################################################
    # Tree traversal (iterative)
    ############################################################################

    def inorder_iterative(self, visit):
        ancestors = []
        undiscovered = self
        while undiscovered or ancestors:
            if undiscovered:
                if undiscovered.left:
                    ancestors.append(undiscovered)
                    undiscovered = undiscovered.left
                else:
                    visit(undiscovered)
                    undiscovered = undiscovered.right
            else:
                ancestor = ancestors.pop()
                visit(ancestor)
                undiscovered = ancestor.right

    def preorder_iterative(self, visit):
        ancestors = []
        undiscovered = self
        while undiscovered or ancestors:
            if undiscovered:
                visit(undiscovered)
                if undiscovered.left:
                    ancestors.append(undiscovered)
                    undiscovered = undiscovered.left
                else:
                    undiscovered = undiscovered.right
            else:
                ancestor = ancestors.pop()
                undiscovered = ancestor.right

    def postorder_iterative(self, visit):
        ancestors = []
        waiting_on_left = [] # Track whether the ancestor is waiting on their
                             #   left or right child.
        undiscovered = self
        while undiscovered or ancestors:
            if undiscovered:
                if undiscovered.left:
                    ancestors.append(undiscovered)
                    waiting_on_left.append(True)
                    undiscovered = undiscovered.left
                elif undiscovered.right:
                    ancestors.append(undiscovered)
                    waiting_on_left.append(False)
                    undiscovered = undiscovered.right
                else:
                    visit(undiscovered)
                    undiscovered = None
            else:
                ancestor = ancestors.pop()
                is_waiting_on_left = waiting_on_left.pop()
                if is_waiting_on_left:
                    if ancestor.right:
                        ancestors.append(ancestor)
                        waiting_on_left.append(False)
                        undiscovered = ancestor.right
                    else:
                        visit(ancestor)
                else:
                    visit(ancestor)

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
    print()
    
    x2 = magic_printer(bart.inorder_iterative)
    y2 = magic_printer(bart.preorder_iterative)
    z2 = magic_printer(bart.postorder_iterative)
    print()

    assert(x == x2)
    assert(y == y2)
    assert(z == z2)
