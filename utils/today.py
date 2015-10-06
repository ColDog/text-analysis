from datetime import datetime


def today():
    d = datetime.now()
    return '%s-%s-%s' % (d.year, d.month, d.day)


def now():
    return datetime.now().strftime('%m-%d-%YT%H:%M')