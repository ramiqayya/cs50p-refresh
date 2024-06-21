from bank import value


def test_value_capital():
    assert value("HELLO")=="$0"
    assert value("HI")=="$20"
    assert value("WIE GEHT'S")=="$100"

def test_value_small():
    assert value("hello")=="$0"
    assert value("hi")=="$20"
    assert value("wie geht's")=="$100"

def test_value_space():
    assert value("    hello   ")=="$0"
    assert value("   hi   ")=="$20"
    assert value("   wie geht's    ")=="$100"



