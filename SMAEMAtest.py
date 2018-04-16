import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np



df = pd.read_json('candles.json')
df = df['C']


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
    return SMA


sma = SMA(df, 9)


plt.plot(df)
plt.plot(sma)
plt.show()