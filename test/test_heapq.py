import unittest
import math

from algorithms.graphs import Heapq


class TestHeapq(unittest.TestCase):
    """
    Note, the heappush tests are only smoke tests.
    """

    def setUp(self):
        self.heaps = {'empty': []}
        states = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
        for idx, state in enumerate(states):
            self.heaps['int_' + state] = list(reversed(range(idx + 1)))
            self.heaps['str_' + state] = list(reversed('bcdefgh'[:idx+1]))
        self.small_int, self.large_int = -1, 7
        self.small_str, self.large_str = 'a', 'i'
        for heap in self.heaps.values():
            Heapq.heapify(heap)
            self.check_heaporder(heap)

    def check_heaporder(self, arr):
        for idx in range(len(arr) - 1, 0, -1):
            pidx = (idx - 1) // 2
            self.assertLessEqual(arr[pidx], arr[idx])

    def test_heapify(self):
        pass

    def test_heappush_small(self):
        for state, heap in self.heaps.items():
            with self.subTest(heap = heap):
                # Push 1 layer of small elements.
                elem = self.small_int if state[:3] == 'int' else self.small_str
                height = math.ceil(math.log(len(heap) + 1, 2))
                missing_leaves = (2**height - 1) - len(heap)
                next_layer = 2**height
                for _ in range(missing_leaves + next_layer):
                    Heapq.heappush(heap, elem)
                    self.check_heaporder(heap)

    def test_heappush_large(self):
        for state, heap in self.heaps.items():
            with self.subTest(heap = heap):
                # Push 1 layer of large elements.
                elem = self.large_int if state[:3] == 'int' else self.large_str
                height = math.ceil(math.log(len(heap) + 1, 2))
                missing_leaves = (2**height - 1) - len(heap)
                next_layer = 2**height
                for _ in range(missing_leaves + next_layer):
                    Heapq.heappush(heap, elem)
                    self.check_heaporder(heap)

    def test_heappop(self):
        for heap in self.heaps.values():
            with self.subTest(heap = heap):
                for _ in range(len(heap)):
                    val = heap[0]
                    self.assertEqual(Heapq.heappop(heap), val)
                    self.check_heaporder(heap)

    def test_heappop_invalid(self):
        for heap in self.heaps.values():
            with self.subTest(heap = heap):
                for _ in range(len(heap)):
                    val = heap[0]
                    self.assertEqual(Heapq.heappop(heap), val)
                    self.check_heaporder(heap)
                with self.assertRaises(IndexError):
                    val = Heapq.heappop(heap)
