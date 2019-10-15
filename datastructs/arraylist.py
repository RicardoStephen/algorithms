from datastructs.array import Array


class ArrayList(Array):
    DEFAULT_INTERNAL_LENGTH = 10
    GROWTH_FACTOR = 2

    def __init__(self, dtype, length=0):
        self.dtype = dtype
        internal_length = self.DEFAULT_INTERNAL_LENGTH
        while internal_length < length:
            internal_length *= self.GROWTH_FACTOR
        self.data = Array(self.dtype, internal_length)
        self.length = length

    def __len__(self):
        return self.length

    def __str__(self):
        if self.dtype == str:
            s = [''.join(["'", str(self.data[i]), "'"]) for i in range(self.length)]
        else:
            s = [str(self.data[i]) for i in range(self.length)]
        s = ', '.join(s)
        s = ''.join(['[', s, ']'])
        return s

    ############################################################################
    # Inherit Array.__getitem__, __setitem__, __iter__
    ############################################################################

    ############################################################################
    # Resizing methods
    ############################################################################

    def append(self, val):
        if not isinstance(val, self.dtype):
            raise TypeError(f"array values must be of type {self.dtype}.")
        if self.length == len(self.data):
            data2 = Array(self.dtype,
                          len(self.data) * self.GROWTH_FACTOR)
            for i in range(self.length):
                data2[i] = self.data[i]
            self.data = data2
        self.data[self.length] = val
        self.length += 1

    def extend(self, arr):
        for x in arr:
            if not isinstance(x, self.dtype):
                raise TypeError(f"array values must be of type {self.dtype}.")
        if len(arr) + self.length > len(self.data):
            internal_length = len(self.data) * self.GROWTH_FACTOR
            while internal_length < len(arr) + self.length:
                internal_length *= self.GROWTH_FACTOR
            data2 = Array(self.dtype, internal_length)
            for i in range(self.length):
                data2[i] = self.data[i]
            self.data = data2
        for i in range(len(arr)):
            self.data[self.length + i] = arr[i]
        self.length += len(arr)

    def pop(self):
        if self.length == 0:
            raise IndexError('pop from empty list.')
        ret = self.data[self.length - 1]
        self.data[self.length - 1] = self.dtype()
        self.length -= 1
        return ret
