class Array:

    def __init__(self, dtype, length=0):
        self.length = length
        self.dtype = dtype
        self.data = [self.dtype() for i in range(self.length)]

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
            raise TypeError("array indices must be integers.")
        if key < 0 or key >= self.length:
            raise IndexError("array index out of range.")
        return self.data[key]

    def __setitem__(self, key, val):
        if not isinstance(key, int):
            raise TypeError("array indices must be integers.")
        if key < 0 or key >= self.length:
            raise IndexError("array index out of range.")
        if not isinstance(val, self.dtype):
            raise TypeError(f"array values must be of type {self.dtype}.")
        self.data[key] = val

    def __iter__(self):
        for i in range(self.length):
            yield self.data[i]
