import pytest

from fuel import gauge, convert

def test_convert():
    assert convert("1/4") == 25
    
def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"
    
def test_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    
def test_value_error():
    with pytest.raises(ValueError):
        convert("three/four")