from tradingview_ta import TA_Handler
import tradingview_ta
from pandas import read_csv as pd
import pandas as pd
import json as j
import multiprocessing as mp
import time
from IPython.display import clear_output
import sys
from math import ceil,floor
import re 

class bcolors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"


class screener:
    def get_data(symbol,screener="India",exchange="NSE",interval='1d'):
        
        data = TA_Handler (
            symbol=symbol,
            screener=screener,
            exchange=exchange,
            interval=interval,
            
        )
        return data

    def getquotes(index="NSE.all"):
        file = open(index,"r+")
        data = file.readline()
        file.close()
        return data


    def Extract_data(filename,storefilename):
        stock_info = pd.read_csv(filename,index_col=None)
        tofile = stock_info["Symbol"].to_json()
        f = open(storefilename,"w+")
        f.write(str(tofile))
        f.close()


    def get_data_indicators(loadprocess,index='NSE.all'):
        data = screener.getquotes(index=index)
        data = j.loads(data)
        stockfoundcount = 0
        interval = ["5m","15m","30m","1h","2h","4h","1d","1W","1M"]
        for k in interval:
            stockfound = []
            stockfoundcount1 = 0
            for i in data:
                try:
                    stockinfo = screener.get_data(symbol=data[i],interval=k).get_analysis().indicators
                    stockfoundcount1+=1
                    sys.stdout.write(str(stockfoundcount1)+"\r")
                    sys.stdout.flush()
                    screener.tofiles(stockinfo,data[i],interval=k)
                    # if (stockinfo["MACD.macd"] == stockinfo["MACD.signal"]) or (stockinfo["MACD.macd"] >= (stockinfo["MACD.signal"]+0.05)):
                    # if (stockinfo["RSI"] >= 58.5 and stockinfo["RSI"] < 63) and stockinfo["close"]<stockinfo["Pivot.M.Fibonacci.R2"]:
                    # # if stockinfo['high']>stockinfo["Pivot.M.Fibonacci.R1"] and stockinfo['high']<stockinfo["Pivot.M.Fibonacci.R2"] and stockinfo['RSI']>50:
                    #     stockfound.append(data[i])
                    #     stockfoundcount+=1
                    #     print(stockinfo["RSI"],data[i])
                        
                        # if stockinfo["Pivot.M.Fibonacci.R3"]<=stockinfo['close'] or stockinfo["Pivot.M.Fibonacci.R2"]<=stockinfo['close'] or stockinfo["Pivot.M.Fibonacci.R1"]<=stockinfo['close']:
                        # print(bcolors.GREEN,"Met Condition",data[i])
                    
                except:
                    continue
            print("Stocks Found",stockfound,"at ",k," interval ")
        # loadprocess.kill()
    def tofiles(stockinfo,quote,interval):
        path = "/Users/aryagirigoudar/Documents/Python /StockScreenerFREE/dump/nifty50/"+str(interval)+"/"+str(quote)+".csv"
        file = open(path,"w+")
        for i in stockinfo:
            file.write(str(i)+",")
        file.close()

        # file = open(path,"a")
        # file.write("\n")
        # for i in stockinfo:
        #     file.write(str(stockinfo[i])+",")
        # file.close()
            
    def droplast():
        df = pd.read_csv("./dump/BAJAJFINSV.csv")
        df = df.drop(df.columns[-1], axis=1)
        print(df)

    def load():
        delay = 0.1
       
        while True:
            continue

            # sys.stdout.write('-\r')
            # # sys.stdout.write(str(stockCount))
            # time.sleep(delay)
            # sys.stdout.flush()
            # sys.stdout.write('\\ \r')
            # time.sleep(delay)
            # sys.stdout.flush()
            # sys.stdout.write('|\r')
            # time.sleep(delay)
            # sys.stdout.flush()
            # time.sleep(delay)
            # sys.stdout.write('/\r')   


class Stratergy:
    def strategy(stockinfo):
        file = open("strategy.strat","r")
        condtion = str(file.read()).replace('\n',"")
        condtion = j.dumps(condtion)
        print(condtion['0'])
        file.close()
    def addindicator():
        
        try:
            stra = dict()
            condition = input("Enter indicator with limit and operator without spaces")
            condition = condition.upper()
            operator = screener.ExtractOperator(condition)
            indictor = condition.split(operator)[0]
            limit = condition.split(operator)[1]
            stra[indictor] = {"limit":limit,"operator":operator}
            return stra
        except:
            print("Cant Insert")
        
            
    def deletestrategy():
        pass
    def addstrategy():
        final = dict()
        file = open("strategy.strat","a")
        n = int(input("how many indicator"))
        for i in range(0,n):
            stra = screener.addindicator()
            final[i] = stra
        jsonload = j.dumps(final,indent=3)
        file.writelines('\n'+str(jsonload))
        file.close()



    def ExtractOperator(string):
        operators = ['>', '<', '<=', '>=', '+', '-', '*', '/', '%', '**', '//', '=', '+=', '-=', '==', '*=', '/=', '%=', '//=', '!=', '&=', '|=', '^=', '>>=', '<<=']
        r = re.compile( '|'.join( '(?:{})'.format(re.escape(o)) for o in sorted(operators, reverse=True, key=len)) )

        for pattern in string:
            if pattern in operators:
                return str(pattern)
if __name__ == "__main__":   
    # screener.Extract_data(filename="data.csv",storefilename="NSE.nifty50")
    # loadprocess = mp.Process(target=screener.load, )
    # loadprocess.start()
    coreprocess = mp.Process(target=screener.get_data_indicators(loadprocess=0,index="NSE.nifty50"), )
    coreprocess.start()
    
    # print(tradingview_ta.__file__)
    # screener.addstrategy()
    # Stratergy.strategy(0)
   
    
   
    

    