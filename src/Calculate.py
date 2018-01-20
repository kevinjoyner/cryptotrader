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
            try:
                prices_df[symbol][seven_days_ago]
                prices_df[symbol][nineteen_hours_ago]
                prices_df[symbol][hour_ago]
            except:
                continue
            else:
                value = {}
                value['symbol'] = symbol
                value['recent_std_dev'] = np.std(prices_df[symbol][nineteen_hours_ago:hour_ago].apply(float))

                value['seven_day_delta'] = \
                (float(prices_df[symbol][hour_ago]) - float(prices_df[symbol][seven_days_ago])) \
                / float(prices_df[symbol][seven_days_ago])

                values.append(value)

        return pd.DataFrame(values)
