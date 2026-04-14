import pandas as pd

class MTFAnalyzer:
    def __init__(self, client):
        self.client = client

    def get_candles(self, asset, timeframe, count=50):
        return self.client.api.get_candles(asset, timeframe, count, 0)

    def trend(self, candles):
        closes = [c["close"] for c in candles]
        if closes[-1] > sum(closes)/len(closes):
            return "UP"
        return "DOWN"

    def analyze(self, asset):
        m1 = self.get_candles(asset, 60)
        m5 = self.get_candles(asset, 300)
        m15 = self.get_candles(asset, 900)

        return {
            "m1": self.trend(m1),
            "m5": self.trend(m5),
            "m15": self.trend(m15)
        }
