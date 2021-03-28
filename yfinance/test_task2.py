
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import yfinance as yf
import unittest
from unittest.mock import Mock
from unittest.mock import patch
import pandas as pd

symbols = ['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD']
tickers = [yf.Ticker(symbol) for symbol in symbols]


class TestEvent2(unittest.TestCase):
    def fill_calendar(self, data):
        try:
            cal = _pd.DataFrame(
                data)
            cal1 = cal
            cal['earningsDate'] = _pd.to_datetime(
                cal['earningsDate'], unit='s')
            self._calendar = cal.T
            self._calendar.index = utils.camel2title(self._calendar.index)
            self._calendar.columns = ['Value']
            return cal1
        except Exception:
            pass

    def set (self):
        self.msft = yf.Ticker("MSFT")
        self.utils_mock = patch('yfinance.base.utils.get_json', autospec=True).start()
        self.addCleanup(patch.stopall)

    def test_event_contains(self):
        data = {'earningsDate': None, 'earningsAverage': None, 'earningsLow': None,
                'earningsHigh': None, 'revenueAverage': None, 'revenueLow': None,
                'revenueHigh': None}
        try:
            calendar = self.fill_calendar(data)
            self.assertIsNotNone(calendar)
        except:
            self.assertTrue(False)



if __name__ == '__main__':
    unittest.main()