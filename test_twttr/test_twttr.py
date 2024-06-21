from twttr import shorten

def test_shorten_upper():
    assert shorten("TWITTER")=="TWTTR"
    assert shorten("TAKEHA")=="TKH"

def test_shorten_lower():
    assert shorten("twitter")=="twttr"
    assert shorten("takeha")=="tkh"

def test_shorten_numbers():
    assert shorten("123 nummber")=="123 nmmbr"
    assert shorten("cs50 python")=="cs50 pythn"