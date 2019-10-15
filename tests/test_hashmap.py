import unittest

from datastructs.hashmap import HashMap


class TestHashMap(unittest.TestCase):
    """
    Test datastructs.HashMap by creating identical hashmaps using python's dict
    class and datastructs' HashMap class, and then testing that identical
    operations on each yield equivalent results.
    """

    def setUp(self):
        subtests = [[],
                    [(1, 'a')],
                    [(1, 'a'), (2, 5), (10, 'q')]]
        x = []
        for i in range(int(HashMap.DEFAULT_INTERNAL_LENGTH *
                           HashMap.LOAD_FACTOR) + 1):
            x.append((i, 2*i - 1))
        subtests.append(x)
        x = []
        for i in range(int(HashMap.DEFAULT_INTERNAL_LENGTH *
                           HashMap.LOAD_FACTOR * HashMap.GROWTH_FACTOR) + 1):
            x.append((i, -3*i - 1))
        subtests.append(x)

        self.pydicts = [dict(x) for x in subtests]
        self.mydicts = [HashMap() for x in subtests]
        for mydict, subtest in zip(self.mydicts, subtests):
            for key, val in subtest:
                mydict[key] = val
        self.extra_items = [[('r', 10)], [('m', -11), ('n', -12)],
                            [('x', '#'), ('y', 'y'), ('z', 'q')]]

    def test_len(self):
        for pydict, mydict in zip(self.pydicts, self.mydicts):
            with self.subTest(pydict = pydict, mydict = mydict):
                self.assertEqual(len(mydict), len(pydict))

    def test_str(self):
        pass

    def test_getitem(self):
        for pydict, mydict in zip(self.pydicts, self.mydicts):
            with self.subTest(pydict = pydict, mydict = mydict):
                for key, val in pydict.items():
                    self.assertEqual(mydict[key], val)

    def test_setitem_create(self):
        for pydict, mydict in zip(self.pydicts, self.mydicts):
            with self.subTest(pydict = pydict, mydict = mydict):
                pydict_copy = pydict.copy()
                # Test set 1, 2, 3 new items.
                def test_setitems(items):
                    for key, val in items:
                        mydict[key] = val
                        pydict[key] = val
                        self.assertEqual(len(mydict), len(pydict))
                        for key2, val2 in pydict.items():
                            self.assertEqual(mydict[key2], pydict[key2])
                for items in self.extra_items:
                    test_setitems(items)
                # Test set new items until resize.
                # Generate values not in the dict by finding the minimum int in
                # the dict, and then using numbers less than that.
                pydict_ints = list(filter(lambda x : isinstance(x, int),
                                          pydict.values()))
                pydict_ints.append(0)
                min_val = min(pydict_ints) - 1
                target_len = (HashMap.DEFAULT_INTERNAL_LENGTH *
                              HashMap.LOAD_FACTOR)
                while target_len <= len(mydict):
                    target_len *= HashMap.GROWTH_FACTOR
                num_more_items = (int(target_len) + 1) - len(mydict)
                more_items = []
                for i in range(num_more_items):
                    more_items.append((min_val - 2*i, min_val - (2*i +1)))
                test_setitems(more_items)
                # Test set new items until resize 2.
                target_len *= HashMap.GROWTH_FACTOR
                num_more_items_2 = (int(target_len) + 1) - len(mydict)
                more_items_2 = []
                for i in range(num_more_items,
                               num_more_items + num_more_items_2):
                    more_items_2.append((min_val + 2*i, min_val + (2*i - 1)))
                test_setitems(more_items_2)
                # Test del undo "set new items until resize 2".
                def test_delitems(items):
                    for key, val in items:
                        del mydict[key]
                        del pydict[key]
                        self.assertEqual(len(mydict), len(pydict))
                        for key2, val2 in pydict.items():
                            self.assertEqual(mydict[key2], pydict[key2])
                test_delitems(more_items_2)
                # Test del undo "set new items until resize".
                test_delitems(more_items)
                # Test del undo "set 1, 2, 3 new items".
                for items in self.extra_items:
                    test_delitems(items)
                    
    def test_setitem_update(self):
        for pydict, mydict in zip(self.pydicts, self.mydicts):
            with self.subTest(pydict = pydict, mydict = mydict):
                # Generate a values not in the dict by finding the minimum int in
                # the dict, and decreasing it by 1.
                pydict_copy = pydict.copy()
                pydict_ints = list(filter(lambda x : isinstance(x, int),
                                          pydict.values()))
                pydict_ints.append(0)
                replacement_val = min(pydict_ints) - 1
                for key, val in pydict.items():
                    mydict[key] = replacement_val
                    pydict[key] = replacement_val
                    for key2, val2 in pydict.items():
                        self.assertEqual(mydict[key2], pydict[key2])
                    mydict[key] = val
                    pydict[key] = val
                    for key2, val2 in pydict.items():
                        self.assertEqual(mydict[key2], pydict[key2])
                for key, val in pydict_copy.items():
                    self.assertEqual(mydict[key], val)
                    self.assertEqual(pydict[key], val)

    def test_delitem(self):
        for pydict, mydict in zip(self.pydicts, self.mydicts):
            with self.subTest(pydict = pydict, mydict = mydict):
                for key in pydict:
                    del mydict[key]
                    with self.assertRaises(KeyError):
                        x = mydict[key]
                for key, val in pydict.items():
                    mydict[key] = val
                for key, val in pydict.items():
                    self.assertEqual(mydict[key], val)


if __name__ == '__main__':
    unittest.main()
