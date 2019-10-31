import unittest
import math

from test import Utils
from algorithms.datastructs import HashSet


class TestHashSet(unittest.TestCase):
    """
    Test datastructs.HashSet by creating identical hashsets using python's set
    class and datastructs' HashSet class, and then testing that identical
    operations on each yield equivalent results.
    """

    def setUp(self):
        self.intgen = Utils.int_generator()
        self.strgen = Utils.str_generator()

        states = ['empty', 'one', 'two', 'three',
                  'capacity', 'resize', 'resize+3',
                  'capacity2', 'resize2', 'resize2+3']
        self.pysets = dict(zip(states, [set() for _ in states]))
        self.mysets = dict(zip(states, [HashSet() for _ in states]))
        self.add_elems(self.mysets['one'], self.pysets['one'])
        self.add_elems(self.mysets['two'], self.pysets['two'], 2)
        self.add_elems(self.mysets['three'], self.pysets['three'], 3)
        self.add_until_capacity(self.mysets['capacity'], self.pysets['capacity'])
        self.add_until_resize(self.mysets['resize'], self.pysets['resize'])
        self.add_until_resize(self.mysets['resize+3'], self.pysets['resize+3'])
        self.add_elems(self.mysets['resize+3'], self.pysets['resize+3'], 3)
        self.add_until_resize(self.mysets['capacity2'], self.pysets['capacity2'])
        self.add_until_capacity(self.mysets['capacity2'], self.pysets['capacity2'])
        self.add_until_resize(self.mysets['resize2'], self.pysets['resize2'])
        self.add_until_resize(self.mysets['resize2'], self.pysets['resize2'])
        self.add_until_resize(self.mysets['resize2+3'], self.pysets['resize2+3'])
        self.add_until_resize(self.mysets['resize2+3'], self.pysets['resize2+3'])
        self.add_elems(self.mysets['resize2+3'], self.pysets['resize2+3'], 3)

    def check_equal(self, myset, pyset):
        self.assertEqual(len(myset), len(pyset))
        for elem in pyset:
            self.assertIn(elem, myset)
        self.check_str_equal(myset, pyset)

    def check_str_equal(self, myset, pyset):
        if not myset:
            self.assertEqual(str(myset), str(pyset))
            return
        myelems = set(str(myset)[1:-1].split(', '))
        pyelems = set(str(pyset)[1:-1].split(', '))
        self.assertEqual(myelems, pyelems)

    def add_elems(self, myset, pyset, count=1):
        for i in range(count // 2):
            elem = next(self.strgen)
            myset.add(elem)
            pyset.add(elem)
            self.check_equal(myset, pyset)
            elem = next(self.intgen)
            myset.add(elem)
            pyset.add(elem)
            self.check_equal(myset, pyset)
        if count % 2:
            elem = next(self.strgen)
            myset.add(elem)
            pyset.add(elem)
            self.check_equal(myset, pyset)

    def add_until_capacity(self, myset, pyset):
        capacity = math.floor(HashSet.LOAD_FACTOR*len(myset.buckets))
        bucket_count = len(myset.buckets)
        for _ in range(capacity - len(myset)):
            elem = next(self.intgen)
            myset.add(elem)
            pyset.add(elem)
        self.check_equal(myset, pyset)
        self.assertEqual(bucket_count, len(myset.buckets))

    def add_until_resize(self, myset, pyset):
        self.add_until_capacity(myset, pyset)
        old_bucket_count = len(myset.buckets)
        elem = next(self.strgen)
        myset.add(elem)
        pyset.add(elem)
        self.check_equal(myset, pyset)
        self.assertEqual(len(myset.buckets),
                         old_bucket_count * HashSet.GROWTH_FACTOR)

    def test_init(self):
        pass

    def test_len(self):
        for pyset, myset in zip(self.pysets.values(), self.mysets.values()):
            with self.subTest(pyset = pyset, myset = myset):
                self.assertEqual(len(myset), len(pyset))

    def test_str(self):
        for pyset, myset in zip(self.pysets.values(), self.mysets.values()):
            with self.subTest(pyset = pyset, myset = myset):
                self.check_str_equal(myset, pyset)

    def test_add(self):
        for pyset, myset in zip(self.pysets.values(), self.mysets.values()):
            with self.subTest(pyset = pyset, myset = myset):
                self.add_elems(myset, pyset, 3)

    def test_add_duplicate(self):
        for pyset, myset in zip(self.pysets.values(), self.mysets.values()):
            with self.subTest(pyset = pyset, myset = myset):
                pyset_copy = pyset.copy()
                for elem in pyset_copy:
                    myset.add(elem)
                    pyset.add(elem)
                    self.check_equal(myset, pyset)

    def test_add_capacity(self):
        for pyset, myset in zip(self.pysets.values(), self.mysets.values()):
            with self.subTest(pyset = pyset, myset = myset):
                self.add_until_capacity(myset, pyset)

    def test_add_resize(self):
        for pyset, myset in zip(self.pysets.values(), self.mysets.values()):
            with self.subTest(pyset = pyset, myset = myset):
                self.add_until_resize(myset, pyset)

    def test_remove(self):
        for pyset, myset in zip(self.pysets.values(), self.mysets.values()):
            with self.subTest(pyset = pyset, myset = myset):
                pyset_copy = pyset.copy()
                for elem in pyset_copy:
                    myset.remove(elem)
                    pyset.remove(elem)
                    self.check_equal(myset, pyset)

    def test_remove_notin(self):
        for pyset, myset in zip(self.pysets.values(), self.mysets.values()):
            with self.subTest(pyset = pyset, myset = myset):
                with self.assertRaises(KeyError):
                    myset.remove(next(self.intgen))
                with self.assertRaises(KeyError):
                    myset.remove(next(self.strgen))

    def test_contains(self):
        for pyset, myset in zip(self.pysets.values(), self.mysets.values()):
            with self.subTest(pyset = pyset, myset = myset):
                for elem in pyset:
                    self.assertIn(elem, myset)

    def test_contains_false(self):
        for pyset, myset in zip(self.pysets.values(), self.mysets.values()):
            with self.subTest(pyset = pyset, myset = myset):
                self.assertNotIn(next(self.intgen), myset)
                self.assertNotIn(next(self.strgen), myset)


if __name__ == '__main__':
    unittest.main()
