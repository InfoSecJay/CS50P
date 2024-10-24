from seasons import time_delta
import pytest

def test_dates():
    assert time_delta("2023-10-05") == "Five hundred twenty-seven thousand forty minutes"
    assert time_delta("2022-10-05") == "One million, fifty-two thousand, six hundred forty minutes"
    
def test_format():
    with pytest.raises(SystemExit, match="Invalid date"):
        time_delta('January 1, 1999')
        
def test_date():
    with pytest.raises(SystemExit, match="Invalid date"):
        time_delta('1991-35-35')
