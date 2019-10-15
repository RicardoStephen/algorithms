from BinaryTreeNode import BinaryTreeNode

class BinarySearchTreeNode(BinaryTreeNode):

    # Inherit __init__, __str__

    # Inherit inorder, preorder, postorder
    
    def add(self, val):
        if val == self.val:
            return False
        if val <= self.val:
            if self.left:
                return self.left.add(val)
            self.left = type(self)(val)
        else:
            if self.right:
                return self.right.add(val)
            self.right = type(self)(val)
        return True

    def __contains__(self, val):
        if vall == self.val:
            return True
        child = self.left if val <= self.val else self.right
        if not child:
            return False
        return child.contains(val)

    
if __name__ == '__main__':
    bart = BinarySearchTreeNode((50, 'bart'))
    print(bart)

    bart.add((25, 'milhouse'))
    bart.add((75, 'nelson'))
    bart.add((15, 'sherry'))
    bart.add((35, 'terry'))
    bart.add((100, 'lisa'))
    print(bart)

    print((101, 'homer')) in bart)
    print((100, 'lisa')) in bart)
    print((25, 'milhouse')) in bart)
    print((45, 'martin')) in bart)
