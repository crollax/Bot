class BotIndicators(object):
    def __init__(self):
        pass
    

    def movingAverage(self, dataPoints, period):
        # print("dataPoints", dataPoints)
        if(len(dataPoints) > 1):
            return sum(dataPoints[-period:]) / float(len(dataPoints[-period:]))
        else:
            return float(0)