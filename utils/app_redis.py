import redis
from utils import singleton


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