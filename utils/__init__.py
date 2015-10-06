from datetime import datetime
import redis


def singleton(cls):
    instances = {}
    if cls not in instances:
        instances[cls] = cls()
    return instances[cls]


def today():
    d = datetime.now()
    return '%s-%s-%s' % (d.year, d.month, d.day)


def now():
    return datetime.now().strftime('%m-%d-%YT%H:%M')


@singleton
class Redis:
    def __init__(self):
        self.client = redis.StrictRedis(host='localhost', port=6379, db=0)

    def get(self, name):
        return self.client.get(name)

    def hmset(self, name, dic):
        return self.client.hmset(name, dic)

    def hmget(self, name, keys):
        return self.client.hmget(name, keys)

    def set(self, name, value):
        return self.client.set(name, value)
