from is_prime import is_prime


# def test_is_prime():
#     assert is_prime(0) == False
#     assert is_prime(1) == False
#     assert is_prime(2) == True
#     assert is_prime(3) == True
#     assert is_prime(4) == False
#     assert is_prime(5) == True
#     assert is_prime(6) == False
#     assert is_prime(7) == True
#     assert is_prime(8) == False
#     assert is_prime(9) == False
#     assert is_prime(10) == False
#     assert is_prime(11) == True
#
#
# if __name__ == '__main__':
#     pytest.main()

import pytest


@pytest.mark.parametrize("n, expected", [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
    (11, True),
])
def test_is_prime(n, expected):
    assert is_prime(n) == expected
