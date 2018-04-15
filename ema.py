def ema(candles, period):
    emas = []
    j = 1

    #get n sma first and calculate the next n period ema
    first = candles[:period]
    sma = 0
    for c in first:
        sma += c['C']
    sma /= period        
    multiplier = 2 / float(1 + period)
    emas.append({'O': candles[period - 1]['O'], 'C': candles[period - 1]['C'], 'T': candles[period - 1]['T'], 'EMA': sma})

    #EMA(current) = ( (Price(current) - EMA(prev) ) x Multiplier) + EMA(prev)
    emas.append({'O': candles[period]['O'], 'C': candles[period]['C'], 'T': candles[period]['T'], 'EMA': ((candles[period]['C'] - sma) * multiplier) + sma})

    #now calculate the rest of the values
    for candle in candles[period+1:]:
        tmp = ((candle['C'] - emas[j]['EMA']) * multiplier) + emas[j]['EMA']
        emas.append({'O': candles[period+j]['O'], 'C': candles[period+j]['C'], 'T': candles[period+j]['T'], 'EMA': tmp})
        j = j + 1

    return emas
