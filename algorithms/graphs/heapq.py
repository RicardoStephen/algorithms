class Heapq:

    @classmethod
    def bubble_up(cls, arr, idx):
        pidx = (idx - 1) // 2
        if pidx >= 0 and arr[idx] < arr[pidx]:
            arr[idx], arr[pidx] = arr[pidx], arr[idx]
            cls.bubble_up(arr, pidx)

    @classmethod
    def bubble_down(cls, arr, idx):
        lidx = 2*idx + 1
        ridx = 2*idx + 2
        if lidx < len(arr):
            cidx = lidx
            if ridx < len(arr) and arr[ridx] < arr[cidx]:
                cidx = ridx
            if arr[cidx] < arr[idx]:
                arr[idx], arr[cidx] = arr[cidx], arr[idx]
                cls.bubble_down(arr, cidx)

    @classmethod
    def heapify(cls, arr):
        for i in range(len(arr) - 1, -1, -1):
            cls.bubble_down(arr, i)

    @classmethod
    def heappush(cls, arr, val):
        arr.append(val)
        cls.bubble_up(arr, len(arr) - 1)

    @classmethod
    def heappop(cls, arr):
        if not arr:
            raise IndexError("Pop from empty list.")
        head = arr[0]
        tail = arr.pop()
        if arr:
            arr[0] = tail
            cls.bubble_down(arr, 0)
        return head
