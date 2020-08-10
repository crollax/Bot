import sys, getopt, time

from botlog import BotLog

class BotCandlestick(object):
    def __init__(self, period=300,open=None,close=None,high=None,low=None,priceAverage=None):
        self.current = None
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.startTime = time.time()
        self.period = period
        self.output = BotLog()
        self.priceAverage = priceAverage


    def tick(self, candlestick, isLive):
        print(candlestick)
        self.current = float(candlestick["last"])
        if (self.open is None):
            self.open = self.current

        if ((self.high is None) or (self.current > self.high)):
            self.high = self.current

        if ((self.low is None) or (self.current < self.low)):
            self.low = self.current

        if (time.time() >= (self.startTime + self.period)):
            self.close = self.current
            self.priceAverage = (self.high + self.low + self.close) / float(3)

        self.output.log("OPEN: " + str(self.open) + " CLOSE: " + str(self.close) + " HIGH: " + 
            str(self.high) + " LOW: " + str(self.low) + " CURRENT: " + str(self.current))


    def isClosed(self):
        if (self.close is not None):
            return True
        else:
            return False