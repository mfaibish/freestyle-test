#showtimes_test.py

from showtimes import date_format, datetime

def test_date_format():
    d = datetime.date(2019, 1, 22)
    full_date = d.strftime("%A, %B %d, %Y")
    assert full_date == "Tuesday, January 22, 2019"


def test_time_format():
    t = datetime.datetime.strptime("22:00", "%H:%M")
    assert t.strftime("%I:%M %p") == "10:00 PM"