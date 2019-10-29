import unittest
import math

from test import Utils
from algorithms.datastructs import HashMap


class TestHashMap(unittest.TestCase):
    """
    Test datastructs.HashMap by creating identical hashmaps using python's dict
    class and datastructs' HashMap class, and then testing that identical
    operations on each yield equivalent results.
    """

    def setUp(self):
        self.intgen = Utils.int_generator()
        self.strgen = Utils.str_generator()

        states = ['empty', 'one', 'two', 'three',
                  'capacity', 'resize', 'resize+3',
                  'capacity2', 'resize2', 'resize2+3']
        self.pydicts = dict(zip(states, [dict() for _ in states]))
        self.mydicts = dict(zip(states, [HashMap() for _ in states]))
        self.add_items(self.mydicts['one'], self.pydicts['one'])
        self.add_items(self.mydicts['two'], self.pydicts['two'], 2)
        self.add_items(self.mydicts['three'], self.pydicts['three'], 3)
        self.add_until_capacity(self.mydicts['capacity'], self.pydicts['capacity'])
        self.add_until_resize(self.mydicts['resize'], self.pydicts['resize'])
        self.add_until_resize(self.mydicts['resize+3'], self.pydicts['resize+3'])
        self.add_items(self.mydicts['resize+3'], self.pydicts['resize+3'], 3)
        self.add_until_resize(self.mydicts['capacity2'], self.pydicts['capacity2'])
        self.add_until_capacity(self.mydicts['capacity2'], self.pydicts['capacity2'])
        self.add_until_resize(self.mydicts['resize2'], self.pydicts['resize2'])
        self.add_until_resize(self.mydicts['resize2'], self.pydicts['resize2'])
        self.add_until_resize(self.mydicts['resize2+3'], self.pydicts['resize2+3'])
        self.add_until_resize(self.mydicts['resize2+3'], self.pydicts['resize2+3'])
        self.add_items(self.mydicts['resize2+3'], self.pydicts['resize2+3'], 3)

    def check_equal(self, mydict, pydict):
        self.assertEqual(len(mydict), len(pydict))
        for key, val in pydict.items():
            self.assertEqual(mydict[key], val)
        self.check_str_equal(mydict, pydict)

    def check_str_equal(self, mydict, pydict):
        myelems = set(str(mydict)[1:-1].split(', '))
        pyelems = set(str(pydict)[1:-1].split(', '))
        self.assertEqual(myelems, pyelems)

    def add_items(self, mydict, pydict, count=1):
        for i in range(count // 2):
            key, val = next(self.strgen), next(self.intgen)
            mydict[key] = val
            pydict[key] = val
            self.check_equal(mydict, pydict)
            key, val = next(self.intgen), next(self.strgen)
            mydict[key] = val
            pydict[key] = val
            self.check_equal(mydict, pydict)
        if count % 2:
            key, val = next(self.strgen), next(self.intgen)
            mydict[key] = val
            pydict[key] = val
            self.check_equal(mydict, pydict)

    def add_until_capacity(self, mydict, pydict):
        capacity = math.floor(HashMap.LOAD_FACTOR*len(mydict.buckets))
        bucket_count = len(mydict.buckets)
        for _ in range(capacity - len(mydict)):
            key, val = next(self.intgen), next(self.strgen)
            mydict[key] = val
            pydict[key] = val
        self.check_equal(mydict, pydict)
        self.assertEqual(bucket_count, len(mydict.buckets))

    def add_until_resize(self, mydict, pydict):
        self.add_until_capacity(mydict, pydict)
        old_bucket_count = len(mydict.buckets)
        key, val = next(self.strgen), next(self.intgen)
        mydict[key] = val
        pydict[key] = val
        self.check_equal(mydict, pydict)
        self.assertEqual(len(mydict.buckets),
                         old_bucket_count * HashMap.GROWTH_FACTOR)

    def test_len(self):
        for pydict, mydict in zip(self.pydicts.values(), self.mydicts.values()):
            with self.subTest(pydict = pydict, mydict = mydict):
                self.assertEqual(len(mydict), len(pydict))

    def test_str(self):
        for pydict, mydict in zip(self.pydicts.values(), self.mydicts.values()):
            with self.subTest(pydict = pydict, mydict = mydict):
                self.check_str_equal(mydict, pydict)

    def test_getitem(self):
        for pydict, mydict in zip(self.pydicts.values(), self.mydicts.values()):
            with self.subTest(pydict = pydict, mydict = mydict):
                for key, val in pydict.items():
                    self.assertEqual(mydict[key], val)

    def test_getitem_invalid(self):
        for pydict, mydict in zip(self.pydicts.values(), self.mydicts.values()):
            with self.subTest(pydict = pydict, mydict = mydict):
                with self.assertRaises(KeyError):
                    mydict[next(self.intgen)]

    def test_setitem_create(self):
        for pydict, mydict in zip(self.pydicts.values(), self.mydicts.values()):
            with self.subTest(pydict = pydict, mydict = mydict):
                self.add_items(mydict, pydict, 3)

    def test_setitem_create_capacity(self):
        for pydict, mydict in zip(self.pydicts.values(), self.mydicts.values()):
            with self.subTest(pydict = pydict, mydict = mydict):
                self.add_until_capacity(mydict, pydict)

    def test_setitem_create_resize(self):
        for pydict, mydict in zip(self.pydicts.values(), self.mydicts.values()):
            with self.subTest(pydict = pydict, mydict = mydict):
                self.add_until_resize(mydict, pydict)

    def test_setitem_update(self):
        for pydict, mydict in zip(self.pydicts.values(), self.mydicts.values()):
            with self.subTest(pydict = pydict, mydict = mydict):
                pydict_copy = pydict.copy()
                for key in pydict_copy:
                    val = next(self.strgen)
                    mydict[key] = val
                    pydict[key] = val
                    self.check_equal(mydict, pydict)
