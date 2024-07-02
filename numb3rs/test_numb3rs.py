from numb3rs import validate
# import pytest

def test_validate_range():
    assert validate("524.425.454.1000")==False
    assert validate("0.0.0.0")==True
    assert validate("255.255.255.255")==True

def test_validate_ip():
    assert validate("1555.555")==False
    assert validate("244.255.123.123.122")==False

def test_validate_nums():
    assert validate("192.168.4.f1")==False
    assert validate("f.a.b.c")==False

def test_validate_str():
    assert validate("cat")==False
    assert validate("cat.cat.cat.cat")==False