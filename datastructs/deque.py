from collections import namedtuple

from datastructs.linkedlist import LinkedList


class Deque(LinkedList):

    class Node:

        def __init__(self, val, next_node=None, prev_node=None):
            self.val = val
            self.next_node = next_node
            self.prev_node = prev_node

    def __init__(self):
        super().__init__()
        self.tail = None

    # Inherit __len__, __str__

    ############################################################################
    # Prepend methods
    ############################################################################

    def appendleft(self, val):
        if self.length == 0:
            node = self.Node(val)
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node = self.Node(val, self.head, None)
            self.head.prev_node = node
            self.head = node
            self.length += 1

    def popleft(self):
        if self.length == 0:
            raise IndexError('pop from empty list.')
        elif self.length == 1:
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node.val
        else:
            node = self.head
            node.next_node.prev_node = None
            self.head = node.next_node
            self.length -= 1
            return node.val

    ############################################################################
    # Append methods
    ############################################################################

    def append(self, val):
        if self.length == 0:
            self.appendleft(val)
        else:
            node = self.Node(val, None, self.tail)
            self.tail.next_node = node
            self.tail = node
            self.length += 1

    def extend(self, arr):
        if not arr:
            return
        if len(arr) == 1:
            self.append(arr[0])
        else:
            # Build a chain of nodes.
            nodes = [self.Node(val) for val in arr]
            for i in range(1, len(nodes)):
                nodes[i].prev_node = nodes[i-1]
            for i in range(0, len(nodes)-1):
                nodes[i].next_node = nodes[i+1]
            # Append the chain to the list.
            if self.length == 0:
                nodes[0].prev_node = None
                self.head = nodes[0]
                self.tail = nodes[-1]
                self.length = len(nodes)
            else:
                self.tail.next_node = nodes[0]
                nodes[0].prev_node = self.tail
                self.tail = nodes[-1]
                self.length += len(nodes)

    def pop(self):
        if self.length == 0:
            raise IndexError('pop from empty list.')
        elif self.length == 1:
            return self.popleft()
        else:
            node = self.tail
            node.prev_node.next_node = None
            self.tail = node.prev_node
            self.length -= 1
            return node.val

    ############################################################################
    # Value methods
    ############################################################################

    # Inherit __contains__

    def remove(self, val):
        if self.length == 0:
            raise ValueError(f"{val} not in list.")
        if self.head.val == val:
            self.popleft()
            return
        if self.tail.val == val:
            self.pop()
            return
        node = self.head.next_node
        while node:
            if node.val == val:
                node.prev_node.next_node = node.next_node
                node.next_node.prev_node = node.prev_node
                self.length -= 1
                return
            node = node.next_node
        raise ValueError(f"{val} not in list.")


    # Inherit __iter__

    def __reversed__(self):
        node = self.tail
        while node:
            yield node.val
            node = node.prev_node
