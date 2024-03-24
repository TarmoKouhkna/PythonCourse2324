from fibonacci import fibonacci

# def test_fibonacci():
#     assert fibonacci(0) == 0
#     assert fibonacci(1) == 1
#     assert fibonacci(2) == 1
#     assert fibonacci(3) == 2
#     assert fibonacci(4) == 3
#     assert fibonacci(5) == 5
#     assert fibonacci(6) == 8
#
#
# if __name__ == '__main__':
#     pytest.main()
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

import pytest


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8)
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


if __name__ == '__main__':
    pytest.main()
