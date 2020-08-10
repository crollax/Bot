import sys, getopt

from botchart import BotChart
from botstrategy import BotStrategy

def main(argv):

	apiURL = "https://poloniex.com/public?command=" 
	
	callType = "returnChartData"
	
	currencyPair = "&currencyPair=BTC_XMR" 
	
	startEndPeriod = "&start=1546300800&end=1546646400&period=14400"

	fullCall = apiURL + callType + currencyPair + startEndPeriod

	chart = BotChart(fullCall)

	strategy = BotStrategy()

	for candlestick in chart.getPoints():
		strategy.tick(candlestick, False)

if __name__ == "__main__":
	main(sys.argv[1:])