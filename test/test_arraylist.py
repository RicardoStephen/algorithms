from test import Utils
from test.test_array import TestArray
from algorithms.datastructs import ArrayList


class TestArrayList(TestArray):

    def setUp(self):
        self.intgen = Utils.int_generator()
        self.strgen = Utils.str_generator()

        self.pyarrs = {
            'emptyi': [],
            'onei': [0], 'twoi': [0]*2, 'threei': [0]*3, '10i': [0]*10,
            'emptys': [],
            'ones': [''], 'twos': ['']*2, 'threes': ['']*3, '10s': ['']*10,
            'capacityi': [0] * ArrayList.DEFAULT_INTERNAL_LENGTH,
            'resizei': [0] * (ArrayList.DEFAULT_INTERNAL_LENGTH + 1),
            'resize+3i': [0] * (ArrayList.DEFAULT_INTERNAL_LENGTH + 4),
            'capacity2i': [0] * ArrayList.DEFAULT_INTERNAL_LENGTH * 2,
            'resize2i': [0] * (ArrayList.DEFAULT_INTERNAL_LENGTH * 2 + 1),
            'resize2+3i': [0] * (ArrayList.DEFAULT_INTERNAL_LENGTH * 2 + 4),
            'capacitys': [''] * ArrayList.DEFAULT_INTERNAL_LENGTH,
            'resizes': [''] * (ArrayList.DEFAULT_INTERNAL_LENGTH + 1),
            'resize+3s': [''] * (ArrayList.DEFAULT_INTERNAL_LENGTH + 4),
            'capacity2s': [''] * ArrayList.DEFAULT_INTERNAL_LENGTH * 2,
            'resize2s': [''] * (ArrayList.DEFAULT_INTERNAL_LENGTH * 2 + 1),
            'resize2+3s': [''] * (ArrayList.DEFAULT_INTERNAL_LENGTH * 2 + 4),
        }
        self.myarrs = dict()
        for state, arr in self.pyarrs.items():
            if state[-1] == 'i':
                self.myarrs[state] = ArrayList(int, len(arr))
            else:
                self.myarrs[state] = ArrayList(str, len(arr))

    # Inherit check_equal

    # Inherit test_init_invalid, test_len, test_str

    # Inherit test_getitem, test_getitem2, test_getitem_invalid

    # Inherit test_setitem, test_setitem_invalid

    def test_append(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                generator = self.intgen if myarr.dtype == int else self.strgen
                val = next(generator)
                myarr.append(val)
                pyarr.append(val)
                self.check_equal(myarr, pyarr)
                val = next(generator)
                myarr.append(val)
                pyarr.append(val)
                self.check_equal(myarr, pyarr)
                val = next(generator)
                myarr.append(val)
                pyarr.append(val)
                self.check_equal(myarr, pyarr)

    def test_append_capacity(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                capacity = len(myarr.data)
                for i in range(capacity - len(myarr)):
                    if myarr.dtype == int:
                        val = next(self.intgen)
                    else:
                        val = next(self.strgen)
                    myarr.append(val)
                    pyarr.append(val)
                self.check_equal(myarr, pyarr)
                self.assertEqual(len(myarr.data), capacity)

    def test_append_resize(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                old_capacity = len(myarr.data)
                for i in range(len(myarr.data) - len(myarr) + 1):
                    if myarr.dtype == int:
                        val = next(self.intgen)
                    else:
                        val = next(self.strgen)
                    myarr.append(val)
                    pyarr.append(val)
                self.check_equal(myarr, pyarr)
                self.assertEqual(len(myarr.data),
                                 old_capacity * ArrayList.GROWTH_FACTOR)

    def test_append_invalid(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                with self.assertRaises(TypeError):
                    if myarr.dtype == int:
                        myarr.append(str())
                    else:
                        myarr.append(int())

    def test_extend(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                generator = self.intgen if myarr.dtype == int else self.strgen
                extension = [next(generator)]
                myarr.extend(extension)
                pyarr.extend(extension)
                self.check_equal(myarr, pyarr)
                extension = [next(generator) for _ in range(2)]
                myarr.extend(extension)
                pyarr.extend(extension)
                self.check_equal(myarr, pyarr)
                extension = [next(generator) for _ in range(3)]
                myarr.extend(extension)
                pyarr.extend(extension)
                self.check_equal(myarr, pyarr)

    def test_extend_empty(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                myarr.extend([])
                pyarr.extend([])
                self.check_equal(myarr, pyarr)

    def test_extend_capacity(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                capacity = len(myarr.data)
                if myarr.dtype == int:
                    extension = [next(self.intgen)
                                 for _ in range(capacity - len(myarr))]
                else:
                    extension = [next(self.strgen)
                                 for _ in range(capacity - len(myarr))]
                myarr.extend(extension)
                pyarr.extend(extension)
                self.check_equal(myarr, pyarr)
                self.assertEqual(len(myarr.data), capacity)

    def test_extend_resize(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                capacity = len(myarr.data)
                if myarr.dtype == int:
                    extension = [next(self.intgen)
                                 for _ in range(capacity - len(myarr) + 1)]
                else:
                    extension = [next(self.strgen)
                                 for _ in range(capacity - len(myarr) + 1)]
                myarr.extend(extension)
                pyarr.extend(extension)
                self.check_equal(myarr, pyarr)
                self.assertEqual(len(myarr.data),
                                 capacity * ArrayList.GROWTH_FACTOR)

    def test_extend_invalid(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                with self.assertRaises(TypeError):
                    if myarr.dtype == int:
                        myarr.extend([str()])
                    else:
                        myarr.extend([int()])

    def test_pop(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                for i in range(len(pyarr)):
                    self.assertEqual(myarr.pop(), pyarr.pop())
                    self.check_equal(myarr, pyarr)

    def test_pop_invalid(self):
        for pyarr, myarr in zip(self.pyarrs.values(), self.myarrs.values()):
            with self.subTest(pyarr = pyarr, myarr = myarr):
                for i in range(len(pyarr)):
                    self.assertEqual(myarr.pop(), pyarr.pop())
                    self.check_equal(myarr, pyarr)
                with self.assertRaises(IndexError):
                    myarr.pop()


if  __name__ == '__main__':
    unittest.main()
