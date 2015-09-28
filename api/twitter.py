from TwitterAPI import TwitterAPI


class Twitter:
    def __init__(self):
        self.api = TwitterAPI(
            'LmACQX3XV1c9rA05MfYVbB9OG',
            'ik7nVuZ0AtXffKjnqCjdCN1rTFVmod7Leehwbx1mezEDXCZAx8',
            '2899747854-L4CzMtqL6BJQLsXNjs64xKavFqAPf3bPgspn4Aq',
            '7zy5QY2hIKwzyUbJ5X9gPDluAoLbOzrFongjqFAiMI8dN'
        )
        self.influential = (
            'CNBC', 'RANsquawk', 'the_real_fly', 'Wsjmarkets', 'Business'
        )

    def search(self, symbol, name, user=None, until=None):
        q = symbol + ' OR ' + name
        if user:
            q += ' from:' + user
        if until:
            q += ' until:' + until
        req = self.api.request('search/tweets', {'q': q, 'count': 100})
        return [twt['text'] for twt in req]

    def influential_tweets(self, symbol, name, until=None):
        influentials = []
        for user in self.influential:
            req = self.search(symbol, name, user, until)
            influentials += req
        return influentials

    def get_tweets(self, symbol, name, until=None):
        return self.search(symbol, name, None, until) + self.influential_tweets(symbol, name, until)
