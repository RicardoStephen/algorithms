from collections import namedtuple

from algorithms.datastructs.linkedlist import LinkedList


class Deque(LinkedList):

    class Node:

        def __init__(self, val, next_node=None, prev_node=None):
            self.val = val
            self.next_node = next_node
            self.prev_node = prev_node

    def __init__(self):
        super().__init__()
        self.tail = None

    # Inherit __len__

    def __str__(self):
        return ''.join(['deque(', super().__str__(), ')'])

    def appendleft(self, val):
        node = self.Node(val, self.head)
        if self.head:
            self.head.prev_node = node
        else:
            self.tail = node
        self.head = node
        self.length += 1

    def popleft(self):
        if not self.head:
            raise IndexError('Pop from empty list.')
        node = self.head
        self.head = self.head.next_node
        if self.head:
            self.head.prev_node = None
        else:
            self.tail = None
        self.length -= 1
        return node.val

    def append(self, val):
        node = self.Node(val, prev_node = self.tail)
        if self.tail:
            self.tail.next_node = node
        else:
            self.head = node
        self.tail = node
        self.length += 1

    def extend(self, arr):
        if not arr:
            return
        self.append(arr[0])
        for i in range(1, len(arr)):
            node = self.Node(arr[i], prev_node = self.tail)
            self.tail.next_node = node
            self.tail = node
        self.length += len(arr) - 1

    def pop(self):
        if not self.tail:
            raise IndexError('Pop from empty list.')
        node = self.tail
        self.tail = node.prev_node
        if self.tail:
            self.tail.next_node = None
        else:
            self.head = None
        self.length -= 1
        return node.val

    # Inherit __iter__

    def __reversed__(self):
        node = self.tail
        while node:
            yield node.val
            node = node.prev_node
