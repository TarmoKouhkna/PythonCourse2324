from vowels import count_vowels


def test_count_vowels():
    text = "Tere tere vana kere Tarmo"
    result = count_vowels(text)
    assert result == 10
