#!/usr/bin/python3

""" For logging data to MongoDB """

from pymongo import MongoClient

DB = MongoClient().cryptotracker

class LogPrices:
    """ For logging prices """

    def eur_bid_prices(self, eth_binance_symbols):
        """ Logs EUR bid prices for symbols you can buy on Binance with ETH """

        data = []
        for item in eth_binance_symbols:
            data.extend([{
                "hour_nano": item["EthEurTime"],
                "symbol": item["symbol"][:-3],
                "EURbidPrice": item["EURbidPrice"]
            }])
        DB.eur_prices.insert(data)

        return
