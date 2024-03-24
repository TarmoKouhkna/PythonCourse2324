from century import get_century


def test_get_century():
    assert get_century(2001) == 21
    assert get_century(1905) == 20
    assert get_century(1812) == 19
