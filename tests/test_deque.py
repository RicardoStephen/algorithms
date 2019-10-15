import unittest
from collections import deque

from tests.test_linkedlist import TestLinkedList
from datastructs import Deque


class TestDeque(TestLinkedList):
    """
    Test datastructs.Deque by creating identical doubly linked lists using
    python's deque class and datastructs' Deque class, and then testing
    that identical operations yield equivalent results.
    """
    
    def setUp(self):
        subtests = [([]),
                    ([1]),
                    ([1, 2, 3]),
                    ([]),
                    (['hello']),
                    (['hello', 'there', 'world']),
                    (['hello', 1, 'world']),
                    ([2, 'there', 3, 'foo', 'bar'])]

        self.pylls = [deque(ll) for ll in subtests]
        self.mylls = [Deque() for i in range(len(self.pylls))]
        for pyll, myll in zip(self.pylls, self.mylls):
            for val in reversed(pyll):
                myll.appendleft(val)
        self.extra_arrs = [[], [1], [2, 'a'], [3, 'b', 'c']]

    # Inherit:
    # + test_len, test_srt
    # + test_appendleft_popleft
    # + test_contains, test_remove, test_iter

    def test_append_pop(self):
        for pyll, myll in zip(self.pylls, self.mylls):
            with self.subTest(pyll = pyll, myll = myll):
                pyll_copy = pyll.copy()
                # Test append 0, 1, 2, 3 elements.
                def test_append(arr):
                    for x in arr:
                        myll.append(x)
                        pyll.append(x)
                    self.assertEqual(len(myll), len(pyll))
                    for myval, pyval in zip(myll, pyll):
                        self.assertEqual(myval, pyval)
                for arr in self.extra_arrs:
                    test_append(arr)
                # Test pop undo "append 0, 1, 2, 3 elements".
                def test_pop_n(n):
                    for i in range(n):
                        myval, pyval = myll.pop(), pyll.pop()
                        self.assertEqual(myval, pyval)
                    self.assertEqual(len(myll), len(pyll))
                    for myval2, pyval2 in zip(myll, pyll):
                        self.assertEqual(myval2, pyval2)
                for arr in self.extra_arrs:
                    test_pop_n(len(arr))
                # Test pop from empty list.
                popped = []
                for _ in range(len(myll)):
                    myval, pyval = myll.pop(), pyll.pop()
                    popped.append(myval)
                    self.assertEqual(myval, pyval)
                    self.assertEqual(len(myll), len(pyll))
                    for myval2, pyval2 in zip(myll, pyll):
                        self.assertEqual(myval2, pyval2)
                with self.assertRaises(IndexError):
                    myll.pop()
                for x in reversed(popped):
                    myll.append(x)
                    pyll.append(x)
                    self.assertEqual(len(myll), len(pyll))
                    for myval, pyval in zip(myll, pyll):
                        self.assertEqual(myval, pyval)
                # Check that values have been properly reset.
                for myval, pyval, cval in zip(myll, pyll, pyll_copy):
                    self.assertEqual(myval, cval)
                    self.assertEqual(pyval, cval)

    def test_extend_pop(self):
        for pyll, myll in zip(self.pylls, self.mylls):
            with self.subTest(pyll = pyll, myll = myll):
                pyll_copy = pyll.copy()
                # Test extend by 0, 1, 2, 3 elements.
                def test_append(arr):
                    myll.extend(arr)
                    pyll.extend(arr)
                    self.assertEqual(len(myll), len(pyll))
                    for myval, pyval in zip(myll, pyll):
                        self.assertEqual(myval, pyval)
                for arr in self.extra_arrs:
                    test_append(arr)
                # Test pop undo "extend by 0, 1, 2, 3 elements".
                def test_pop_n(n):
                    for i in range(n):
                        myval, pyval = myll.pop(), pyll.pop()
                        self.assertEqual(myval, pyval)
                    self.assertEqual(len(myll), len(pyll))
                    for myval2, pyval2 in zip(myll, pyll):
                        self.assertEqual(myval2, pyval2)
                for arr in self.extra_arrs:
                    test_pop_n(len(arr))
                # Check that values have been properly reset.
                for myval, pyval, cval in zip(myll, pyll, pyll_copy):
                    self.assertEqual(myval, cval)
                    self.assertEqual(pyval, cval)

    def test_reversed(self):
        for pyll, myll in zip(self.pylls, self.mylls):
            with self.subTest(pyll = pyll, myll = myll):
                for myval, pyval in zip(reversed(myll), reversed(pyll)):
                    self.assertEqual(myval, pyval)

if __name__ == '__main__':
    unittest.main()
