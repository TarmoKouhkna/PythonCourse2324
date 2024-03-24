from play_with_words import format_sentence

def test_format_sentence():
    sentence = "Tere tere vana kere Tarmo"
    expected_output = "TeR!e Te!rE v!Ana !keRe! Tar!Mo"

    assert format_sentence(sentence) == expected_output