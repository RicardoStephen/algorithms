from collections import namedtuple


class LinkedList:

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

    ############################################################################
    # Prepend methods
    ############################################################################

    def appendleft(self, val):
        node = self.Node(val, self.head)
        self.head = node
        self.length += 1

    def popleft(self):
        if self.length == 0:
            raise IndexError('pop from empty list.')
        node = self.head
        self.head = node.next_node
        self.length -= 1
        return node.val

    ############################################################################
    # Value methods
    ############################################################################

    def __contains__(self, val):
        node = self.head
        while node:
            if node.val == val:
                return True
            node = node.next_node
        return False

    def remove(self, val):
        if self.length == 0:
            raise ValueError(f"{val} not in list.")
        if self.head.val == val:
            self.popleft()
            return
        trail = self.head
        lead = trail.next_node
        while lead:
            if lead.val == val:
                trail.next_node = lead.next_node
                self.length -= 1
                return
            lead = lead.next_node
            trail = trail.next_node
        raise ValueError(f"{val} not in list.")


    def __iter__(self):
        node = self.head
        while node:
            yield node.val
            node = node.next_node
