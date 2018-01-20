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
        seven_days_ago = datehour - timedelta(days=7)
        nineteen_hours_ago = datehour - timedelta(hours=19)
        hour_ago = datehour - timedelta(hours=1)

        for symbol in prices_df.columns:
            value = {}
            value['symbol'] = symbol
            value['recent_std_dev'] = np.std(prices_df[symbol][nineteen_hours_ago:hour_ago].apply(float))

            value['seven_day_delta'] = \
            (prices_df[symbol][hour_ago].apply(float) - prices_df[symbol][seven_days_ago].apply(float)) \
            / prices_df[symbol][seven_days_ago].apply(float)

            values.append(value)

        return pd.DataFrame(values)
