import unittest

from datastructs import Array


class TestArray(unittest.TestCase):
    """
    Test datastructs.Array by creating identical arrays using python's list
    class and datastructs' Array class, and then testing that identical
    operations on each yield equivalent results.
    """

    def setUp(self):
        subtests = [([], int),
                    ([1], int),
                    ([1, 2, 3], int),
                    ([], str),
                    (['hello'], str),
                    (['hello', 'there', 'world'], str)]

        self.pyarrs = [pyarr for pyarr, _ in subtests]
        self.myarrs = [Array(dtype, len(pyarr)) for pyarr, dtype in subtests]
        for pyarr, myarr in zip(self.pyarrs, self.myarrs):
            for idx, elem in enumerate(pyarr):
                myarr[idx] = elem

    def test_len(self):
        for pyarr, myarr in zip(self.pyarrs, self.myarrs):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                self.assertEqual(len(myarr), len(pyarr))

    def test_str(self):
        for pyarr, myarr in zip(self.pyarrs, self.myarrs):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                self.assertEqual(str(myarr), str(pyarr))

    def test_getitem(self):
        for pyarr, myarr in zip(self.pyarrs, self.myarrs):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                for idx in range(len(myarr)):
                    self.assertEqual(myarr[idx], pyarr[idx])
                # Test that the index is of a valid type and within range.
                with self.assertRaises(TypeError):
                    x = myarr['a']
                with self.assertRaises(IndexError):
                    x = myarr[-1]
                with self.assertRaises(IndexError):
                    x = myarr[len(myarr) + 1]

    def test_setitem(self):
        for pyarr, myarr in zip(self.pyarrs, self.myarrs):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                pyarr_copy = pyarr.copy()
                replacement_val = myarr.dtype()
                for i in range(len(myarr)):
                    original_val = myarr[i]
                    myarr[i] = replacement_val
                    pyarr[i] = replacement_val
                    for j in range(len(myarr)):
                        self.assertEqual(myarr[j], pyarr[j])
                    myarr[i] = original_val
                    pyarr[i] = original_val
                    for j in range(len(myarr)):
                        self.assertEqual(myarr[j], pyarr[j])
                # Test that the index is of a valid type and within range.
                with self.assertRaises(TypeError):
                    myarr['a'] = replacement_val
                with self.assertRaises(IndexError):
                    myarr[-1] = replacement_val
                with self.assertRaises(IndexError):
                    myarr[len(myarr) + 1] = replacement_val
                # Test that assigned value is of the valid type.
                if myarr:
                    with self.assertRaises(TypeError):
                        replacement_val = str() if myarr.dtype == int else int()
                        myarr[0] = replacement_val()
                # Check that values have been properly reset.
                for myval, pyval, cval in zip(myarr, pyarr, pyarr_copy):
                    self.assertEqual(myval, cval)
                    self.assertEqual(pyval, cval)
                    
    def test_iter(self):
        for pyarr, myarr in zip(self.pyarrs, self.myarrs):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                for myelem, pyelem in zip(myarr, pyarr):
                    myelem == pyelem


if  __name__ == '__main__':
    unittest.main()
