class Search:

    def linear_search(self, arr, val):
        for i in range(len(arr)):
            if arr[i] == val:
                return i
        return -1

    def binary_search(self, arr, val):
        l, r = 0, len(arr)
        while l != r:
            i = (l + r) // 2
            if arr[i] == val:
                return i
            elif arr[i] > val:
                r = i
            else:
                l = i + 1
        return -1


if __name__ == '__main__':
    search = Search()

    arr = [75, 25, 0, 40, 100, 50]
    arr_sorted = sorted(arr)
    print(arr)
    print(arr_sorted)
    print()

    linear = search.linear_search(arr, 40)
    binary = search.binary_search(arr_sorted, 40)
    print('linear 40: ', linear)
    print('binary 40: ', binary)
    assert(linear != -1 and arr[linear] == 40)
    assert(binary != -1 and arr_sorted[binary] == 40)
    print()

    arr_sorted = []
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [30]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [40]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [50]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [30, 50]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [30, 40]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [40, 50]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [30, 40, 50]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [30, 35, 40]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [40, 45, 50]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [20, 30, 40, 50, 60]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [20, 30, 35, 40]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [40, 50, 55, 60]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [20, 30, 40, 50]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
    arr_sorted = [35, 40, 55, 60]
    print(arr_sorted, search.binary_search(arr_sorted, 40))
