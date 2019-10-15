import unittest

from datastructs import String

class TestString(unittest.TestCase):
    """
    Test datastructs.String by creating identical strings using python's str
    class and datastructs' String class, and then testing that identical
    operations on each yield equivalent results.
    """

    def setUp(self):
        subtests = ['',
                    'Hello',
                    'World',
                    'Hello World']
        
        self.pystrings = subtests
        self.mystrings = [String(s) for s in subtests]

    def test_init(self):
        with self.assertRaises(TypeError):
            s = String(1)
    
    def test_len(self):
        for pys, mys in zip(self.pystrings, self.mystrings):
            with self.subTest(pys = pys, mys = mys):
                self.assertEqual(len(mys), len(pys))

    def test_str(self):
        for pys, mys in zip(self.pystrings, self.mystrings):
            with self.subTest(pys = pys, mys = mys):
                self.assertEqual(str(mys), str(pys))

    def test_getitem(self):
        for pys, mys in zip(self.pystrings, self.mystrings):
            with self.subTest(pys = pys, mys = mys):
                for i in range(len(mys)):
                    self.assertEqual(mys[i], pys[i])
                # Test that the index is of a valid type and within range.
                with self.assertRaises(TypeError):
                    c = mys['a']
                with self.assertRaises(IndexError):
                    c = mys[-1]
                with self.assertRaises(IndexError):
                    c = mys[len(mys) + 1]

    def test_iter(self):
        for pys, mys in zip(self.pystrings, self.mystrings):
            with self.subTest(pys = pys, mys = mys):
                for myc, pyc in zip(mys, pys):
                    self.assertEqual(myc, pyc)


if  __name__ == '__main__':
    unittest.main()
