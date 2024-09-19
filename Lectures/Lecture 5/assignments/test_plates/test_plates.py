from plates import is_valid

def test_start_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("12") == False

def test_min_max_char():
    assert is_valid("AAAAAAA") == False
    assert is_valid("AAAAAA") == True
    assert is_valid("A") == False

def test_middle_numbers():
    assert is_valid("AAA0AA") == False
    assert is_valid("AAA012") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_punctuation():
    assert is_valid("AAA,AA") == False
    assert is_valid("AAA 12") == False
