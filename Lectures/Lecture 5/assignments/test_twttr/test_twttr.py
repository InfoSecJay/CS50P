from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"
    
def test_number():
    assert shorten("4") == "4"
    
def test_punctuation():
    assert shorten("test,") == "tst,"
    
def test_upper():
    assert shorten("UPPER") == "PPR"