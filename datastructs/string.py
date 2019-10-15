class String():

    def __init__(self, data):
        if not isinstance(data, str):
            raise TypeError("string instances must be strings.")
        self.length = len(data)
        self.data = [x for x in data]

    def __len__(self):
        return self.length

    def __str__(self):
        return ''.join(self.data)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("string indices must be integers.")
        if key < 0 or key >= self.length:
            raise IndexError("string index out of range.")
        return self.data[key]

    def __iter__(self):
        for i in range(self.length):
            yield self.data[i]
