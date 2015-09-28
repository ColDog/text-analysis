from flask import Flask, request
from api.guardian import Guardian
from api.twitter import Twitter
from api.times import Times
from datetime import datetime
from text.analysis import analyze_list
import redis

redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)
twitter = Twitter()
guardian = Guardian()
times = Times()
app = Flask(__name__, static_url_path='')


def today():
    d = datetime.now()
    return '%s-%s-%s' % (d.year, d.month, d.day)


def get_data(symbol, name, from_date, to_date):
    g = guardian.get_stories(name, from_date, to_date)
    t = twitter.get_tweets(symbol, name, to_date)
    ts = times.get_stories(name, from_date, to_date)
    if from_date == today():
        ts += times.most_popular()
    print(' ')
    print(' ')
    for words in g + t + ts:
        print(words)
    return analyze_list(g + t + ts)


def redis_name(sym, name, from_date, to_date):
    return 'ticker:%s-name:%s-from:%s-to:%s' % (sym, name, from_date, to_date)


def respond(sym, from_date, to_date):
    name = request.args.get('name', sym)
    cached = redis_db.get(redis_name(sym, name, from_date, to_date))
    if cached:
        return cached
    else:
        val = str(get_data(sym, name, from_date, to_date))
        redis_db.set(redis_name(sym, name, from_date, to_date), val)
        return val


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/ticker/<sym>/today')
def ticker_today(sym):
    return respond(sym, today(), today())


@app.route('/ticker/<sym>/from/<from_date>/to/<to_date>')
def ticker_date(sym, from_date, to_date):
    return respond(sym, from_date, to_date)


app.run(debug=True)
