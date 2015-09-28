import requests


class Guardian:
    def __init__(self):
        self.api_key = '8amqwrxyxuhvb8zyvearzv66'

    def get(self, url, query=None):
        params = {'api-key': self.api_key, 'format': 'json'}
        if query:
            params.update(query)
        req = requests.get(url, params=params)
        return req.json()

    def search(self, q, from_date, to_date):
        return self.get('http://content.guardianapis.com/search', {'from-date': from_date, 'to-date': to_date, 'q': q})

    def get_stories(self, q, from_date, to_date):
        res = self.search(q, from_date, to_date).get('response', {})
        return [story.get('webTitle') for story in res.get('results', [])]
