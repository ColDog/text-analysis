from data.data import get_data
from utils.today import now

while True:
    symbol = raw_input("\n\nTicker: ")
    get_data(symbol, now())
