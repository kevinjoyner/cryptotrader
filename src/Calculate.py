#!/usr/bin/python3

""" For calculating variances etc. """

from datetime import timedelta
import pandas as pd
import numpy as np

class Calculators:
    """ . """

    def stats_report(self, datehour, prices_df):
        """ . """

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

        return pd.DataFrame(values)
