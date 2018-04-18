#Tenkan-sen (Conversion Line): (9-period high + 9-period low)/2))

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

#Kijun-sen (Base Line): (26-period high + 26-period low)/2))
#Senkou Span A (Leading Span A): (Conversion Line + Base Line)/2))
#Senkou Span B (Leading Span B): (52-period high + 52-period low)/2))

#Сalculating lagging span - shift pandas dataframe with closing prices by period
lagSpan = s = closes.shift(-period)