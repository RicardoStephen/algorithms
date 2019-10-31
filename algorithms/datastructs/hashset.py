from collections import deque

from algorithms.baseobject import BaseObject


class HashSet(BaseObject):
    DEFAULT_NUM_BUCKETS = 10
    GROWTH_FACTOR = 2
    LOAD_FACTOR = 0.7

    def __init__(self):
        self.buckets = [deque() for _ in range(self.DEFAULT_NUM_BUCKETS)]
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.length == 0:
            return "set()"
        s = []
        for bucket in self.buckets:
            for elem in bucket:
                if isinstance(elem, str):
                    s.append(''.join(["'", str(elem), "'"]))
                else:
                    s.append(str(elem))
        s = ', '.join(s)
        s = ''.join(['{', s, '}'])
        return s

    def add(self, elem):
        idx = hash(elem) % len(self.buckets)
        if elem in self.buckets[idx]:
            return
        if (self.length + 1) / len(self.buckets) > self.LOAD_FACTOR:
            buckets2 = [deque() for _ in range(len(self.buckets) *
                                               self.GROWTH_FACTOR)]
            for old_bucket in self.buckets:
                for elem2 in old_bucket:
                    idx = hash(elem2) % len(buckets2)
                    buckets2[idx].append(elem2)
            self.buckets = buckets2
            idx = hash(elem) % len(self.buckets)
        self.buckets[idx].append(elem)
        self.length += 1

    def remove(self, elem):
        idx = hash(elem) % len(self.buckets)
        try:
            self.buckets[idx].remove(elem)
        except ValueError:
            raise KeyError(elem)
        self.length -= 1

    def __contains__(self, elem):
        idx = hash(elem) % len(self.buckets)
        return elem in self.buckets[idx]
