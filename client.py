from TwitterAPI import TwitterAPI
from textblob import TextBlob


class TraderResult:
    def __init__(self, tweets):
        self.tweets = tweets

    def analyze_sentiment(self):
        polarity = []
        for twt in self.tweets:
            polarity.append(TextBlob(twt).sentiment.polarity)
        try:
            return sum(polarity) / float(len(polarity))
        except ZeroDivisionError:
            return 0


class Trader:
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
        twts = self.search(symbol, name, None, until) + self.influential_tweets(symbol, name, until)
        print ' '
        print 'TWEETS-----'
        print twts
        return TraderResult(twts)


trader = Trader()
goog = trader.get_tweets('$goog', 'google', '2015-09-25')
print goog.analyze_sentiment()
