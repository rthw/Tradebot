import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data

SMA = []

""" df = [10908, 11024, 11455, 11500, 11402, 10720, 9910, 9300, 9216, 8869, 9527, 9130, 9135, 8176, 8250, 8250, 7845, 8200, 8600, 8899, 8888, 8699, 8914, 8522, 8445, 8131, 7784, 7936, 7094, 6840, 6925, 6816, 7053, 7405, 6786, 6769, 6610, 6892, 7023, 6770, 6837, 6943, 7912, 7886, 7981]
 """

df = pd.read_json('candles.json')
df = df['C']

period = 9

for i in range (period):
    SMA.append(None)

i = 0
for c in df:
        tempList = df[i:i+period]
        average = sum(tempList)/period
        SMA.append (round(average, 2))
        print('i=', i)
        print('templist=', tempList)
        i+=1

del SMA[-period:]

print('lenSMA', len(SMA))

print (SMA)
plt.plot(df) 
plt.plot(SMA)
plt.show()  
