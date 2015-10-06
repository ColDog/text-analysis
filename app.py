from flask import Flask, request
from data.data import get_data
from utils.today import now

app = Flask(__name__)


@app.route('/<sym>/now')
def ticker_today(sym):
    return get_data(sym, now())


@app.route('/<sym>/<time>')
def ticker_time(sym, time):
    return get_data(sym, time)


app.run(debug=True)
