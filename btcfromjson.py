import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data

df = pd.read_json('candles.json')

df.set_index('T')

print(df.tail())
df[['C','O']].plot()
plt.show() 

        