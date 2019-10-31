from collections import namedtuple

from algorithms.baseobject import BaseObject


class LinkedList(BaseObject):

    class Node:

        def __init__(self, val, next_node=None):
            self.val = val
            self.next_node = next_node

    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        s = []
        for x in self:
            if isinstance(x, str):
                s.append(''.join(["'", str(x), "'"]))
            else:
                s.append(str(x))
        s = ', '.join(s)
        s = ''.join(['[', s, ']'])
        return s

    def appendleft(self, val):
        node = self.Node(val, self.head)
        self.head = node
        self.length += 1

    def popleft(self):
        if self.length == 0:
            raise IndexError('Pop from empty list.')
        node = self.head
        self.head = node.next_node
        self.length -= 1
        return node.val

    def __iter__(self):
        node = self.head
        while node:
            yield node.val
            node = node.next_node
