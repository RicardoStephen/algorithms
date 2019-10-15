import unittest

from tests.test_array import TestArray
from datastructs.arraylist import ArrayList


class TestArrayList(TestArray):
    """
    Test datastructs.ArrayList by creating identical resizeable arrays using
    python's list class and datastructs' ArrayList class, and then testing that
    identical operations on each yield equivalent results.
    """

    def setUp(self):
        subtests = [([], int),
                    ([1], int),
                    ([1, 2, 3], int),
                    (list(range(ArrayList.DEFAULT_INTERNAL_LENGTH + 1)), int),
                    (list(range(ArrayList.GROWTH_FACTOR *
                                ArrayList.DEFAULT_INTERNAL_LENGTH + 1)), int),
                    ([], str),
                    (['hello'], str),
                    (['hello', 'there', 'world'], str),
                    (['hello'] * (ArrayList.DEFAULT_INTERNAL_LENGTH + 1), str),
                    (['hello'] * (ArrayList.GROWTH_FACTOR *
                                  ArrayList.DEFAULT_INTERNAL_LENGTH + 1), str)]

        self.pyarrs = [pyarr for pyarr, _ in subtests]
        self.myarrs = [ArrayList(dtype, len(pyarr)) for pyarr, dtype in subtests]
        for pyarr, myarr in zip(self.pyarrs, self.myarrs):
            for idx, elem in enumerate(pyarr):
                myarr[idx] = elem

    # Inherit:
    # + test_len, test_str
    # + test_getitem, test_setitem, test_iter

    def test_append_pop(self):
        for pyarr, myarr in zip(self.pyarrs, self.myarrs):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                pyarr_copy = pyarr.copy()
                append_val = myarr.dtype()
                # Test append 1, 2, 3 elements.
                def test_append_n(n):
                    for i in range(n):
                        myarr.append(append_val)
                        pyarr.append(append_val)
                    self.assertEqual(len(myarr), len(pyarr))
                    for i in range(len(myarr)):
                        self.assertEqual(myarr[i], pyarr[i])
                test_append_n(1)
                test_append_n(2)
                test_append_n(3)
                # Test append elements until resize.
                target_len = ArrayList.DEFAULT_INTERNAL_LENGTH
                while target_len <= len(myarr):
                    target_len *= ArrayList.GROWTH_FACTOR
                append_len = (target_len + 1) - len(myarr)
                test_append_n(append_len)
                # Test append elements until resize 2.
                target_len *= ArrayList.GROWTH_FACTOR
                append_len_2 = (target_len + 1) - len(myarr)
                test_append_n(append_len_2)
                # Test pop undo "append elements until resize 2".
                def test_pop_n(n):
                    for i in range(n):
                        myval, pyval = myarr.pop(), pyarr.pop()
                        self.assertEqual(myval, pyval)
                    self.assertEqual(len(myarr), len(pyarr))
                    for i in range(len(myarr)):
                        self.assertEqual(myarr[i], pyarr[i])
                test_pop_n(append_len_2)
                # Test pop undo "append elements until resize".
                test_pop_n(append_len)
                # Test pop undo "append 1, 2, 3 elements".
                test_pop_n(3)
                test_pop_n(2)
                test_pop_n(1)
                # Test append invalid value.
                with self.assertRaises(TypeError):
                    append_val = str() if myarr.dtype == int else int()
                    myarr.append(append_val)
                # Check that values have been properly reset.
                for myval, pyval, cval in zip(myarr, pyarr, pyarr_copy):
                    self.assertEqual(myval, cval)
                    self.assertEqual(pyval, cval)

    def test_extend_pop(self):
        for pyarr, myarr in zip(self.pyarrs, self.myarrs):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                pyarr_copy = pyarr.copy()
                extend_val = myarr.dtype()
                # Test extend by 0, 1, 2, 3 elements.
                def test_extend_n(n):
                    myarr.extend([extend_val]*n)
                    pyarr.extend([extend_val]*n)
                    self.assertEqual(len(myarr), len(pyarr))
                    for i in range(len(myarr)):
                        self.assertEqual(myarr[i], pyarr[i])
                test_extend_n(0)
                test_extend_n(1)
                test_extend_n(2)
                test_extend_n(3)
                # Test extend until resize.
                target_len = ArrayList.DEFAULT_INTERNAL_LENGTH
                while target_len <= len(myarr):
                    target_len *= ArrayList.GROWTH_FACTOR
                extend_len = (target_len + 1) - len(myarr)
                test_extend_n(extend_len)
                # Test extend until resize 2.
                target_len *= ArrayList.GROWTH_FACTOR
                extend_len_2 = (target_len + 1) - len(myarr)
                test_extend_n(extend_len_2)
                # Test pop undo "extend until resize 2".
                def test_pop_n(n):
                    for i in range(n):
                        myval, pyval = myarr.pop(), pyarr.pop()
                        self.assertEqual(myval, pyval)
                    self.assertEqual(len(myarr), len(pyarr))
                    for i in range(len(myarr)):
                        self.assertEqual(myarr[i], pyarr[i])
                test_pop_n(extend_len_2)
                # Test pop undo "extend until resize".
                test_pop_n(extend_len)
                # Test pop undo "extend by 0, 1, 2, 3 elements".
                test_pop_n(3)
                test_pop_n(2)
                test_pop_n(1)
                # Test extend with invalid value.
                with self.assertRaises(TypeError):
                    extend_val = [str()] if myarr.dtype == int else [int()]
                    myarr.extend(extend_val)
                # Check that values have been properly reset.
                for myval, pyval, cval in zip(myarr, pyarr, pyarr_copy):
                    self.assertEqual(myval, cval)
                    self.assertEqual(pyval, cval)

    def test_pop(self):
        for pyarr, myarr in zip(self.pyarrs, self.myarrs):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                pyarr_copy = pyarr.copy()
                # Test pop until the list is empty.
                popped = []
                for i in range(len(myarr)):
                    myval, pyval = myarr.pop(), pyarr.pop()
                    popped.append(myval)
                    self.assertEqual(myval, pyval)
                    self.assertEqual(len(myarr), len(pyarr))
                    for j in range(len(myarr)):
                        self.assertEqual(myarr[j], pyarr[j])
                # Test pop from an empty list.
                with self.assertRaises(IndexError):
                    x = myarr.pop()
                # Put back the popped values.
                for x in reversed(popped):
                    myarr.append(x)
                    pyarr.append(x)
                # Check that values have been properly reset.
                for myval, pyval, cval in zip(myarr, pyarr, pyarr_copy):
                    self.assertEqual(myval, cval)
                    self.assertEqual(pyval, cval)

    
if  __name__ == '__main__':
    unittest.main()
