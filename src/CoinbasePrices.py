#!/usr/bin/python3

""" For retreiving prices from Coinbase """

import urllib.parse
import urllib.request
import json
import datetime

BASEURL = "https://api.coinbase.com/v2/prices/"
HEADERS = {"CB-VERSION": "2017-08-07"}

class EurSellPrices:
    """ For retreiving EUR sell prices """

    def fetch_etheur(self):
        """ Gets the sell price of ETH in EUR from Coinbase and timestamps it
            with the current hour in microseconds """

        url = BASEURL + '/ETH-EUR/sell'

        req = urllib.request.Request(url, None, HEADERS)
        with urllib.request.urlopen(req) as response:
            price = json.loads(response.read().decode('utf-8'))

        epoch = datetime.datetime.utcfromtimestamp(0)
        price['time'] = round((datetime.datetime.now() - epoch).total_seconds() * 1000000)

        return price
