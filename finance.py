import datetime as dt 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2016, 1, 1)
end = dt.datetime(2017, 12, 31)

df = web.DataReader('TSLA', 'quandl', start, end)
print(df.head())


import json

with open("/Users/Gospodinko/Desktop/Python/candles.json","r") as json_file:
     candles = json.load(json_file)

""" for candle in candles:
  print(candle) """