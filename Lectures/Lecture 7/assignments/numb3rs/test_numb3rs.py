import pytest
from numb3rs import validate


def test_formatting():
    assert validate("10.20.30.40") == True
    assert validate("10.20.30") == False
    assert validate("10.20") == False
    assert validate("10") == False

def test_ranges():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.512.1") == False
    assert validate("1.1.1.512") == False

def test_word():
    assert validate("cat") == False