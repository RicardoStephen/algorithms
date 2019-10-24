from collections import deque

from test import Utils
from test.test_linkedlist import TestLinkedList
from algorithms.datastructs import Deque


class TestDeque(TestLinkedList):
    """
    Test datastructs.Deque by creating identical doubly linked lists using
    python's deque class and datastructs' Deque class, and then testing
    that identical operations yield equivalent results.
    """

    def setUp(self):
        self.intgen = Utils.int_generator()
        self.strgen = Utils.str_generator()

        states = ['empty', 'one', 'two', 'three', '10']
        self.pylls = dict(zip(states, [deque() for _ in states]))
        self.mylls = dict(zip(states, [Deque() for _ in states]))
        self.add_values(self.mylls['one'], self.pylls['one'])
        self.add_values(self.mylls['two'], self.pylls['two'], 2)
        self.add_values(self.mylls['three'], self.pylls['three'], 3)
        self.add_values(self.mylls['10'], self.pylls['10'], 10)

    def check_equal(self, myll, pyll):
        self.assertEqual(len(myll), len(pyll))
        for myval, pyval in zip(myll, pyll):
            self.assertEqual(myval, pyval)
        for myval, pyval in zip(reversed(myll), reversed(pyll)):
            self.assertEqual(myval, pyval)
        self.check_str(myll, pyll)

    def check_str(self, myll, pyll):
        self.assertEqual(str(myll), str(pyll))

    # Inherit add_values

    # Inherit test_len, test_str

    # Inherit test_appendleft, test_popleft, test_popleft_invalid

    def test_append(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                val = next(self.strgen)
                myll.append(val)
                pyll.append(val)
                self.check_equal(myll, pyll)
                val = next(self.intgen)
                myll.append(val)
                pyll.append(val)
                self.check_equal(myll, pyll)
                val = next(self.strgen)
                myll.append(val)
                pyll.append(val)
                self.check_equal(myll, pyll)

    def test_extend(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                extension = [next(self.strgen)]
                myll.extend(extension)
                pyll.extend(extension)
                self.check_equal(myll, pyll)
                extension = [next(self.intgen) for _ in range(2)]
                myll.extend(extension)
                pyll.extend(extension)
                self.check_equal(myll, pyll)
                extension = [next(self.strgen) for _ in range(3)]
                myll.extend(extension)
                pyll.extend(extension)
                self.check_equal(myll, pyll)

    def test_extend_empty(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                myll.extend([])
                pyll.extend([])
                self.check_equal(myll, pyll)

    def test_pop(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                for i in range(len(pyll)):
                    self.assertEqual(myll.pop(), pyll.pop())
                    self.check_equal(myll, pyll)

    def test_pop_invalid(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                for i in range(len(pyll)):
                    self.assertEqual(myll.pop(), pyll.pop())
                    self.check_equal(myll, pyll)
                with self.assertRaises(IndexError):
                    myll.pop()

    # Inherit test_iter

    def test_reversed(self):
        for pyll, myll in zip(self.pylls.values(), self.mylls.values()):
            with self.subTest(pyll = pyll, myll = myll):
                for myval, pyval in zip(reversed(myll), reversed(pyll)):
                    self.assertEqual(myval, pyval)


if __name__ == '__main__':
    unittest.main()
