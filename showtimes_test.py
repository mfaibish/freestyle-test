#showtimes_test.py

from showtimes import date_format, datetime

def test_date_format():
    x = "2019-07-01 10:49:29.621754"
    today_date = x.strftime("%A, %B %d, %Y")
    assert today_date == "Monday, July 01, 2019"


def test_time_format():
    t = datetime.datetime.strptime("22:00", "%H:%M")
    assert t == "10:00 PM"