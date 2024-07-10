from seasons import get_birthday,age_minutes
import pytest


def test_get_birthday():
    # assert get_birthday("15-05-2014")=="Invalid date"
    with pytest.raises(ValueError):
        get_birthday("15-05-2015")
    with pytest.raises(ValueError):
        get_birthday("January, 14th 2015")

def test_get_birthday_string():
    with pytest.raises(ValueError):
        get_birthday("Hello")

