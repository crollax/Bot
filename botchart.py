from poloniex import poloniex
import requests

class BotChart(object):

    def __init__(self, fullCall):
        self.fullCall = fullCall
        self.data = requests.get(self.fullCall).json()


    def getPoints(self):
        return self.data


    def getCurrentPrice(self, currentPriceCall, currencyPair):

        print("Call:", currentPriceCall)
        print("Currency Pair:", currencyPair)

        if (currentPriceCall):
            currentValues = requests.get(currentPriceCall).json()
            lastPairPrice = {}
            lastPairPrice = currentValues[currencyPair]
            return lastPairPrice
        else:
            return []