#!/usr/bin/python3

""" Main script """

import datetime
from CoinbasePrices import EurSellPrices
from BinancePrices import EthBidPrices
from Log import LogPrices
from Query import MongoQueries
from Log import PostgresLogging
from Report import Reports

   
NOW = datetime.datetime.now()
DATEHOUR = datetime.datetime(NOW.year, NOW.month, NOW.day, NOW.hour, 0, 0, 0)

ETHEURSELLPRICE = EurSellPrices().fetch_etheur(DATEHOUR)
ETHBINANCESYMBOLS = EthBidPrices().fetch_eth(ETHEURSELLPRICE)

LogPrices().eur_bid_prices(ETHBINANCESYMBOLS)
PostgresLogging().hourly_prices(ETHBINANCESYMBOLS)

# PRICESDF = MongoQueries().hourly_prices_per_symbol_df()

# Set argument if_exists to 'replace' for replacing the pg db
# PostgresLogging().prices_pivot(PRICESDF)

# STATSREPORT = Reports().stats_report(DATEHOUR, PRICESDF)
