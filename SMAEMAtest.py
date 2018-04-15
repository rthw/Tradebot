import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd



df = pd.read_json('candles.json')
df = df['C']

period = 9

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

print (SMA)
plt.plot(df) 
plt.plot(SMA)
plt.show()  