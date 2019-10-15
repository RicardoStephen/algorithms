import unittest

from datastructs.hashset import HashSet


class TestHashSet(unittest.TestCase):
    """
    Test datastructs.HashSet by creating identical hashsets using python's set
    class and datastructs' HashSet class, and then testing that identical
    operations on each yield equivalent results.
    """

    def setUp(self):
        subtests = [[],
                    [1],
                    [201, 'a', 'c']]
        x = []
        for i in range(int(HashSet.DEFAULT_INTERNAL_LENGTH *
                           HashSet.LOAD_FACTOR) + 1):
            x.append((i, 2*i - 1))
        subtests.append(x)
        x = []
        for i in range(int(HashSet.DEFAULT_INTERNAL_LENGTH *
                           HashSet.LOAD_FACTOR * HashSet.GROWTH_FACTOR) + 1):
            x.append((i, -3*i - 1))
        subtests.append(x)

        self.pysets = [set(x) for x in subtests]
        self.mysets = [HashSet() for x in subtests]
        for pyset, myset in zip(self.pysets, self.mysets):
            for elem in pyset:
                myset.add(elem)

    def test_len(self):
        for pyset, myset in zip(self.pysets, self.mysets):
            with self.subTest(pyset = pyset, myset = myset):
                self.assertEqual(len(myset), len(pyset))

    def test_str(self):
        pass

    def test_add_simple(self):
        for pyset, myset in zip(self.pysets, self.mysets):
            with self.subTest(pyset = pyset, myset = myset):
                for new_elem in [10001, 'zab', 'foo']:
                    myset.add(new_elem)
                    pyset.add(new_elem)
                    self.assertEqual(len(myset), len(pyset))
                    for elem in pyset:
                        self.assertIn(elem, myset)

    def test_add_unique(self):
        for pyset, myset in zip(self.pysets, self.mysets):
            with self.subTest(pyset = pyset, myset = myset):
                # Generate values not in the set by finding the minimum int in
                # the set, and then using numbers less than that.
                pyset_ints = list(filter(lambda x : isinstance(x, int), pyset))
                pyset_ints.append(0)
                pyset_new_val = min(pyset_ints) - 1
                notin_vals = [pyset_new_val- i for i in range(5)]
                for notin_val in notin_vals:
                    myset.add(notin_val)
                    pyset.add(notin_val)
                    self.assertEqual(len(myset), len(pyset))
                    for elem in pyset:
                        self.assertIn(elem, myset)
    
    def test_add_duplicate(self):
        for pyset, myset in zip(self.pysets, self.mysets):
            with self.subTest(pyset = pyset, myset = myset):
                for elem in pyset:
                    myset.add(elem)
                    self.assertEqual(len(myset), len(pyset))
                    for elem2 in pyset:
                        self.assertIn(elem2, myset)

    def test_add_resize(self):
        for pyset, myset in zip(self.pysets, self.mysets):
            with self.subTest(pyset = pyset, myset = myset):
                # Test add new elements until resize.
                # Generate values not in the set by finding the minimum int in
                # the set, and then using numbers less than that.
                pyset_ints = list(filter(lambda x : isinstance(x, int), pyset))
                pyset_ints.append(0)
                pyset_new_val = min(pyset_ints) - 1
                target_set_len = (HashSet.DEFAULT_INTERNAL_LENGTH *
                                 HashSet.LOAD_FACTOR)
                while target_set_len <= len(myset):
                    target_set_len *= HashSet.GROWTH_FACTOR
                num_new_elems = (int(target_set_len) + 1) - len(myset)
                def test_add_elems(elems):
                    for i in elems:
                        myset.add(i)
                        pyset.add(i)
                        self.assertEqual(len(myset), len(pyset))
                        for elem in pyset:
                            self.assertIn(elem, myset)
                test_add_elems(range(pyset_new_val,
                                     pyset_new_val - num_new_elems, -1))
                # Test add new elements until resize 2.
                target_set_len *= HashSet.GROWTH_FACTOR
                num_new_elems_2 = (int(target_set_len) + 1) - len(myset)
                test_add_elems(range(pyset_new_val - num_new_elems,
                                     pyset_new_val - num_new_elems_2, -1))

    def test_remove_simple(self):
        for pyset, myset in zip(self.pysets, self.mysets):
            with self.subTest(pyset = pyset, myset = myset):
                for elem in list(pyset):
                    myset.remove(elem)
                    pyset.remove(elem)
                    self.assertEqual(len(myset), len(pyset))
                    for elem2 in pyset:
                        self.assertIn(elem2, myset)

    def test_remove_notin(self):
        for pyset, myset in zip(self.pysets, self.mysets):
            with self.subTest(pyset = pyset, myset = myset):
                # Generate values not in the set by finding the minimum int in
                # the set, and then using numbers less than that.
                pyset_ints = list(filter(lambda x : isinstance(x, int), pyset))
                pyset_ints.append(0)
                pyset_new_val = min(pyset_ints) - 1
                with self.assertRaises(KeyError):
                    myset.remove(pyset_new_val)

    def test_contains_true(self):
        for pyset, myset in zip(self.pysets, self.mysets):
            with self.subTest(pyset = pyset, myset = myset):
                for elem in pyset:
                    self.assertIn(elem, myset)

    def test_contains_false(self):
        for pyset, myset in zip(self.pysets, self.mysets):
            with self.subTest(pyset = pyset, myset = myset):
                # Generate values not in the set by finding the minimum int in
                # the set, and then using numbers less than that.
                pyset_ints = list(filter(lambda x : isinstance(x, int), pyset))
                pyset_ints.append(0)
                pyset_new_val = min(pyset_ints) - 1
                self.assertNotIn(pyset_new_val, myset)


if __name__ == '__main__':
    unittest.main()
