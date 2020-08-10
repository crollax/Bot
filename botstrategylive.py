from botlog import BotLog
from botindicators import BotIndicators
from bottrade import BotTrade

class BotStrategyLive(object):
    def __init__(self):
        self.output = BotLog()
        self.prices = []
        self.trades = []
        self.currentPrice = ""
        self.numSimulTrades = 1
        self.period = 15
        self.stopLoss = .0001

        self.indicators = BotIndicators()


    def tick(self, candlestick, isLive):
        if isLive:
            self.currentPrice = float(candlestick['last'])
        else:
            self.currentPrice = float(candlestick['weightedAverage'])


        self.prices.append(self.currentPrice)
        self.output.log("Price: " + str(self.currentPrice) + 
                        "\tMoving Average: " + str(self.indicators.movingAverage(self.prices, self.period)))

        self.evaluatePositions()
        self.updateOpenTrades()
        self.showPositions()


    """ Core trade logic """
    def evaluatePositions(self):
        openTrades = []

        """ Look at all open trades """
        for trade in self.trades:
            if(trade.status == "OPEN"):
                openTrades.append(trade)

        """ OPEN TRADE LOGIC """
        if(len(openTrades) < self.numSimulTrades):

            """ Measure current state against indicators """
            if(self.currentPrice < self.indicators.movingAverage(self.prices, self.period)):
                self.trades.append(BotTrade(self.currentPrice, stopLoss=self.stopLoss))

        """ CLOSE TRADE LOGIC """
        for trade in openTrades:
            if(self.currentPrice > self.indicators.movingAverage(self.prices, self.period)):
                trade.close(self.currentPrice)


    def updateOpenTrades(self):
        for trade in self.trades:
            if (trade.status == "OPEN"):
                trade.tick(self.currentPrice)


    def showPositions(self):
        for trade in self.trades:
            trade.showTrade()