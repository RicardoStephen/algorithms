class Sort:

    def __init__(self):
        pass

    def selection_sort(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return
        left_wall = 0
        while left_wall < len(arr):
            min_idx = left_wall
            for i in range(left_wall + 1, len(arr)):
                if arr[i] < arr[min_idx]:
                    min_idx = i
            arr[left_wall], arr[min_idx] = arr[min_idx], arr[left_wall]
            left_wall += 1

    def bubble_sort(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return
        right_wall = len(arr) - 1
        while right_wall != 0:
            for i in range(right_wall):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            right_wall -= 1

    def insertion_sort(self, arr):
        if len(arr) == 0 or len(arr) == 1:
            return
        left_wall = 1
        while left_wall < len(arr):
            for i in range(left_wall - 1, -1, -1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                else:
                    break
            left_wall += 1
        


if __name__ == '__main__':
    arr = [5, 4, 3, 6, 1, 2, 3]
    arr_sorted = sorted(arr)
    sort = Sort()
    
    x = arr.copy()
    sort.selection_sort(x)
    print(x)
    assert(x == arr_sorted)
    print()

    x = arr.copy()
    sort.bubble_sort(x)
    print(x)
    assert(x == arr_sorted)
    print()

    x = arr.copy()
    sort.insertion_sort(x)
    print(x)
    assert(x == arr_sorted)
    print()
