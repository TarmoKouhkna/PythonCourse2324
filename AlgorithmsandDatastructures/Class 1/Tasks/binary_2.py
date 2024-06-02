def binary_recursive(arr, x, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] < x:
        return binary_recursive(arr, x, mid + 1, high)
    elif arr[mid] > x:
        return binary_recursive(arr, x, low, mid - 1)
    else:
        return mid


pages = [n for n in range(1, 21)]
the_page = 7

index = binary_recursive(pages, the_page)
if index != -1:
    print(f"The page {the_page} is at index {index}.")
else:
    print(f"The page {the_page} is not found.")
