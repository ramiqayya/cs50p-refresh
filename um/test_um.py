from um import count

def test_count():
    assert count("um")==1
    assert count("um.. yes, um")==2


def test_count_words():
    assert count("yummy")==0
    assert count("circumscription")==0

def test_count_capital():
    assert count("YUMMY")==0
    assert count("UM, YES uM.")==2