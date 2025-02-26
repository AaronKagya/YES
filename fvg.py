import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import time

# Initialize MT5 connection
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# Define FVG strategy parameters
symbol = "Jump50 index"
timeframe = mt5.TIMEFRAME_M5
fvg_threshold = 10  # Example threshold, adjust as needed

# Function to get historical data
def get_data(symbol, timeframe, bars=100):
    utc_from = datetime.now() - pd.Timedelta(days=1)
    rates = mt5.copy_rates_from(symbol, timeframe, utc_from, bars)
    return pd.DataFrame(rates)

# Function to identify FVGs
def identify_fvg(df):
    df['gap'] = df['high'].shift(1) - df['low']
    fvg = df[df['gap'] > fvg_threshold]
    return fvg

# Function to place an order
def place_order(symbol, order_type, lot=0.1):
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": order_type,
        "price": mt5.symbol_info_tick(symbol).ask if order_type == mt5.ORDER_TYPE_BUY else mt5.symbol_info_tick(symbol).bid,
        "deviation": 10,
        "magic": 234000,
        "comment": "FVG strategy",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }
    result = mt5.order_send(request)
    return result

# Main trading loop
while True:
    data = get_data(symbol, timeframe)
    fvg_zones = identify_fvg(data)
    if not fvg_zones.empty:
        last_fvg = fvg_zones.iloc[-1]
        if data.iloc[-1]['close'] > last_fvg['high']:
            result = place_order(symbol, mt5.ORDER_TYPE_BUY)
            print("Buy order placed:", result)
        elif data.iloc[-1]['close'] < last_fvg['low']:
            result = place_order(symbol, mt5.ORDER_TYPE_SELL)
            print("Sell order placed:", result)
    time.sleep(300)  # Wait for 5 minutes

# Shutdown MT5 connection
mt5.shutdown()