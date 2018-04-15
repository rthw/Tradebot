def backtestStrategy(candles, strategy) {

    states = ["Looking for entry", "Looking for exit"]    
    taken_trades = []

    bot_state = states[0]
    trade_entry = 0
    trade_exit = 0
    trade_entry_ts = ""
    trade_exit_ts = ""

    for candle, index in enumerate(candles):
        # bot is looking for entry
        if bot_state == states[0]:
            if strategy.isEntry(candles, index):
                bot_state = states[1]
                trade_entry = candle['C']
                trade_entry_ts = candle['T']
                
        # bot is looking for exit
        elif bot_state == states[1]:
            if strategy.isExit(candles, index):
                bot_state = states[0]
                trade_exit = candle['C']
                trade_exit_ts = candle['T']
                taken_trades.append({'entry': trade_entry, 'exit': trade_exit, 'entry_ts': trade_entry_ts, 'exit_ts': trade_exit_ts})

    return taken_trades
}