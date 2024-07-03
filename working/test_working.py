from working import convert,time_converter_AM,time_converter_PM
import pytest


def test_time_converter_AM():
    assert time_converter_AM("9")=="09:00"
    assert time_converter_AM("9:05")=="09:05"

def test_time_converter_PM():
    assert time_converter_PM("9")=="21:00"
    assert time_converter_PM("9:05")=="21:05"

def test_time_converter_PM_errors():
    with pytest.raises(ValueError):
        time_converter_PM("13:06")
    with pytest.raises(ValueError):
        time_converter_PM("1:97")    

def test_time_converter_AM_errors():
    with pytest.raises(ValueError):
        time_converter_AM("13:05")
    with pytest.raises(ValueError):
        time_converter_AM("1:64")

def test_convert():
    assert convert("9:57 AM to 8:33 PM")=="09:57 to 20:33"
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"
    assert convert("9 PM to 5 AM")=="21:00 to 05:00"

def test_convert_errors():
    with pytest.raises(ValueError):
        convert("15:12 AM to 1:00 PM")
    with pytest.raises(ValueError):
        convert("1:12 AM - 1:00 PM")
    with pytest.raises(ValueError):
        convert("cat to cat")
        
