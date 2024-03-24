from anagrams import is_anagrams


def test_anagrams():
    assert is_anagrams("listen", "silent") == True
