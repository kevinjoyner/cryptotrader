#!/usr/bin/python3

""" For retreiving prices from Binance """

import urllib.parse
import urllib.request
import json

BASEURL = "https://api.binance.com/api/v3/ticker/bookTicker"

class EthBidPrices:
    """  Get Book Ticker records from Binance """

    def fetch_eth(self, eth_eur_sell_price):
        """  Get bid price of all currenices in ETH from binance and add timestamped
             conversion to EUR """

        req = urllib.request.Request(BASEURL)
        with urllib.request.urlopen(req) as response:
            binance_symbols = json.loads(response.read().decode('utf-8'))

        eth_binance_symbols = []
        for item in binance_symbols:
            if item['symbol'].endswith('ETH'):
                eth_binance_symbols.append(item)

        for item in eth_binance_symbols:
            item['EURbidPrice'] = str(
                float(item['bidPrice']) * float(eth_eur_sell_price['data']['amount'])
            )
            item['EthEurTime'] = eth_eur_sell_price['time']

        return eth_binance_symbols
