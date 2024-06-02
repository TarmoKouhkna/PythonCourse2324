def quicksort(sortable):
    print(sortable)
    if len(sortable) <= 1:
        return sortable

    pivot = sortable[0]
    items_lower = [item for item in sortable[1:] if item <= pivot]
    items_greater = [item for item in sortable[1:] if item > pivot]

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


sorting_list = [0, 3, 6, 9, 5, 4, 1, 2, 6, 55, 7, 9, 4, 33, 6, 9, 7, 141, 9, 96, 58, 1, 32, 3]
sorted_list = quicksort(sorting_list)
print(sorted_list)
