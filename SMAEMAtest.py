import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

df = pd.read_json('candles.json')
closes = df['C']

def SMA(closes, period):
    
    SMA = []
    for i in range (len (closes)):
        if i < period:
            SMA.append(None)
        else:
            tempList = closes [i - period:i]
            average = sum (tempList) / period
            SMA.append (round (average, 2))
    return SMA

def EMA (closes, period):
    
    EMA = []
    initSMA = (sum (closes [:period])) / period
    multiplier = 2/(period+1)
    EMA.append (initSMA)
    for i in range (len (closes)):
        EMA.append ((closes [i] - EMA [i]) * multiplier + EMA [i])
    return EMA

def tenkan(df, period):
    
    tenkan = []
    highs = df['H']
    lows = df['L']
    for i in range (len (highs)):
        if i < period:
            tenkan.append(None)
        else:
            tempHighs = highs [i - period:i]
            tempLows = lows [i - period:i]
            averageHighs = sum (highs) / period
            averageLows = sum (lows) / period
            tenkan.append ((averageHighs + averageLows)/2)
    return tenkan

SMAS = pd.rolling_mean(closes, 50)

ema = EMA(closes, 50)
sma = SMA(closes, 50)
tenkan = tenkan(df, 9)

#span here has arbitrary 26 period
period = 26
lagSpan = closes.shift(-period)

#PLOT ALL THE STUFF!!!
#plt.plot(lagSpan)
plt.plot(closes)
plt.plot(SMAS)
plt.plot(ema)
#plt.plot(tenkan)
plt.show()
