import pandas as pd

def SMA(candles, period):
    
    SMA = []
    for i in range(len(candles)):
        if i < period:
            SMA.append(None)
        else:
            tempList = candles[i:i+period]
            average = sum(tempList)/period
            SMA.append (round(average, 2))

    del SMA[-period:]
