from api.guardian import Guardian
from api.twitter import Twitter
from api.times import Times
from utils import Redis, now
import json
from config import *


def redis_name(symb, time):
    return symb + ':' + time


def get_data(symbol, time):
    if CACHING:
        lookup = Redis().get(redis_name(symbol, time))
        if lookup:
            return lookup
    return Data(symbol).process()


class Data:
    def __init__(self, symbol):
        self.symbol = symbol
        self.data = []
        self.filtered = []
        self.sentiment = None
        self.relevance = None
        self.time = now()

    def process(self):
        self.collect()
        self.filter()
        self.analyze()
        self.log()
        self.save()
        return self.to_json()

    def log(self):
        if LOGGING:
            for line in self.data:
                print(line)
            print(' ')
            print('sentiment:', self.sentiment)
            print('relevance:', self.relevance)

    def collect(self):
        name = Redis().hmget('symbols', self.symbol)
        self.data = Guardian().text(self.symbol, name) + \
            Twitter().text(self.symbol, name) + \
            Times().text(self.symbol, name)

    def filter(self):
        self.filtered = 'some value'
        return self

    def analyze(self):
        self.sentiment = 'some value'
        self.relevance = 'some value'
        return self

    def to_json(self):
        return json.dumps({'sentiment': self.sentiment, 'relevance': self.relevance})

    def save(self):
        Redis().set(redis_name(self.symbol, self.time), self.to_json())
        return self

