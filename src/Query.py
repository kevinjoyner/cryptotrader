#!/usr/bin/python3

""" For querying tracked prices and calculating variances etc. """

import pandas as pd
from pymongo import MongoClient

CLIENT = MongoClient()
DB = CLIENT.cryptotracker

VALUES = []
HOURS = []
for cc in db.eur_prices.find():
    HOURS.append(datetime.datetime.fromtimestamp(cc['hour_micro']/1000000))
    VALUES.append({'symbol': cc['symbol'], 'EURbidPrice': cc['EURbidPrice']})

DF = pd.DataFrame(VALUES, index=pd.DatetimeIndex(HOURS))
DF = DF.pivot(index=None, VALUES='EURbidPrice', columns='symbol')

print(DF)
