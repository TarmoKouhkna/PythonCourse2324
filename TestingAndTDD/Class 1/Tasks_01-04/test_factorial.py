from factorial import factorial

# ____________________________________
# def test_factorial():
#     assert factorial(0) == 1
#     assert factorial(1) == 1
#     assert factorial(2) == 2
#     assert factorial(3) == 6
#     assert factorial(4) == 24
#     assert factorial(5) == 120
#
#
# if __name__ == '__main__':
#     pytest.main()
# ___________________________________
import pytest


@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def test_factorial(n, expected):
    assert factorial(n) == expected
