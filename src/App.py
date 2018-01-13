#!/usr/bin/python3

from CoinbasePrices import EurSellPrices
from BinancePrices import EthBidPrices
from MongoLog import LogPrices

eur_sell_prices = EurSellPrices()
EthEurSellPrice = eur_sell_prices.fetch_etheur()

eth_bid_prices = EthBidPrices()
eth_binance_symbols = eth_bid_prices.fetch_eth(EthEurSellPrice)

log_prices = LogPrices()
log_prices.eur_bid_prices(eth_binance_symbols)
