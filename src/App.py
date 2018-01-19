#!/usr/bin/python3

import datetime
from CoinbasePrices import EurSellPrices
from BinancePrices import EthBidPrices
from MongoLog import LogPrices
from Query import MongoQueries
from Calculate import Calculators

NOW = datetime.datetime.now()
DATEHOUR = datetime.datetime(NOW.year, NOW.month, NOW.day, NOW.hour, 0, 0, 0)

eur_sell_prices = EurSellPrices()
EthEurSellPrice = eur_sell_prices.fetch_etheur(DATEHOUR)

eth_bid_prices = EthBidPrices()
eth_binance_symbols = eth_bid_prices.fetch_eth(EthEurSellPrice)

log_prices = LogPrices()
log_prices.eur_bid_prices(eth_binance_symbols)

mongo_queries = MongoQueries()
prices_df = mongo_queries.hourly_prices_per_symbol_df()

calculators = Calculators()
statsreport = calculators.stats_report(DATEHOUR, prices_df)

print(statsreport)
