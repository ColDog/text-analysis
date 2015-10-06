from utils.app_redis import Redis
import requests


def get_data():
    return requests.get('ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt').raw()


def strip_name(name):
    spl = name.split('-')[0]
    name2 = spl.replace('Inc.', '')
    name3 = name2.replace('Corp.', '')
    return name3


def data():
    symbols = {}
    for line in get_data().split('\n'):
        spl = line.split('|')
        symbols[spl[0]] = {'name': strip_name(spl[1]), 'category': spl[2]}
    return symbols


def save_data():
    Redis().hmset('symbols', data())
