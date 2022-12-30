import tradingview_ta 
from tradingview_ta import TA_Handler, Exchange
import pandas as pd
import json as j
import multiprocessing as mp
from multiprocessing import Lock,Process
import time
import os
from IPython.display import clear_output


finState = True


# class Interval:
#     INTERVAL_1_MINUTE = "1m"
#     INTERVAL_5_MINUTES = "5m"
#     INTERVAL_15_MINUTES = "15m"
#     INTERVAL_30_MINUTES = "30m"
#     INTERVAL_1_HOUR = "1h"
#     INTERVAL_2_HOURS = "2h"
#     INTERVAL_4_HOURS = "4h"
#     INTERVAL_1_DAY = "1d"
#     INTERVAL_1_WEEK = "1W"
#     INTERVAL_1_MONTH = "1M"


def get_data(symbol,screener="India",exchange="NSE",interval='1d'):
    print(symbol)
    data = TA_Handler (
        symbol=symbol,
        screener=screener,
        exchange=exchange,
        interval=interval,
        # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
    )
    return data

def getquotes():
    file = open("Quotes.Aria","r+")
    data = file.readline()
    file.close()
    return data


def Extract_data():
    stock_info = pd.read_csv("data.csv",index_col=None)
    tofile = stock_info["Symbol"].to_json()
    f = open("Quotes.Aria","w+")
    f.write(str(tofile))
    f.close()

# Extract_data()

data = getquotes()
data = j.loads(data)

def get_data_indicators():
    for i in data:
        if data[i] == "BPCL":
            break
        try:
            temp = get_data(symbol=data[i]).get_analysis().indicators
            # temp[whichIndicator]
            # temp = get_data(symbol=data[i].get_analysis().indicators)
            
        except:
            continue
    global finState
    finState = False

    
   
    
   
# all = pd.read_csv("AllStocks.csv",index_col=0)
# all = all['Symbol'].to_list()
# for i in all:
#         try:
#             temp = get_data(symbol=i).get_analysis().indicators 
#         except:
#             print("Not found",end=" ")
#             continue

import sys

def load():
    delay = 0
    i = 10000
    
    
   
    # print("load main ",os.getpid())

    while True:
        global finState
        if finState:
            
            break
        sys.stdout.write('-\r')
        time.sleep(delay)
        sys.stdout.flush()
        sys.stdout.write('\\ \r')
        time.sleep(delay)
        sys.stdout.flush()
        sys.stdout.write('|\r')
        time.sleep(delay)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('/\r')
        
    
    
        

if __name__ == "__main__":
    
    mp.freeze_support()
    mp.set_start_method('fork')
    p1 = mp.Process(target=load, )
    p2 = mp.Process(target=get_data_indicators, )

    p2.start()
    p1.start()
    p1.join()
   
    

  
    