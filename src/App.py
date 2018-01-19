#!/usr/bin/python3

import datetime
from CoinbasePrices import EurSellPrices
from BinancePrices import EthBidPrices
from MongoLog import LogPrices

NOW = datetime.datetime.now()
DATEHOUR = datetime.datetime(NOW.year, NOW.month, NOW.day, NOW.hour, 0, 0, 0)

eur_sell_prices = EurSellPrices()
EthEurSellPrice = eur_sell_prices.fetch_etheur(DATEHOUR)

eth_bid_prices = EthBidPrices()
eth_binance_symbols = eth_bid_prices.fetch_eth(EthEurSellPrice)

log_prices = LogPrices()
log_prices.eur_bid_prices(eth_binance_symbols)
