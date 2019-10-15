import unittest
from collections import deque

from datastructs import LinkedList


class TestLinkedList(unittest.TestCase):
    """
    Test datastructs.LinkedList by creating identical linked lists using
    python's deque class and datastructs' LinkedList class, and then testing
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
        self.mylls = [LinkedList() for i in range(len(self.pylls))]
        for pyll, myll in zip(self.pylls, self.mylls):
            for val in reversed(pyll):
                myll.appendleft(val)
        self.extra_arrs = [[], [1], [2, 'a'], [3, 'b', 'c']]

    def test_len(self):
        for pyll, myll in zip(self.pylls, self.mylls):
            with self.subTest(pyll = pyll, myll = myll):
                self.assertEqual(len(myll), len(pyll))

    def test_str(self):
        for pyll, myll in zip(self.pylls, self.mylls):
            with self.subTest(pyll = pyll, myll = myll):
                self.assertEqual(str(myll), str(list(pyll)))

    def test_appendleft_popleft(self):
        for pyll, myll in zip(self.pylls, self.mylls):
            with self.subTest(pyll = pyll, myll = myll):
                pyll_copy = pyll.copy()
                # Test appendleft 0, 1, 2, 3 elements.
                def test_appendleft(arr):
                    for x in arr:
                        myll.appendleft(x)
                        pyll.appendleft(x)
                    self.assertEqual(len(myll), len(pyll))
                    for myval, pyval in zip(myll, pyll):
                        self.assertEqual(myval, pyval)
                for arr in self.extra_arrs:
                    test_appendleft(arr)
                # Test popleft undo "appendleft 0, 1, 2, 3 elements".
                def test_popleft_n(n):
                    for i in range(n):
                        myval, pyval = myll.popleft(), pyll.popleft()
                        self.assertEqual(myval, pyval)
                    self.assertEqual(len(myll), len(pyll))
                    for myval2, pyval2 in zip(myll, pyll):
                        self.assertEqual(myval2, pyval2)
                for arr in self.extra_arrs:
                    test_popleft_n(len(arr))
                # Test popleft from empty list.
                popped = []
                for _ in range(len(myll)):
                    myval, pyval = myll.popleft(), pyll.popleft()
                    popped.append(myval)
                    self.assertEqual(myval, pyval)
                    self.assertEqual(len(myll), len(pyll))
                    for myval2, pyval2 in zip(myll, pyll):
                        self.assertEqual(myval2, pyval2)
                with self.assertRaises(IndexError):
                    myll.popleft()
                for x in reversed(popped):
                    myll.appendleft(x)
                    pyll.appendleft(x)
                    self.assertEqual(len(myll), len(pyll))
                    for myval, pyval in zip(myll, pyll):
                        self.assertEqual(myval, pyval)
                # Check that values have been properly reset.
                for myval, pyval, cval in zip(myll, pyll, pyll_copy):
                    self.assertEqual(myval, cval)
                    self.assertEqual(pyval, cval)

    def test_contains(self):
        for pyll, myll in zip(self.pylls, self.mylls):
            with self.subTest(pyll = pyll, myll = myll):
                for x in pyll:
                    self.assertIn(x, myll)

    def test_remove(self):
        for pyll, myll in zip(self.pylls, self.mylls):
            with self.subTest(pyll = pyll, myll = myll):
                pyll_copy = pyll.copy()
                # Test removing values not in the list.
                # Generate a value not in the list by finding the minimum int in
                # the list, and decreasing it by 1.
                myll_ints = list(filter(lambda x : isinstance(x, int), myll))
                myll_ints.append(0)
                remove_val = min(myll_ints) - 1
                with self.assertRaises(ValueError):
                    x = myll.remove(remove_val)
                # Test remove.
                for x in pyll_copy:
                    myll.remove(x)
                    pyll.remove(x)
                    self.assertEqual(len(myll), len(pyll))
                    for myval, pyval in zip(myll, pyll):
                        self.assertEqual(myval, pyval)
                # Test removing from empty list.
                with self.assertRaises(ValueError):
                    x = myll.remove(0)
                # Reset the values.
                for x in reversed(pyll_copy):
                    myll.appendleft(x)
                    pyll.appendleft(x)
                    self.assertEqual(len(myll), len(pyll))
                    for myval, pyval in zip(myll, pyll):
                        self.assertEqual(myval, pyval)
                # Check that values have been properly reset.
                for myval, pyval, cval in zip(myll, pyll, pyll_copy):
                    self.assertEqual(myval, cval)
                    self.assertEqual(pyval, cval)

    def test_iter(self):
        for pyll, myll in zip(self.pylls, self.mylls):
            with self.subTest(pyll = pyll, myll = myll):
                for myval, pyval in zip(myll, pyll):
                    self.assertEqual(myval, pyval)


if __name__ == '__main__':
    unittest.main()
