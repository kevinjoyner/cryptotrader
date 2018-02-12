#!/usr/bin/python3

""" For logging data to MongoDB """

from pymongo import MongoClient
import datetime
import pandas as pd
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
    
    def hourly_prices(self, eth_binance_symbols):
        """ Logs EUR bid prices to postgres """
        
        date_hour = []
        symbol = []
        eurbidprice = []
        dict_for_df = {
            'date_hour': date_hour,
            'symbol': symbol,
            'eurbidprice': eurbidprice
        }
        for item in eth_binance_symbols:
            dict_for_df['date_hour'].append(
                datetime.datetime.fromtimestamp(item["EthEurTime"]/1000000).strftime("%Y%m%d%H")
            )
            dict_for_df['symbol'].append(item["symbol"][:-3])
            dict_for_df['eurbidprice'].append(item["EURbidPrice"])
        input_df = pd.DataFrame(dict_for_df)
        
        with open('../creds/pg_creds.json') as json_data:
            d = json.load(json_data)
            json_data.close()

        user = d[0]['user']
        password = d[0]['password']
        
        engine = create_engine('postgresql://' + user + ':' + password + '@localhost:5432/cryptotracker')
        input_df.to_sql('eur_prices', engine, schema="public", if_exists='append', index=False)

        return


    def prices_pivot(self, prices_df, if_exists='append'):
        """ Adds the Prices Pivot dataframe to Postgresql database """

        prices_df['date_hour'] = prices_df.index
        prices_df['date_hour'] = prices_df['date_hour'].dt.strftime('%Y%m%d%H')
        prices_df['eurbidprice'] = prices_df['EURbidPrice']
        prices_df.drop(['EURbidPrice'], axis=1, inplace = True)
        
        with open('../creds/pg_creds.json') as json_data:
            d = json.load(json_data)
            json_data.close()

        user = d[0]['user']
        password = d[0]['password']
        
        engine = create_engine('postgresql://' + user + ':' + password + '@localhost:5432/cryptotracker')
        prices_df.to_sql('eur_prices', engine, schema="public", if_exists=if_exists, index=False)

        return
