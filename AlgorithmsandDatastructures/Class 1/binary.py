def binary_iter(arr, x):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        steps = steps + 1
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return steps
    return -1


pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
the_page = 19

print(binary_iter(pages, the_page))
