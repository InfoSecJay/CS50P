from jar import Jar
import pytest

def test_init():
    jar = Jar()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    with pytest.raises(ValueError):
        jar.deposit(100)

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(4)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.deposit(100)