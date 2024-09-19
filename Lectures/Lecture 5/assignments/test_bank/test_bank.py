from bank import value

def test_0():
    assert value("Hello good sir") == 0
    assert value("Hello dude") == 0
    assert value("Hello") == 0
    
def test_20():
    assert value("hey") == 20
    
def test_100():
    assert value("Whats up") == 100
    
    

