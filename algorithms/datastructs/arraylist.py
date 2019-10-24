from . import Array


class ArrayList(Array):
    DEFAULT_INTERNAL_LENGTH = 10
    GROWTH_FACTOR = 2

    def __init__(self, dtype, length=0):
        if not isinstance(length, int):
            raise TypeError("Length must be of type `int`.")
        if length < 0:
            raise ValueError('Length must be non-negative.')
        if not isinstance(dtype, type):
            raise TypeError('Dtype must be of type `type`.')
        self.dtype = dtype
        internal_length = self.DEFAULT_INTERNAL_LENGTH
        while internal_length < length:
            internal_length *= self.GROWTH_FACTOR
        self.data = [self.dtype() for _ in range(internal_length)]
        self.length = length

    def __len__(self):
        return self.length

    def __str__(self):
        if self.dtype == str:
            s = [''.join(["'", str(self.data[i]), "'"]) for i in
                 range(self.length)]
        else:
            s = [str(self.data[i]) for i in range(self.length)]
        s = ', '.join(s)
        s = ''.join(['[', s, ']'])
        return s

    # Inherit Array.__getitem__

    # Inherit Array.__setitem__

    def append(self, val):
        if not isinstance(val, self.dtype):
            raise TypeError(f"Array values must be of type {self.dtype}.")
        if self.length == len(self.data):
            data2 = [self.dtype()
                     for _ in range(len(self.data)*self.GROWTH_FACTOR)]
            for i in range(self.length):
                data2[i] = self.data[i]
            self.data = data2
        self.data[self.length] = val
        self.length += 1

    def extend(self, arr):
        for i in range(len(arr)):
            if not isinstance(arr[i], self.dtype):
                raise TypeError(f"Array values must be of type {self.dtype}.")
        if self.length + len(arr) > len(self.data):
            internal_length = len(self.data)
            while internal_length < self.length + len(arr):
                internal_length *= self.GROWTH_FACTOR
            data2 = [self.dtype() for _ in range(internal_length)]
            for i in range(self.length):
                data2[i] = self.data[i]
            self.data = data2
        for i in range(len(arr)):
            self.data[self.length + i] = arr[i]
        self.length += len(arr)

    def pop(self):
        if not self.length:
            raise IndexError('Pop from empty list.')
        val = self.data[self.length - 1]
        self.data[self.length - 1] = self.dtype()
        self.length -= 1
        return val
