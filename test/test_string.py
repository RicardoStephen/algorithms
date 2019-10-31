import unittest

from algorithms.datastructs import String


class TestString(unittest.TestCase):
    """
    Test datastructs.String by creating identical strings using python's str
    class and datastructs' String class, and then testing that identical
    operations on each yield equivalent results.
    """

    def setUp(self):
        self.pystrs = {
            'empty': '',
            'onec': 'a', 'twoc': 'ab', 'threec': 'abc', '10c': 'abcdefghij',
            'onei': '1', 'twoi': '12', 'threei': '123', '10i': '0123456789',
            'two': 'a1', 'three': 'a1b', 'four': 'a1b2', '10': 'a1b2c3d4e5'}
        self.mystrs = dict([(state, String(pystr))
                            for state, pystr in self.pystrs.items()])

    def test_init(self):
        pass

    def test_init_invalid(self):
        with self.assertRaises(TypeError):
            s = String(1)

    def test_len(self):
        for pystr, mystr in zip(self.pystrs.values(), self.mystrs.values()):
            with self.subTest(pystr = pystr, mystr = mystr):
                self.assertEqual(len(mystr), len(pystr))

    def test_str(self):
        for pystr, mystr in zip(self.pystrs.values(), self.mystrs.values()):
            with self.subTest(pystr = pystr, mystr = mystr):
                self.assertEqual(str(mystr), str(pystr))

    def test_getitem(self):
        for pystr, mystr in zip(self.pystrs.values(), self.mystrs.values()):
            with self.subTest(pystr = pystr, mystr = mystr):
                for i in range(len(pystr)):
                    self.assertEqual(mystr[i], pystr[i])

    def test_getitem_invalid(self):
        for pystr, mystr in zip(self.pystrs.values(), self.mystrs.values()):
            with self.subTest(pystr = pystr, mystr = mystr):
                with self.assertRaises(TypeError):
                    c = mystr['a']
                with self.assertRaises(IndexError):
                    c = mystr[-1]
                with self.assertRaises(IndexError):
                    c = mystr[len(mystr) + 1]


if  __name__ == '__main__':
    unittest.main()
