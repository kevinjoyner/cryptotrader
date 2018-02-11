#!/usr/bin/python3

""" For logging data to MongoDB """

from pymongo import MongoClient
import json
from sqlalchemy import create_engine

DB = MongoClient().cryptotracker

class LogPrices:
    """ For logging prices """

    def eur_bid_prices(self, eth_binance_symbols):
        """ Logs EUR bid prices for symbols you can buy on Binance with ETH """

        data = []
        for item in eth_binance_symbols:
            data.extend([{
                "hour_micro": item["EthEurTime"],
                "symbol": item["symbol"][:-3],
                "EURbidPrice": item["EURbidPrice"]
            }])
        DB.eur_prices.insert(data)

        return

class PostgresLogging:
    """ For adding dataframes to the Postgres table """
    
    def prices_pivot(self, prices_df):
        """ Adds the Prices Pivot dataframe to Postgresql database """

        with open('../creds/pg_creds.json') as json_data:
            d = json.load(json_data)
            json_data.close()

        user = d[0]['user']
        password = d[0]['password']
        
        engine_string = 'postgresql://' + user + ':' + password + '@localhost:5432/cryptotracker'
        engine = create_engine(engine_string)
        prices_df.to_sql('eur_prices', engine)

        return