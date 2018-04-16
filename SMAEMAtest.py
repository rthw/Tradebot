import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np



df = pd.read_json('candles.json')
df = df['C']


def SMA(candles, period):
    
    SMA = []
    for i in range (len (candles)):
        if i < period:
            SMA.append(None)
        else:
            tempList = candles [i - period:i]
            average = sum (tempList) / period
            SMA.append (round (average, 2))
    return SMA


def EMA (candles, period):
    
    EMA = []
    initSMA = (sum (candles [:period])) / period
    multiplier = 2/(period+1)
    EMA.append (initSMA)
    for i in range (len (candles)):
        EMA.append ((candles [i] - EMA [i]) * multiplier + EMA [i])
    return EMA

ema = EMA(df, 50)
sma = SMA(df, 50)


plt.plot(df)
plt.plot(sma)
plt.plot(ema)
plt.show()