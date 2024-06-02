def infinite_range(start, step):
    num = start
    while True:
        yield num
        num += step


result = infinite_range(0, 2)
for i in range(10):
    print(next(result))
