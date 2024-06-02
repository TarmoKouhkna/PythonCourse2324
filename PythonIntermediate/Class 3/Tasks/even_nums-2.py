def even_numbers(limit):
    for num in range(2, limit + 1, 2):
        yield num
        print('Yield Done its job')

limit = 20
even_nums = even_numbers(limit)
for num in even_nums:
    print(num)
