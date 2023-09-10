import yfinance as yf
import pandas as pd
from datetime import datetime
import pandas_datareader as pdr
import subprocess 

test_text = input('Enter a code:')


if test_text[0:2] == "$G":
    stock_code = test_text[2:]
    historical_stock_info = pdr.get_data_yahoo(symbols=stock_code, start=datetime(2020, 1, 1), end=datetime(2021, 1, 1))
    historical_stock_info.to_csv('/Users/jaredking/Stock_bot/empty_sheet.csv')
    make_graph = subprocess.call("Rscript /Users/jaredking/Stock_bot/graph_maker.R", shell=True)
    graph = subprocess.Popen('Users/jaredking/Stock_bot/Rplot.pdf', shell=True)
    