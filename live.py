import sys, getopt, time

from botchart import BotChart
from botstrategy import BotStrategy
from botlog import BotLog
from botcandlestick import BotCandlestick


def main(argv):

    apiURL = "https://poloniex.com/public?command=" 
	
    callType = "returnChartData"
	
    currencyPair = "BTC_XMR" 
	
    startEndPeriod = "&start=1546300800&end=1546646400&period=14400"

    fullCall = apiURL + callType + "&currencyPair=" + currencyPair + startEndPeriod
    currentPriceCall = apiURL + "returnTicker"

    chart = BotChart(fullCall)
    strategy = BotStrategy()

    period = 10
    sleep = 10
    candlesticks = []
    developingCandlestick = BotCandlestick(period=period)

    # """ SINGLE """
    # while True:
    #     try:
    #         candlestick = chart.getCurrentPrice(currentPriceCall, currencyPair)
    #     except urllib2.URLError:
    #         time.sleep(int(30))
    #         candlestick = chart.getCurrentPrice(currentPriceCall, currencyPair)

    #     print(candlestick)
    #     strategy.tick(candlestick, True)
    #     time.sleep(int(10))


    """ MULTI """
    while True:
        try:
            developingCandlestick.tick(chart.getCurrentPrice(currentPriceCall, currencyPair), True)
        except urllib2.URLError:
            time.sleep(int(sleep))
            developingCandlestick.tick(chart.getCurrentPrice(currentPriceCall, currencyPair), True)

        if (developingCandlestick.isClosed()):
            candlesticks.append(developingCandlestick)            
            strategy.tick(developingCandlestick, True)
            developingCandlestick = BotCandlestick(period=period)

        time.sleep(int(sleep))


if __name__ == "__main__":
    main(sys.argv[1:])