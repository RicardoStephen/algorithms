from .baseobject import BaseObject


class String(BaseObject):

    def __init__(self, data):
        if not isinstance(data, str):
            raise TypeError("String data must be a of type `str`.")
        self.length = len(data)
        self.data = [x for x in data]

    def __len__(self):
        return self.length

    def __str__(self):
        return ''.join(self.data)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Index must be of type `int`.")
        if key < 0 or key >= self.length:
            raise IndexError("Index out of range.")
        return self.data[key]
