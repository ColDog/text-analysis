import requests
from utils.singleton import singleton
from utils.today import today


@singleton
class Guardian:
    def __init__(self):
        self.api_key = '8amqwrxyxuhvb8zyvearzv66'

    def get(self, url, query=None):
        params = {'api-key': self.api_key, 'format': 'json'}
        if query:
            params.update(query)
        req = requests.get(url, params=params)
        return req.json()

    def search(self, q):
        return self.get('http://content.guardianapis.com/search', {'from-date': today(), 'to-date': today(), 'q': q})

    def get_stories(self, symbol, name):
        q = symbol + 'OR' + name
        res = self.search(q).get('response', {})
        return [story.get('webTitle') for story in res.get('results', [])]

    def text(self, symbol, name):
        return self.get_stories(symbol, name)
