import unittest
from collections import deque

from test import Utils
from algorithms.datastructs import LinkedList


class TestLinkedList(unittest.TestCase):
    """
    Test datastructs.LinkedList by creating identical linked lists using
    python's deque class and datastructs' LinkedList class, and then testing
    that identical operations yield equivalent results.
    """

    def setUp(self):
        self.intgen = Utils.int_generator()
        self.strgen = Utils.str_generator()

        states = ['empty', 'one', 'two', 'three', '10']
        self.pylls = dict(zip(states, [deque() for _ in states]))
        self.mylls = dict(zip(states, [LinkedList() for _ in states]))
        self.add_values(self.mylls['one'], self.pylls['one'])
        self.add_values(self.mylls['two'], self.pylls['two'], 2)
        self.add_values(self.mylls['three'], self.pylls['three'], 3)
        self.add_values(self.mylls['10'], self.pylls['10'], 10)

    def check_equal(self, myll, pyll):
        self.assertEqual(len(myll), len(pyll))
        for myval, pyval in zip(myll, pyll):
            self.assertEqual(myval, pyval)
        self.check_str(myll, pyll)

    def check_str(self, myll, pyll):
        self.assertEqual(str(myll), str(pyll)[6:-1])

    def add_values(self, myll, pyll, count=1):
        for i in range(count // 2):
            val = next(self.strgen)
            myll.appendleft(val)
            pyll.appendleft(val)
            self.check_equal(myll, pyll)
            val = next(self.intgen)
            myll.appendleft(val)
            pyll.appendleft(val)
            self.check_equal(myll, pyll)
        if count % 2:
            val = next(self.strgen)
            myll.appendleft(val)
            pyll.appendleft(val)
            self.check_equal(myll, pyll)

    def test_len(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                self.assertEqual(len(myll), len(pyll))

    def test_str(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                self.check_str(myll, pyll)

    def test_appendleft(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                self.add_values(myll, pyll, 3)

    def test_popleft(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                for i in range(len(pyll)):
                    self.assertEqual(myll.popleft(), pyll.popleft())
                    self.check_equal(myll, pyll)

    def test_popleft_invalid(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                for i in range(len(pyll)):
                    self.assertEqual(myll.popleft(), pyll.popleft())
                    self.check_equal(myll, pyll)
                with self.assertRaises(IndexError):
                    myll.popleft()

    def test_iter(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                for myval, pyval in zip(myll, pyll):
                    self.assertEqual(myval, pyval)


if __name__ == '__main__':
    unittest.main()
