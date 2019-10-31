from algorithms.baseobject import BaseObject


class BinaryTree(BaseObject):

    class BinaryTreeNode:

        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

        def inorder(self, visit):
            if self.left: self.left.inorder(visit)
            visit(self.val)
            if self.right: self.right.inorder(visit)

        def preorder(self, visit):
            visit(self.val)
            if self.left: self.left.preorder(visit)
            if self.right: self.right.preorder(visit)

        def postorder(self, visit):
            if self.left: self.left.postorder(visit)
            if self.right: self.right.postorder(visit)
            visit(self.val)


    def __init__(self, data = []):
        self.length = len(data) - data.count(None)
        if not data:
            self.root = None
            return
        self.root = self.BinaryTreeNode(data[0])
        def addChildren(node, idx):
            lidx, ridx = 2*idx + 1, 2*idx + 2
            if lidx >= len(data):
                return
            if data[lidx] != None:
                node.left = self.BinaryTreeNode(data[lidx])
                addChildren(node.left, lidx)
            if data[ridx] != None:
                node.right = self.BinaryTreeNode(data[ridx])
                addChildren(node.right, ridx)
        addChildren(self.root, 0)

    def __len__(self):
        return self.length

    def __str__(self):
        serialized = []
        current_queue = []
        next_queue = [self.root]
        while any(next_queue):
            current_queue = next_queue
            next_queue = []
            for node in current_queue:
                if node:
                    if isinstance(node.val, str):
                        serialized.append(''.join(['\'', str(node.val), '\'']))
                    else:
                        serialized.append(str(node.val))
                    next_queue.append(node.left)
                    next_queue.append(node.right)
                else:
                    serialized.append('None')
                    next_queue.append(None)
                    next_queue.append(None)
        return ''.join(['[', ', '.join(serialized), ']'])

    def inorder(self, visit):
        if self.root:
            self.root.inorder(visit)

    def preorder(self, visit):
        if self.root:
            self.root.preorder(visit)

    def postorder(self, visit):
        if self.root:
            self.root.postorder(visit)
