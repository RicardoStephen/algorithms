from collections import deque

from .baseobject import BaseObject


class HashMap(BaseObject):
    DEFAULT_NUM_BUCKETS = 10
    GROWTH_FACTOR = 2
    LOAD_FACTOR = 0.7

    def __init__(self):
        self.buckets = [deque() for _ in range(self.DEFAULT_NUM_BUCKETS)]
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        s = []
        for bucket in self.buckets:
            for (key, val) in bucket:
                if isinstance(key, str) and isinstance(val, str):
                    s.append("'" + str(key) + "': '" + str(val) + "'")
                elif isinstance(key, str):
                    s.append("'" + str(key) + "': " + str(val))
                elif isinstance(val, str):
                    s.append(str(key) + ": '" + str(val) + "'")
                else:
                    s.append(str(key) + ': ' + str(val))
        s = ', '.join(s)
        s = ''.join(['{', s, '}'])
        return s

    def __getitem__(self, key):
        idx = hash(key) % len(self.buckets)
        for (key2, val) in self.buckets[idx]:
            if key == key2:
                return val
        raise KeyError(key)

    def __setitem__(self, key, val):
        idx = hash(key) % len(self.buckets)
        # Handle case where the hashmap already has a mapping for the key.
        for (key2, val2) in self.buckets[idx]:
            if key2 == key:
                self.buckets[idx].remove((key2, val2))
                self.buckets[idx].append((key, val))
                return
        if (self.length + 1) / len(self.buckets) > self.LOAD_FACTOR:
            buckets2 = [deque() for _ in range(len(self.buckets)*
                                               self.GROWTH_FACTOR)]
            for old_bucket in self.buckets:
                for key2, val2 in old_bucket:
                    idx = hash(key2) % len(buckets2)
                    buckets2[idx].append((key2, val2))
            self.buckets = buckets2
            idx = hash(key) % len(self.buckets)
        self.buckets[idx].append((key, val))
        self.length += 1
