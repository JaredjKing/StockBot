import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime
import pandas_datareader as pdr
import subprocess 

def handle_response(message) -> str:
    p_message = message.lower()
    stock_code = p_message[1:]

    historical_stock_info = pdr.get_data_yahoo(symbols=stock_code, start=datetime(2020, 1, 1), end=datetime(2021, 1, 1))
    historical_stock_info.to_csv('/Users/jaredking/Stock_bot/empty_sheet.csv')
    subprocess.call("Rscript /Users/jaredking/Stock_bot/graph_maker.R", shell=True)
    
    stock_call = yf.Ticker(stock_code)
    stock_price = str(stock_call.info['regularMarketPrice'])
    if stock_price == "None":
        return 'Sorry, that stock is not recognised. Please try another one!'
    else:
        return f'The stock value is ${stock_price} USD'


