from Screener import screener
import multiprocessing as mp
import os
import pandas as pd
if __name__ == "__main__":   
    # loadprocess = mp.Process(target=screener.load, )
    # loadprocess.start()
    # length_dir = (len(os.listdir('dumpSplit')))
    # count = 0
    # # for i in range(0,length_dir):
    # coreprocess = mp.Process(target=screener.get_data_indicators(loadprocess=0,index=f"dumpSplit/0.csv"), )
    # coreprocess.start()
    data = pd.read_csv("dumpSplit/0.csv",index_col=0)
    df = pd.DataFrame(data)
    df.columns = ["Symbol"]
    df = df.to_csv()
    

    print(df)
    # print(df['Symbol'])
    


   
