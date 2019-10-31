from algorithms.baseobject import BaseObject


class Array(BaseObject):

    def __init__(self, dtype, length=0):
        if not isinstance(dtype, type):
            raise TypeError('Dtype must be of type `type`.')
        if not isinstance(length, int):
            raise TypeError("Length must be of type `int`.")
        if length < 0:
            raise ValueError('Length must be non-negative.')
        self.length = length
        self.dtype = dtype
        self.data = [self.dtype() for _ in range(self.length)]

    def __len__(self):
        return self.length

    def __str__(self):
        if self.dtype == str:
            s = [''.join(["'", str(c), "'"]) for c in self.data]
        else:
            s = list(map(str, self.data))
        s = ', '.join(s)
        s = ''.join(['[', s, ']'])
        return s

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Index must be of type `int`.")
        if key < 0 or key >= self.length:
            raise IndexError("Index out of range.")
        return self.data[key]

    def __setitem__(self, key, val):
        if not isinstance(key, int):
            raise TypeError("Index must be of type `int`.")
        if key < 0 or key >= self.length:
            raise IndexError("Index out of range.")
        if not isinstance(val, self.dtype):
            raise TypeError(f"Array values must be of type {self.dtype}.")
        self.data[key] = val
