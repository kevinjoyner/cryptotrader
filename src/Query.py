#!/usr/bin/python3

""" For querying tracked prices """

import datetime
import pandas as pd
from pymongo import MongoClient

CLIENT = MongoClient()
DB = CLIENT.cryptotracker

class MongoQueries:
    """ For retreiving previously logged data """

    def hourly_prices_per_symbol_df(self, query=None):
        """ Returns pandas dataframe of EUR prices with column for each symbol indexed by
            hourly datetime timestamps"""

        values = []
        hours = []
        for record in DB.eur_prices.find(query):
            hours.append(datetime.datetime.fromtimestamp(record['hour_micro']/1000000))
            values.append({'symbol': record['symbol'], 'EURbidPrice': record['EURbidPrice']})

        dataframe = pd.DataFrame(values, index=pd.DatetimeIndex(hours))
        dataframe = dataframe.pivot(index=None, values='EURbidPrice', columns='symbol')
        dataframe = dataframe.apply(pd.to_numeric, errors='ignore')

        return dataframe
