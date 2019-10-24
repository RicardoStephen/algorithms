class Sorts:

    def __init__(self):
        pass

    def insertion_sort(self, arr):
        for idx in range(len(arr)):
            for swap_idx in range(idx-1, -1, -1):
                if arr[swap_idx] > arr[swap_idx+1]:
                    arr[swap_idx], arr[swap_idx+1] = (arr[swap_idx+1],
                                                      arr[swap_idx])
                else:
                    break

    def bubble_sort(self, arr):
        for bubble_len in range(len(arr)-1, 0, -1):
            for bubble_idx in range(bubble_len):
                if arr[bubble_idx] > arr[bubble_idx+1]:
                    arr[bubble_idx], arr[bubble_idx+1] = (arr[bubble_idx+1],
                                                          arr[bubble_idx])

    def selection_sort(self, arr):
        for search_root in range(len(arr)-1):
            min_idx = search_root
            for idx in range(search_root+1, len(arr)):
                if arr[idx] < arr[min_idx]:
                    min_idx = idx
            arr[search_root], arr[min_idx] = (arr[min_idx], arr[search_root])

    # https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
    # Hoare partition scheme with the median of the first, middle, and last as
    # the pivot.
    def quicksort(self, arr):
        def partition(arr, lo, hi):
            # Pick a pivot value.
            pivot = sorted([arr[lo], arr[(lo+hi)//2], arr[hi]])[1]
            # Parition the array about the pivot value.
            while True:
                while arr[lo] < pivot:
                    lo += 1
                while arr[hi] > pivot:
                    hi -= 1
                if lo >= hi:
                    return hi
                arr[lo], arr[hi] = arr[hi], arr[lo]
                lo += 1
                hi -= 1
        def quicksortRec(arr, lo, hi):
            if lo < hi: # Avoid the base case lo == hi.
                p = partition(arr, lo, hi)
                quicksortRec(arr, lo, p)
                quicksortRec(arr, p+1, hi)
        quicksortRec(arr, 0, len(arr)-1)

    # http://www.cs.cornell.edu/courses/cs2112/2015fa/lectures/lecture.html?id=sorting
    def mergesort(self, arr):
        def merge(arr, l, m, r, tmp):
            # arr: [l  |i  m |j    ]r
            # tmp: [l    |k        ]
            i, j = l, m
            k = l
            while i < m and j < r:
                tmp[k] = min(arr[i], arr[j])
                k += 1
                if arr[i] < arr[j]:
                    i += 1
                else:
                    j += 1
            for off in range(m-i):
                tmp[k+off] = arr[i+off]
            for idx in range(l, j):
                arr[idx] = tmp[idx]
        def sort(arr, l, r, tmp):
            if r - l < 2: # base case
                return
            m = (l + r) // 2
            sort(arr, l, m, tmp)
            sort(arr, m, r, tmp)
            merge(arr, l, m, r, tmp)
        tmp = [0]*len(arr)
        sort(arr, 0, len(arr), tmp)


if __name__ == '__main__':
    cases = [[],
             [1],
             [1, 2],
             [2, 1],
             [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1],
             [1, 1, 3], [1, 3, 1], [3, 1, 1],
             [1, 3, 3], [3, 1, 3], [3, 3, 1],
             [1, 1, 1],

             [5, 3, 7, 1], [3, 1, 5, 7], [1, 5, 3, 7], [5, 1, 7, 3],
             [5, 4, 3, 6, 1, 2, 3]]
    solutions = [sorted(case) for case in cases]
    sorts = Sorts()

    print('Insertion sort')
    for case, solution in zip(cases, solutions):
        case = case.copy()
        sorts.insertion_sort(case)
        assert(case == solution)

    print('Bubble sort')
    for case, solution in zip(cases, solutions):
        case = case.copy()
        sorts.bubble_sort(case)
        assert(case == solution)

    print('Selection sort')
    for case, solution in zip(cases, solutions):
        case = case.copy()
        sorts.selection_sort(case)
        assert(case == solution)
    
    print('Quicksort')
    for case, solution in zip(cases, solutions):
        case = case.copy()
        sorts.quicksort(case)
        assert(case == solution)

    print('Mergesort')
    for case, solution in zip(cases, solutions):
        case = case.copy()
        sorts.mergesort(case)
        assert(case == solution)
