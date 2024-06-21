from fuel import convert,gauge

def test_conver_per():
    assert convert("3/4")== 75
    assert convert("1/2")== 50

def test_conver_zero():
    assert convert("0/4")== 0
    assert convert("1/0")== "zero"
    assert convert("5/2")== "zero"


def test_guage_full():
    assert gauge(99)=="F"
    assert gauge(100)=="F"

def test_guage_empty():
    assert gauge(1)=="E"
    assert gauge(0)=="E"

def test_guage_per():
    assert gauge(75)=="75%"
    assert gauge(50)=="50%"

