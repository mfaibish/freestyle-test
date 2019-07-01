#showtimes_test.py

from showtimes import date_format

def test_date_format():
    assert date_format("2019-01-23") == "Wednesday, January 23, 2019"