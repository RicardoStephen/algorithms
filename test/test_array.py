import unittest

from test import Utils
from algorithms.datastructs import Array


class TestArray(unittest.TestCase):
    """
    Test datastructs.Array by creating identical arrays using python's list
    class and datastructs' Array class, and then testing that identical
    operations on each yield equivalent results.
    """

    def setUp(self):
        self.intgen = Utils.int_generator()
        self.strgen = Utils.str_generator()

        self.pyarrs = {
            'emptyi':[],
            'onei': [0], 'twoi': [0]*2, 'threei': [0]*3, '10i': [0]*10,
            'emptys': [],
            'ones': [''], 'twos': ['']*2, 'threes': ['']*3, '10s': ['']*10}
        self.myarrs = dict()
        for state, arr in self.pyarrs.items():
            if state[-1] == 'i':
                self.myarrs[state] = Array(int, len(arr))
            else:
                self.myarrs[state] = Array(str, len(arr))

    def check_equal(self, myarr, pyarr):
        self.assertEqual(len(myarr), len(pyarr))
        for idx in range(len(pyarr)):
            self.assertEqual(myarr[idx], pyarr[idx])
        self.assertEqual(str(myarr), str(pyarr))

    def test_init_invalid(self):
        with self.assertRaises(TypeError):
            x = Array(1)
        with self.assertRaises(TypeError):
            x = Array(int, 'c')
        with self.assertRaises(ValueError):
            x = Array(int, -1)

    def test_len(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                self.assertEqual(len(myarr), len(pyarr))

    def test_str(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                self.assertEqual(str(myarr), str(pyarr))

    def test_getitem(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                for idx in range(len(pyarr)):
                    self.assertEqual(myarr[idx], pyarr[idx])

    def test_getitem2(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                for idx in range(len(pyarr)):
                    if myarr.dtype == int:
                        val = next(self.intgen)
                    else:
                        val = next(self.strgen)
                    pyarr[idx] = val
                    myarr[idx] = val
                for idx in range(len(pyarr)):
                    self.assertEqual(myarr[idx], pyarr[idx])

    def test_getitem_invalid(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                with self.assertRaises(TypeError):
                    x = myarr['a']
                with self.assertRaises(IndexError):
                    x = myarr[-1]
                with self.assertRaises(IndexError):
                    x = myarr[len(myarr) + 1]

    def test_setitem(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                for i in range(len(pyarr)):
                    if myarr.dtype == int:
                        val = next(self.intgen)
                    else:
                        val = next(self.strgen)
                    myarr[i] = val
                    pyarr[i] = val
                    self.check_equal(myarr, pyarr)

    def test_setitem_invalid(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                with self.assertRaises(TypeError):
                    x = myarr['a']
                with self.assertRaises(IndexError):
                    x = myarr[-1]
                with self.assertRaises(IndexError):
                    x = myarr[len(myarr) + 1]
                if not pyarr:
                    continue
                with self.assertRaises(TypeError):
                    if myarr.dtype == int:
                        myarr[0] = str()
                    else:
                        myarr[0] = int()


if  __name__ == '__main__':
    unittest.main()
