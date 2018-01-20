#!/usr/bin/python3

""" Main script """

import datetime
from CoinbasePrices import EurSellPrices
from BinancePrices import EthBidPrices
from MongoLog import LogPrices
from Query import MongoQueries
from Report import Reports

NOW = datetime.datetime.now()
DATEHOUR = datetime.datetime(NOW.year, NOW.month, NOW.day, NOW.hour, 0, 0, 0)

EURSELLPRICES = EurSellPrices()
ETHEURSELLPRICE = EURSELLPRICES.fetch_etheur(DATEHOUR)

ETHBIDPRICES = EthBidPrices()
ETHBINANCESYMBOLS = ETHBIDPRICES.fetch_eth(ETHEURSELLPRICE)

LOGPRICES = LogPrices()
LOGPRICES.eur_bid_prices(ETHBINANCESYMBOLS)

MONGOQUERIES = MongoQueries()
PRICESDF = MONGOQUERIES.hourly_prices_per_symbol_df()

REPORTS = Reports()
STATSREPORT = REPORTS.stats_report(DATEHOUR, PRICESDF)
