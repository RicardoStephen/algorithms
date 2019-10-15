from datastructs.array import Array
from datastructs.linkedlist import LinkedList


class HashSet:
    DEFAULT_INTERNAL_LENGTH = 10
    GROWTH_FACTOR = 2
    LOAD_FACTOR = 0.7

    def __init__(self):
        self.buckets = Array(LinkedList, self.DEFAULT_INTERNAL_LENGTH)
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
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

    ############################################################################
    # Membership management
    ############################################################################
    def add(self, elem):
        if elem in self:
            return
        if (self.length + 1) / len(self.buckets) > self.LOAD_FACTOR:
            buckets2 = Array(LinkedList, len(self.buckets) * self.GROWTH_FACTOR)
            self.buckets, buckets2 = buckets2, self.buckets
            self.length = 0
            for bucket in buckets2:
                for elem2 in bucket:
                    self.add(elem2)
        bucket_idx = hash(elem) % len(self.buckets)
        self.buckets[bucket_idx].appendleft(elem)
        self.length += 1

    def remove(self, elem):
        bucket_idx = hash(elem) % len(self.buckets)
        try:
            self.buckets[bucket_idx].remove(elem)
        except ValueError:
            raise KeyError(elem)
        self.length -= 1

    def __contains__(self, elem):
        bucket_idx = hash(elem) % len(self.buckets)
        for elem2 in self.buckets[bucket_idx]:
            if elem == elem2:
                return True
        return False
