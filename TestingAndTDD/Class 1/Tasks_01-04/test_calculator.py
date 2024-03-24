import pytest

from calculator import calculator


def test_calculator():
    assert calculator('+', 3, 4) == 7
    assert calculator('-', 5, 2) == 3
    assert calculator('*', 2, 3) == 6
    assert calculator('/', 10, 2) == 5
    with pytest.raises(ValueError):
        calculator('/', 10, 0)
    with pytest.raises(ValueError):
        calculator('!', 2, 3)


if __name__ == '__main__':
    pytest.main()
