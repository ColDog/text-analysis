from text.keywords import KEYWORDS
from textblob import TextBlob


def avg(l):
    try:
        return float(sum(l)) / float(len(l))
    except ZeroDivisionError:
        return 0.0


def analyze_list(list_of_words):
    scores = []
    for words in list_of_words:
        score = keyword(words)
        if score > 0:
            scores.append(score * sentiment(words))
    return avg(scores)


def sentiment(words):
    return TextBlob(words).sentiment.polarity


def keyword(words):
    key_score = 0
    for word in words.split(' '):
        if word.lower() in KEYWORDS:
            key_score += 1
    return key_score
