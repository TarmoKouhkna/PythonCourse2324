def sort_odds(arr):
    # Extract odd numbers and sort them
    odds = sorted([x for x in arr if x % 2 != 0])
    # Replace odd numbers in the original array with sorted odd numbers
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            arr[i] = odds.pop(0)
    return arr


# Test cases
print(sort_odds([7, 1]))  # Output: [1, 7]
print(sort_odds([5, 8, 6, 3, 4]))  # Output: [3, 8, 6, 5, 4]
print(sort_odds([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # Output: [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
