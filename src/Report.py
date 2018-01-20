#!/usr/bin/python3

""" For calculating and reporting stats """

from datetime import timedelta
import pandas as pd
import numpy as np

class Reports:
    """ For calculating and reporting stats """

    def stats_report(self, datehour, prices_df):
        """ Returns dataframe indexed on currency Symbol giving recent standard deviation and
            longer term deltas for each """

        values = []
        seven_days_ago = datehour - timedelta(hours=((6*24)-1))
        nineteen_hours_ago = datehour - timedelta(hours=19)
        hour_ago = datehour - timedelta(hours=1)

        for symbol in prices_df.columns:
            if prices_df[symbol][seven_days_ago] and prices_df[symbol][hour_ago]:
                value = {}
                value['symbol'] = symbol
                value['recent_std_dev'] = np.std(prices_df[symbol][nineteen_hours_ago:hour_ago])

                value['seven_day_delta'] = \
                (prices_df[symbol][hour_ago] - prices_df[symbol][seven_days_ago]) \
                / prices_df[symbol][seven_days_ago]

                values.append(value)

        dataframe = pd.DataFrame(values).set_index('symbol')
        dataframe = dataframe.apply(pd.to_numeric, errors='ignore')
        return dataframe
