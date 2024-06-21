from plate import is_valid

def test_is_valid_two_letter():
    assert is_valid("CS50")==True
    assert is_valid("C1240")==False

def test_is_valid_char_count():
    assert is_valid("C")==False
    assert is_valid("GOODBYE")==False
    assert is_valid("HELLO")==True

def test_is_valid_num_location():
    assert is_valid("AAA555")==True
    assert is_valid("AAA55A")==False

def test_is_valid_zero_location():
    assert is_valid("AAA055")==False
    assert is_valid("AAA550")==True
    