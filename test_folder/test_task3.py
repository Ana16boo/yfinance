import yfinance as yf
import unittest
from unittest.mock import Mock
from unittest.mock import patch
import pandas as pd

symbols = ['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD']
tickers = [yf.Ticker(symbol) for symbol in symbols]


class TestEvent1(unittest.TestCase):
    def __init__(self):
        self.msft = yf.Ticker("MSFT")
        self.utils_mock = patch('yfinance.base.utils.get_json', autospec=True).start()
        self.addCleanup(patch.stopall)

    def test_proper_date(self):
        data = {'earningsDate': [1619481600, 1620000000], 'earningsAverage': 1.77, 'earningsLow': 1.69,
                'earningsHigh': 1.93, 'revenueAverage': 41030500000, 'revenueLow': 40541000000,
                'revenueHigh': 41894000000}
        
        calendar = self.msft.fill_calendar(data)
        self.assertNotEqual(calendar['earningsDate'], pd.to_datetime([1619481600, 1620000000], unit='s'))

if __name__ == '__main__':
    unittest.main()