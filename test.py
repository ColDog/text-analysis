from app import get_data
from app import today


list_of_words = get_data('goog', 'google', today(), today())
for words in list_of_words:
    print(words)
