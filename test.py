from api.guardian import Guardian
from api.twitter import Twitter
from datetime import datetime
from text.analysis import analyze_list


def today():
    d = datetime.now()
    return '%s-%s-%s' % (d.year, d.month, d.day)

twitter = Twitter()
guardian = Guardian()


def get_data(symbol, name, from_date=today(), to_date=today()):
    g = guardian.get_stories(name, from_date, to_date)
    t = twitter.get_tweets(symbol, name, to_date)
    print(' ')
    print(' ')
    return analyze_list(g.get('text') + t) * g.get('count', 1)
