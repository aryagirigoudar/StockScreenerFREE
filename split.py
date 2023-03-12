import pandas as pd
import os 
import shutil
import multiprocessing as mp
import Screener 
import time
import threading 
start = time.time()

data = pd.read_csv("data.csv",index_col=None)
indices = data["Symbol"].to_list()
count = 0

def split(li,name):
    d = pd.DataFrame(li)
    d.to_csv(str(name)+".csv")
    




def run():
    col = 0
    global count
    li = list()
    for i in indices:
        li.append(i)
        if count>5:
            split(li,col)
            shutil.move(f'{col}.csv', f'dumpSplit/{col}.csv')
            count=0
            col+=1
            li.clear()

        count+=1


countloop = 0
def mprocess(col):
    global countloop
    d = pd.read_csv(f'dumpSplit/{col}.csv',index_col=0)

   
    for i in d['0']:
        countloop+=1
        try:
            data = Screener.screener.get_data(symbol=i).get_analysis().indicators
        except:
            continue
    

def getcount():
    dir_path = 'dumpSplit/'
    count = 0
    for path in os.listdir(dir_path):
  
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1

    return count



if __name__ == "__main__":
    # symbol,screener="India",exchange="NSE",interval='1d'):
    
    # length_dir = (len(os.listdir('dumpSplit')))
    count = getcount()
    
    # # mprocess(3)
    countThread = 0
    d = pd.read_csv('data.csv')
    for i in d["Symbol"]:
        try:
            data = Screener.screener.get_data(symbol=i).get_analysis().indicators
        except:
            pass
        print(i)
    # for i in range(1,count-1):
        # mprocess(i)
        # countThread+=1
        # if i%2==0:
        #     loadprocess = mp.Process(target=mprocess(i))
        #     loadprocess.start()
        #     print(loadprocess.pid)
        # else:
        #     loadprocess = threading.Thread(target=mprocess(i))
    end = time.time()   
    print(end - start)



       
   
   
