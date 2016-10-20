import pandas_datareader.data as web 
import pandas as pd
import numpy as np
import time
import datetime
import Openmarket 

class StockList():
    
    def __init__(self, start, end):
        df=pd.read_csv('S&P500index.csv')
        stocks = df.iloc[:, 0].tolist()
        volumes=([None]*len(stocks))
        now_time = datetime.datetime.now()
        y_time = now_time + datetime.timedelta(days=-1)
        y_time_nyr = y_time.strftime('%Y-%m-%d')
        


        for i in range(len(volumes)):
            if Openmarket.Openmarket(y_time_nyr).judgeWeekend(t=5) == False:
                volumes[i] = 0
            else: 
                volumes[i] = web.DataReader(stocks[i], 'yahoo', y_time_nyr, y_time_nyr).Volume[y_time_nyr]
                    
        self._df = pd.DataFrame({'stock': stocks, 'volume':volumes})
        self._df = self._df.set_index('stock')
        

    def topNVolume(self, n = 5, order = False, minVolume = 0):
        if minVolume == 0:
            r = self._df.sort_values(by='volume', ascending=False)[:n]
            if order:
                return r
            else:
                return r.sort_index()
        else:
            return self._df[self._df.volume >= minVolume]        