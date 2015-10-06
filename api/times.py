import requests
from utils import singleton, today


@singleton
class Times:
    def __init__(self):
        self.article_key = '0ef62d9d804001c734eac1302721ec36:7:68950361'
        self.popular_key = '0b21208f8418cae0691da24369777e5a:9:68950361'

    def get_article(self, url, query=None):
        params = {'api-key': self.article_key, 'format': 'json'}
        if query:
            params.update(query)
        req = requests.get(url, params=params)
        return req.json()

    def search(self, q):
        return self.get_article(
            'http://api.nytimes.com/svc/search/v2/articlesearch.json',
            {'from-date': today().replace('-', ''), 'to-date': today().replace('-', ''), 'q': q}
        )

    def most_popular(self):
        req = requests.get(
            'http://api.nytimes.com/svc/mostpopular/v2/mostviewed.json',
            params={'api-key': self.popular_key, 'time-period': 1}
        )
        return [story.get('headline') for story in req.json().get('results', [])]

    def get_stories(self, symbol, name):
        q = symbol + 'OR' + name
        res = self.search(q).get('response', {})
        return [
            '%s %s' % (story.get('abstract'), story.get('headline', {}).get('main')) for story in res.get('docs', [])
        ]

    def text(self, symbol, name):
        return self.get_stories(symbol, name) + self.most_popular()
