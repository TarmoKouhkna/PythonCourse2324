def generator(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2
        print('Yield Done its job')


# Example usage
limit = 20
even_nums = generator(limit)
for num in even_nums:
    print(num)
