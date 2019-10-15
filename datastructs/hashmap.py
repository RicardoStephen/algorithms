from datastructs.array import Array
from datastructs.linkedlist import LinkedList


class HashMap:
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

    ############################################################################
    # Keyed access
    ############################################################################
    def __getitem__(self, key):
        bucket_idx = hash(key) % len(self.buckets)
        for (key2, val) in self.buckets[bucket_idx]:
            if key == key2:
                return val
        raise KeyError(key)

    def __setitem__(self, key, val):
        try:
            del self[key]
        except KeyError:
            pass
        if (self.length + 1) / len(self.buckets) > self.LOAD_FACTOR:
            buckets2 = Array(LinkedList, len(self.buckets) * self.GROWTH_FACTOR)
            self.buckets, buckets2 = buckets2, self.buckets
            self.length = 0
            for bucket in buckets2:
                for (key2, val2) in bucket:
                    self[key2] = val2
        bucket_idx = hash(key) % len(self.buckets)
        self.buckets[bucket_idx].appendleft((key, val))
        self.length += 1

    def __delitem__(self, key):
        val = self[key]
        bucket_idx = hash(key) % len(self.buckets)
        self.buckets[bucket_idx].remove((key, val))
        self.length -= 1
